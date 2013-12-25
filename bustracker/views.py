from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.sites.models import get_current_site

# Local
from busTrackerQuery.routequery import Route, RouteQuery
from busTrackerQuery.mandrillmailer import MandrilMessagelMailer
from datetime import datetime
import time
import json
from django.utils import simplejson
from django.conf import settings

routes = [
	{'route' : 74, 'direction' : 'North', 'id' : 779},
	{'route' : 74, 'direction' : 'South', 'id' : 54}
]

times = [
	{'hour' : 8,  'min' : 0,  'id' : 54 , 'time_remaining' : None},
	{'hour' : 8,  'min' : None,  'id' : 54 , 'time_remaining' : 15},
	{'hour' : 8,  'min' : None,  'id' : 54 , 'time_remaining' : 20},
	{'hour' : 17, 'min' : 0,  'id' : 54 , 'time_remaining' : None},
	{'hour' : 17, 'min' : 15, 'id' : 54 , 'time_remaining' : None},
	{'hour' : 17, 'min' : None, 'id' : 54 , 'time_remaining' : 20},
	{'hour' : 17, 'min' : None, 'id' : 54 , 'time_remaining' : 15},
]

def main(request):

	route_parent = Route()

	# List of Queries
	all_route_queries = {}
	for route in routes: 
		# Form Query
		all_route_queries[route['id']] = RouteQuery(route)

	# Parse Response
	response = {}
	for a in all_route_queries:
		response[a] = {} 
		response[a]['route_id'] = str(all_route_queries[a].route_id) 
		response[a]['stop_id'] = str(all_route_queries[a].stop_id) 
		response[a]['direction'] = str(all_route_queries[a].direction) 
		response[a]['status'] = str(all_route_queries[a].status) 
		response[a]['minutes'] = str(all_route_queries[a].minutes)
		response[a]['url'] = str(all_route_queries[a].url)
		response[a]['stops_away'] = str(all_route_queries[a].stops_away)

	return render(
        request, 
        'index.html',
        {
            'all_route_queries' : response,
            'static_root' : settings.STATIC_ROOT
        })

@csrf_exempt
def ajax_request(request):
	route_parent = Route()

	# List of Queries
	all_route_queries = {}
	for route in routes: 
		# Form Query
		all_route_queries[route['id']] = RouteQuery(route)

	# Parse Response
	response = {}
	for a in all_route_queries:
		response[a] = {} 
		response[a]['route_id'] = str(all_route_queries[a].route_id) 
		response[a]['stop_id'] = str(all_route_queries[a].stop_id) 
		response[a]['direction'] = str(all_route_queries[a].direction) 
		response[a]['status'] = str(all_route_queries[a].status) 
		response[a]['minutes'] = str(all_route_queries[a].minutes)
		response[a]['url'] = str(all_route_queries[a].url)
		response[a]['stops_away'] = str(all_route_queries[a].stops_away)

	return HttpResponse(
        json.dumps(response), 
       	mimetype='application/json'
        )

def cronjob(request):
	# for t in times: 
	# 	if t['hour'] is now.hour and t['min'] is now.minute and t['id'] in all_route_queries:
	# 		response += "FOUND FOUND FOUND"
	# 		# mailer = MandrilMessagelMailer(all_route_queries[779].getMessageString())
	# 		# print "Sending Email"
	# 		# print all_route_queries[t['id']].stop_id
	# 		# print all_route_queries[t['id']].status
	# 		response += all_route_queries[t['id']].getMessageString()
	# 		# print all_route_queries[t['id']].minutes
	return HttpResponse('Feature Not Currently Available')

