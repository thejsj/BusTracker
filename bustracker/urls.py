from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Main:
    url(r'^$', 'bustracker.views.main', name='main'),
    
    # API:
    url(r'^api/', 'bustracker.views.ajax_request', name='ajax'),

    url(r'^admin/', include(admin.site.urls)),
)
