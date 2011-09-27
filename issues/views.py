# Create your views here.

from django.views.generic.simple import direct_to_template
from django.http import HttpResponse

def discover(request, issue):
    return direct_to_template(request, 'discover.html', {
        'issue': issue,
    })

def discuss(request, issue):
    return direct_to_template(request, 'discuss.html', {
        'issue': issue,
    })

def resolve(request, issue):
    return direct_to_template(request, 'resolve.html', {
        'issue': issue,
    })