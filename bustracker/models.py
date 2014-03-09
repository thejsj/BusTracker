from django.db import models
from datetime import datetime

class SingleQuery(models.Model):

	created_at = models.DateTimeField(
		default=datetime.utcnow,
	)

	bus_line_id = models.IntegerField()

	bus_stop_id = models.IntegerField()

	query_successful = models.BooleanField()

	NORTH = 'N'
	SOUTH = 'S'
	WEST  = 'W'
	EAST  = 'E'

	DIRECTION = (
		( NORTH, 'North'),
		( SOUTH, 'South'),
		( WEST , 'West'),
		( EAST , 'South'),
	)

	direction = models.CharField(
		max_length=1,
		choices=DIRECTION,
	)

	time_remaining = models.IntegerField(
		blank = True,
		null = True,
		default = None,
	)

	def save(self, *args, **kwargs):

		# Parse Direction If Necessary 
		if len( self.direction ) > 1:
			for direction in self.DIRECTION:
				if direction[ 1 ] == self.direction:
					self.direction = direction[ 0 ]

		super(SingleQuery, self).save(*args, **kwargs)