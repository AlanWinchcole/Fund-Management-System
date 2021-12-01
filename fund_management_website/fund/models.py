from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	userID = models.AutoField(primary_key=True)
	user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
	verified = models.BooleanField(default = False)
	userType = models.CharField(max_length = 50)
	def __str__(self):
		return self.user.username

class ApplicationData(models.Model):
        
        applicationID = models.AutoField(primary_key=True, unique=True)
        organisationName = models.CharField(max_length=200)
        projectTitle = models.CharField(max_length=200)
        CH_OSCR_number = models.CharField(max_length=20, unique=True, blank=True)
        contactName = models.CharField(max_length=200)
        contactEmail = models.EmailField(max_length=254)
        projectDesc = models.CharField(max_length=300)
        userGroupDesc = models.CharField(max_length=300)
        learningOpp = models.CharField(max_length=300)
        keyPartnersWork = models.CharField(max_length=300)
        projImpactClimate = models.CharField(max_length=300)
        projSupportLocBus = models.CharField(max_length=300)
        proContribution = models.CharField(max_length=300)
        feedback = models.CharField(max_length=500)

        def save(self, *args, **kwargs):
                super(ApplicationData, self).save(*args, **kwargs)

        def __str__(self):
                return self.applicationID

        class Meta:
                verbose_name_plural = "ApplicationData"

        
        

        #need to create a class for budget profile and link to app data

#class BudgetProfile(models.Model):
        
        
        
