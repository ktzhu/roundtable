from django.contrib import admin
from roundtable.issues import models as issues

class IssueAdmin(admin.ModelAdmin):
    pass

class SolutionAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass

class RatingAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(issues.Issue, IssueAdmin)