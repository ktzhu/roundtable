# Create your views here.

from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from models import Issue, Solution

def discover(request, issue):
    issue = get_object_or_404(Issue, slug=issue)
    
    return direct_to_template(request, 'discover.html', {
        'issue': issue,
    })

def discuss(request, issue):    
    issue = get_object_or_404(Issue, slug=issue)
    
    return direct_to_template(request, 'discuss.html', {
        'issue': issue,
    })

def resolve(request, issue):
    issue = get_object_or_404(Issue, slug=issue)

    if request.method == 'POST':
        Solution.objects.create(**request.POST)

    return direct_to_template(request, 'resolve.html', {
        'issue': issue,
        'solutions': issue.solutions.all(),
    })