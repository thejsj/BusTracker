from bs4 import BeautifulSoup
import urllib 
import urllib2
import re
from datetime import datetime
import json
import os
from bustracker.models import SingleQuery
from django.utils.timezone import utc

"""

Get Current Time
http://grtcbustracker.com/bustime/map/getTimeAndTemp.jsp
Get Time Remaining Through Simple Html Page
http://grtcbustracker.com/bustime/wireless/html/eta.jsp?route=74&direction=North%20Bound&id=1693&showAllBusses=off

"""

class Route:

	def __init__(self):
		pass

	def getHeaderList(self):
		return ['route', 'stop', 'direction', 'status', 'minutes', 'timestamp', 'time']

class RouteQuery(Route):

	def __init__(self, route, get_future_stops=False):
		self.route_id = str(route['route'])
		self.direction = route['direction']
		self.stop_id = str(route['id'])
		self.time = datetime.now()
		self.status, self.minutes = self.query(self.route_id, self.direction, self.stop_id)
		if get_future_stops:
			self.stops_away, self.message = self.getNumberOfStopsAway(self.route_id, self.direction, self.stop_id)

	def query(self, route, direction, stop):
		# Form Url
		url = 'http://grtcbustracker.com/bustime/wireless/html/eta.jsp?route='
		url += str(route) + '&direction=' + str(direction)
		url += '%20Bound&id=' + str(stop) + '&showAllBusses=off' 

		self.url = url

		req = urllib2.Request(url) 
		response = urllib2.urlopen(req) 
		page = response.read()

		soup = BeautifulSoup(page)

		for element in soup.body:
			if element.name == 'font':
				for sub_element in element:
					if sub_element.name == 'b':
						if 'arrival' in sub_element.text.lower() or 'min' in sub_element.text.lower() or 'due' in sub_element.text.lower():
							# If Has Minutes
							if 'min' in sub_element.text.lower():
								minutes = int(re.match(r'\d+', sub_element.text).group())	
								return 'transition', minutes, 
							# If Has 'Due'
							if 'due' in sub_element.text.lower():
								return 'due', 0
		return None, None

	def getNumberOfStopsAway(self, route, direction, stop):
		
		# Check if self is is 'due' or 'approcahing'
		if self.status is 'due':
			return 0, self.stop_id

		# Load Json with Stops
		this_file_path = os.path.dirname(os.path.dirname(__file__))
		json_path = os.path.join(this_file_path, 'busTrackerQuery/schedule/weekday/' + route + '.json')
		bus_line_schedeule = open(json_path, 'r').read()
		stops_list  = json.loads(bus_line_schedeule)
		
		# 
		# Arrange Array Accordingly (Our Stop First, then all other stops)
		#
		this_key = None
		for i, stop_number in enumerate(stops_list):
			if int(stop_number) == int(stop):
				this_key = i
				break
		if this_key is None:
			# This list does not have the requested stop id
			return stops_list, 'broek at key : ' + str(stop) + ' ' + str(len(stops_list))
		# Break list at key
		stops_list = stops_list[this_key:]+stops_list[:this_key]
		stops_list.reverse()
		# Query Each Stop
		all_statuses = []
		if len(stops_list) > 0:
			for stops_away, stop_number in enumerate(stops_list):
				this_status, this_minutes = self.query(self.route_id, self.direction,stop_number)
				all_statuses.append([this_status, this_minutes, stop_number])
				if this_status == 'due' or this_status == 'transition':
					return str(stops_away), this_status + ' ' + str(stop_number) + '    --    ' + str(stops_list)
		#	# If Status is due or approaching or minutes, return...
		return None, None

	def getList(self):
		return [self.route_id, self.stop_id, self.direction, self.status, self.minutes, self.time.strftime("%s"), self.time.strftime("%Y-%m-%d %H-%M-%S'")]

	def getMessageString(self):
		if self.status == 'transition':
			return str(self.minutes) + " minutes remaing. Bus # " + str(self.route_id) + " / Stop # " + str(self.stop_id) + '.'
		elif self.status is None:
			return 'No Status Currently Available'
		else:
			return 'Status : ' + str(self.status) + ". Bus # " + str(self.route_id) + " / Stop # " + str(self.stop_id) + '.'


class CompleteRouteQuery(Route):

	def __init__(self, route_id):
		self.route_id = route_id
		self.stops_list = self.getStopsList()
		self.results = self.queryAllStops()

	def getStopsList(self):
		# Load Json with All Stops
		this_file_path = os.path.dirname(os.path.dirname(__file__))
		json_path = os.path.join(this_file_path, 'busTrackerQuery/schedule/weekday/' + str( self.route_id ) + '.json')
		bus_line_schedeule = open(json_path, 'r').read()
		stops_list  = json.loads(bus_line_schedeule)

		return stops_list

	def queryAllStops(self):
		all_queries = []
		for direction in ['North', 'South']:
			for stop in self.stops_list:
				# Activate Crawler
				query_result = RouteQuery( {
					'route' : self.route_id,
					'direction' : direction,
					'id' : stop
				})
				# Check If Result Was Successful
				if query_result.minutes is not None:
					query_successful = True
				else:
					query_successful = False
				# Add Results To Database
				this_query_result = SingleQuery(
					created_at = datetime.utcnow().replace(tzinfo=utc),
					bus_line_id = self.route_id,
					direction = direction,
					bus_stop_id = stop,
					query_successful = query_successful,
					time_remaining = query_result.minutes,
				)
				this_query_result.save()
				all_queries.append( this_query_result.pk )
		return all_queries