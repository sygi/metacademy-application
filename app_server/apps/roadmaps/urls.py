from django.conf.urls import patterns, url

from apps.roadmaps import views

urlpatterns = patterns('',
                       url(r'^([^/]+)/([^/]+)$', views.get_roadmap),
                       url(r'^([^/]+)/([^/]+)/edit$', views.edit_roadmap),
                       )
