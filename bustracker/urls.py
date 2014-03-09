from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Main:
    url(r'^$', 'bustracker.views.main', name='main'),
    url(r'^admin/', include(admin.site.urls)),
)
