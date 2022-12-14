"""Module to define data storage"""
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator
# Create your models here.
from django.utils import timezone

class UserProfile(models.Model):
    """Define table for Users in database"""
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    regex_validator = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
    contact_number = models.CharField(validators=[regex_validator], max_length=12, blank=True)


# Each application has a budget profile
class BudgetProfile(models.Model) :
    """Define table for Budget Profile in database"""

    totalBudget = models.DecimalField(max_digits=10, decimal_places=2)
    objects = models.Manager()

class ApplicationData(models.Model) :

    class Status(models.TextChoices):
        REJECTED = 'Rejected'
        PENDING = 'Pending'
        ACCEPTED = 'Accepted'

    """Define table for Applications in database"""
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
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
    feedback = models.TextField(max_length=200, null=True, blank=True)

    length = models.IntegerField(null=True, blank=True)
    application_complete = models.BooleanField(default=False)
    date_of_application = models.DateField(null=True, blank=True)
    reviewed = models.BooleanField(default=False)
    app_status = models.TextField(choices = Status.choices, default = Status.PENDING)


    # One application can only have one budget profile
    associated_budgetProfile = models.OneToOneField(BudgetProfile, on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        """override save method to add date of application"""
        if self.application_complete:
            self.date_of_application = timezone.now()
        if self.app_status == 'Accepted':
            newSP = SpendingProfile.objects.get_or_create(associated_budget_profile = self.associated_budgetProfile, associated_application = self)[0]
            newSP.save()
            all_budget_items = BudgetItems.objects.filter(associated_budget_profile=self.associated_budgetProfile)
            for bi in all_budget_items :
                spend_items = SpendingItems(ID=bi.ID, associated_spending_profile=newSP, heading=bi.heading, item_name=bi.item_name,
                                            description=bi.description,
                                            budget_allocation=bi.budget_allocation)
                spend_items.save()
                print("Spent item has been created")

        super(ApplicationData, self).save(*args, **kwargs)

    def __str__(self):
        """returns the project title"""
        return str(self.id)

    class Meta :
        """ Further information about Application"""
        verbose_name_plural = "ApplicationData"




class Review(models.Model):

    class Light(models.IntegerChoices):
        RED = 0
        AMBER = 1
        GREEN = 2

    application = models.ForeignKey(ApplicationData, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    co_production = models.IntegerField(choices=Light.choices, default=Light.RED)
    capacity_building = models.IntegerField(choices=Light.choices, default=Light.RED)
    partnership_working = models.IntegerField(choices=Light.choices, default=Light.RED)
    climate_environment = models.IntegerField(choices=Light.choices, default=Light.RED)
    local_economic_res_building = models.IntegerField(choices=Light.choices, default=Light.RED)
    social_return_acc = models.IntegerField(choices=Light.choices, default=Light.RED)
    total_score = models.IntegerField(default=0, editable=False)

    general_feedback = models.TextField(blank=True, null=True)
    date_completed = models.DateField(null=True, blank=True, auto_now_add = True)
    review_complete = models.BooleanField(default=False)

    def score(self):
        return self.co_production + self.capacity_building + self.partnership_working + self.climate_environment + self.local_economic_res_building + self.social_return_acc


    def save(self, *args, **kwargs):
        self.application.reviewed = True
        self.total_score = self.score()
        super(Review, self).save(*args, **kwargs)


# Budget profile would be divided into different headings
# class SubBudgetProfile(models.Model):
#     """Define table for Sub Budget Profile in database"""
#     associated_budget_profile = models.ForeignKey(BudgetProfile, on_delete=models.CASCADE, blank=True, null=True)
#     heading = models.CharField(max_length=255, null=False, blank=False, unique=True, primary_key=True)
#     budget_allocation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     sub_budget_slug = models.SlugField(max_length=255, unique=True,blank=True, null=True)
#
#     def save(self, *args, **kwargs):
#         """Override save method to slugify the budget heading"""
#         self.sub_budget_slug = slugify(self.heading)
#         super(SubBudgetProfile, self).save(*args, **kwargs)


# Each heading will be itemised
class BudgetItems(models.Model):
    """Define table for Budget Items in database"""
    ID = models.AutoField(primary_key=True)
    associated_budget_profile = models.ForeignKey(BudgetProfile, on_delete=models.CASCADE, blank=True, null=True)
    heading = models.CharField(max_length=255, blank=False, null=True)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    budget_allocation = models.DecimalField(max_digits=10, decimal_places=2)


# Heading wise Spending Profile
class SpendingProfile(models.Model):
    """Define table for Spending Profile in database"""
    associated_budget_profile = models.OneToOneField(BudgetProfile, on_delete=models.CASCADE, null=True)
    associated_application = models.OneToOneField(ApplicationData, on_delete=models.CASCADE, null=True)
    total_money_spent = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

# https://www.geeksforgeeks.org/filefield-django-models/
def user_directory_path(instance, filename):
    """Defines directory path for a user"""
    sp = instance.associated_spending_profile
    bp = sp.associated_budget_profile
    ap = ApplicationData.objects.get(associated_budgetProfile = bp)
    user = ap.user
    return f"user_{user.id}/{filename}"

# Each heading has itemised expenditure
class SpendingItems(models.Model):
    """Define table for Spending Items in database"""
    ID = models.AutoField(primary_key=True)
    associated_spending_profile = models.ForeignKey(SpendingProfile, on_delete=models.CASCADE, null=True, blank=True)
    heading = models.CharField(max_length=255, blank=True, null=True)
    item_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    money_spent = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True,default=Decimal('0.00'))
    budget_allocation = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    evidence = models.FileField(upload_to=user_directory_path,blank=True, null=True)

    @property
    def calc_budget_remaining(self):
        """Calculates and returns remaining budget"""
        if self.budget_allocation and self.money_spent:
            return self.budget_allocation - self.money_spent

# Model to allow multiple file uploads
class EvidenceFile(models.Model):
    """Define table for Evidences in database"""
    file = models.FileField(upload_to=user_directory_path,blank=True, null=True)
    spending_profile = models.ForeignKey(SpendingProfile, on_delete=models.CASCADE, related_name='evidences',blank=True, null=True)


class Comments(models.Model):
    """Define table for Comments for applications"""
    comment = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(null=True, blank=True, auto_now_add = True)
    application = models.ForeignKey(ApplicationData, on_delete=models.CASCADE, null=True, blank=True)
    budgetProfile = models.ForeignKey(BudgetProfile, on_delete=models.CASCADE, null=True, blank=True)

    # def save(self,*args,**kwargs):
    #     """Method to save date when a new comment is made"""
    #     if self.application_complete :
    #         self.date_of_application = timezone.now()
    #     super(ApplicationData, self).save(*args, **kwargs)
