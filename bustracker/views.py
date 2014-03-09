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
from busTrackerQuery.routequery import Route, RouteQuery, CompleteRouteQuery
from busTrackerQuery.mandrillmailer import MandrilMessagelMailer
from datetime import datetime
import time
import json
from django.utils import simplejson
from django.conf import settings


def main(request):

	route_parent = Route()

	complete_query = CompleteRouteQuery( 74 )

	raise Exception( complete_query.results )

	return render(
        request, 
        'index.html',
        {
            'all_route_queries' : response,
            'static_root' : settings.STATIC_ROOT
        })
