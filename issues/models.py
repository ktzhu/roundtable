from django.db import models
from django.contrib.auth import models as auth
from django.template.defaultfilters import slugify
from datetime import datetime

class Issue(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
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
                return option
        
        return None
            
    def save(self, *vargs, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super(Issue, self).save(*vargs, **kwargs)

    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/{slug}/discover/".format(slug=self.slug)

class Solution(models.Model):
    issue = models.ForeignKey(Issue, related_name='solutions')
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey('issues.User')

    def __unicode__(self):
        return self.title

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