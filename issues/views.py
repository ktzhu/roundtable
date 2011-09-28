# Create your views here.

from django.views.generic.simple import direct_to_template
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from models import Issue, Solution, User

def latest(request):
    return redirect(Issue.objects.latest(field_name='pk'))  

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
        author = User.objects.get(pk=request.user.pk)
        Solution.objects.create(
            title=request.POST['title'], 
            body=request.POST['body'],
            issue=issue,
            author=author,
            )

    return direct_to_template(request, 'resolve.html', {
        'issue': issue,
        'solutions': issue.solutions.all(),
    })