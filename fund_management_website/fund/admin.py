from django.contrib import admin
from fund.models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ApplicationData)
admin.site.register(BudgetProfile)
admin.site.register(SubBudgetProfile)
admin.site.register(BudgetItems)
admin.site.register(SpendingProfile)
admin.site.register(SpendingItems)
admin.site.register(EvidenceFile)