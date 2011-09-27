# Create your views here.

from django.views.generic.simple import direct_to_template
from django.http import HttpResponse

def hello(request):
    return HttpResponse("hello world")