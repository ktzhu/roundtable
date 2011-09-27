from django.conf.urls.defaults import patterns, include, url
from surlex.dj import surl
import issues

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    surl('<issue:s>/discover/', 'issues.views.discover'),
    surl('<issue:s>/discuss/', 'issues.views.discuss'),
    surl('<issue:s>/resolve/', 'issues.views.resolve'),
)
