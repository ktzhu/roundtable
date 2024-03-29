from django.conf.urls.defaults import patterns, include, url
from surlex.dj import surl
import issues

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    surl('^admin/', include(admin.site.urls)),
    surl('^comments/', include('django.contrib.comments.urls')),
    surl('^', include(issues.urls)),
)
