from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator



# Create your models here.
class UserProfile(models.Model) :
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    regex_validator = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
    contact_number = models.CharField(validators=[regex_validator], max_length=12, blank=True)

    def __str__(self) :
        return self.user.username


class ApplicationData(models.Model) :
    user = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    organisationName = models.CharField(max_length=200, null=True, blank=True)
    projectTitle = models.CharField(max_length=200, null=True, blank=True)
    CH_OSCR_number = models.CharField(max_length=20, unique=True, blank=True, null=True, )
    projectDesc = models.TextField(max_length=300, null=True, blank=True)
    userGroupDesc = models.TextField(max_length=300, null=True, blank=True)
    learningOpp = models.TextField(max_length=300, null=True, blank=True)
    keyPartnersWork = models.TextField(max_length=300, null=True, blank=True)
    projImpactClimate = models.TextField(max_length=300, null=True, blank=True)
    projSupportLocBus = models.TextField(max_length=300, null=True, blank=True)
    proContribution = models.TextField(max_length=300, null=True, blank=True)

    length = models.IntegerField(null=True, blank=True)
    application_complete = models.BooleanField(default=False)

    def save(self, *args, **kwargs) :
        super(ApplicationData, self).save(*args, **kwargs)

    def __str__(self) :
        return self.projectTitle

    class Meta :
        verbose_name_plural = "ApplicationData"


# Each application has a budget profile
class BudgetProfile(models.Model) :
    # One application can only have one budget profile
    associated_application = models.OneToOneField(ApplicationData, on_delete=models.CASCADE, blank=True, null=True)
    totalBudget = models.DecimalField(max_digits=10, decimal_places=2)
    objects = models.Manager()

# Budget profile would be divided into different headings
class SubBudgetProfile(models.Model):
    associated_budget_profile = models.ForeignKey(BudgetProfile, on_delete=models.CASCADE, blank=True, null=True)
    heading = models.CharField(max_length=255, null=False, blank=False, unique=True, primary_key=True)
    budget_allocation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sub_budget_slug = models.SlugField(max_length=255, unique=True,blank=True, null=True)

    def save(self, *args, **kwargs):
        self.sub_budget_slug = slugify(self.heading)
        super(SubBudgetProfile, self).save(*args, **kwargs)

    def __str__(self):
        return self.heading

# Each heading will be itemised
class BudgetItems(models.Model):
    ID = models.AutoField(primary_key=True)
    heading = models.ForeignKey(SubBudgetProfile, on_delete=models.CASCADE, blank=True, null=True)
    #heading = models.CharField(max_length=255, blank=False, null=False)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    budget_allocation = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name


# Heading wise Spending Profile
class SpendingProfile(models.Model):
    associated_budget_profile = models.OneToOneField(SubBudgetProfile, on_delete=models.CASCADE, null=False)
    total_money_spent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

# https://www.geeksforgeeks.org/filefield-django-models/
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# Each heading has itemised expenditure
class SpendingItems(models.Model):
    associated_spending_profile = models.ForeignKey(SpendingProfile, on_delete=models.CASCADE, null=False)
    item_name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    money_spent = models.DecimalField(max_digits=10, decimal_places=2)
    evidence = models.FileField(upload_to=user_directory_path)

# Model to allow multiple file uploads
class EvidenceFile(models.Model):
    file = models.FileField(upload_to=user_directory_path)
    spending_profile = models.ForeignKey(SpendingProfile, on_delete=models.CASCADE, related_name='evidences')

