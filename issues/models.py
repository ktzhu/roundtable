from django.db import models
from django.contrib.auth import models as auth
from datetime import datetime

class Issue(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    # phase scheduling
    discover = models.DateTimeField()
    discuss = models.DateTimeField()
    resolve = models.DateTimeField()
    vote = models.DateTimeField()

    @property
    def phase(self):
        now = datetime.today()
        
        for option in ['vote', 'resolve', 'discuss', 'discover']:
            if getattr(self, option) <= now:
                return options
        
        return None
            

class Solution(models.Model):
    issue = models.ForeignKey(Issue, related_name='solutions')
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey('issues.User')

class User(auth.User):
    subscriptions = models.ManyToManyField(Issue, related_name='subscribers')
    proxied_subscriptions = models.ManyToManyField(Issue, related_name='proxies')

RATINGS = (
    (1, 'poor'),
    (2, 'fair'),
    (3, 'good'),
    (4, 'great'),
    )

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings')
    solution = models.ForeignKey(Solution, related_name='ratings')
    score = models.IntegerField(choices=RATINGS)