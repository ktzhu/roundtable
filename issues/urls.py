from django.conf.urls.defaults import patterns, include, url
from surlex.dj import surl

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    surl('accounts/login/', 'django.contrib.auth.views.login', 
        {'template_name': 'login.html'}),
    surl('$', 'issues.views.overview'),
    surl('latest/', 'issues.views.latest'),
    surl('<issue:s>/discover/', 'issues.views.discover'),
    surl('<issue:s>/discuss/', 'issues.views.discuss'),
    surl('<issue:s>/resolve/', 'issues.views.resolve'),
)
