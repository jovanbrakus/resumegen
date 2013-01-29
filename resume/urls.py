from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'resume.views.home'),  
    url(r'^generate/$', 'resume.views.generate'),  
)
