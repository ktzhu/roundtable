from django.conf.urls.defaults import patterns, include, url
from surlex.dj import surl
import issues

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    surl('hello', 'issues.views.hello'),
)
