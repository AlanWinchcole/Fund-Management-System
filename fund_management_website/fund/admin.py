""" Register all models to admin page"""
from django.contrib import admin
from django.contrib.auth.models import Group, User

from fund.models import UserProfile, ApplicationData, BudgetProfile\
    ,BudgetItems, SpendingProfile, SpendingItems, EvidenceFile, Comments, Review


# Register your models here.
# unregister these at code freeze
admin.site.register(UserProfile)
admin.site.register(ApplicationData)
admin.site.register(BudgetProfile)
admin.site.register(BudgetItems)
admin.site.register(SpendingProfile)
admin.site.register(SpendingItems)
admin.site.register(EvidenceFile)
admin.site.register(Comments)
admin.site.register(Review)


admin.site.unregister(Group)


# Admin site header
admin.site.site_header = 'Scottish Borders Admin Console'

#class UserAdmin(admin.ModelAdmin):
    #list_filter = ('date_joined', 'is_superuser', 'is_staff', 'is_active')

#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)
