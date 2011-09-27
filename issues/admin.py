from django.contrib import admin
from roundtable.issues import models as issues

"""
Stubbed out the model admin classes so we can easily refine
them later if we have to.
"""

class IssueAdmin(admin.ModelAdmin):
    pass

class SolutionAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass

class RatingAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(issues.Issue, IssueAdmin)
admin.site.register(issues.Solution, SolutionAdmin)
admin.site.register(issues.User, UserAdmin)
admin.site.register(issues.Rating, RatingAdmin)