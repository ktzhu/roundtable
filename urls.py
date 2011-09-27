from django.conf.urls.defaults import patterns, include, url
from surlex.dj import surl

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    surl(r'^/', include())
    surl(r'^admin/', include(admin.site.urls)),
    surl(r'^comments/', include('django.contrib.comments.urls')),
)
