from django.db import models
from django.contrib.auth import models as auth

class Issue(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    # phase scheduling
    discover = models.DateTimeField()
    discuss = models.DateTimeField()
    resolve = models.DateTimeField()
    vote = models.DateTimeField()

class Solution(models.Model):
    issue = models.ForeignKey(Issue)
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User)

class Subscription(models.Model):
    issue = models.ForeignKey(Issue)
    user = models.ForeignKey('issues.User')
    proxy = models.ForeignKey('issues.User', null=True)

class User(auth.User):
    issues = models.ManyToManyField(Issue, through=Subscription)

RATINGS = (
    (1, 'poor'),
    (2, 'fair'),
    (3, 'good'),
    (4, 'great'),
    )

class Rating(models.Model):
    user = models.ForeignKey(User)
    solution = models.ForeignKey(Solution)
    score = models.IntField(choices=RATINGS)