""" Register all models to admin page"""
from django.contrib import admin
from fund.models import UserProfile, ApplicationData, BudgetProfile, SubBudgetProfile\
    ,BudgetItems, SpendingProfile, SpendingItems, EvidenceFile, Comments, Review
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ApplicationData)
admin.site.register(BudgetProfile)
admin.site.register(SubBudgetProfile)
admin.site.register(BudgetItems)
admin.site.register(SpendingProfile)
admin.site.register(SpendingItems)
admin.site.register(EvidenceFile)
admin.site.register(Comments)
admin.site.register(Review)
