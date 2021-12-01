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
        
        applicationID = models.CharField(max_length=200, null = True, blank=True)
        organisationName = models.CharField(max_length=200, null = True, blank=True)
        projectTitle = models.CharField(max_length=200, null = True, blank=True)
        CH_OSCR_number = models.CharField(max_length=20, unique=True, blank=True, null = True,)
        contactName = models.CharField(max_length=200, null = True, blank=True)
        contactEmail = models.EmailField(max_length=254, null = True, blank=True)
        projectDesc = models.CharField(max_length=300, null = True, blank=True)
        userGroupDesc = models.CharField(max_length=300, null = True, blank=True)
        learningOpp = models.CharField(max_length=300, null = True, blank=True)
        keyPartnersWork = models.CharField(max_length=300, null = True, blank=True)
        projImpactClimate = models.CharField(max_length=300, null = True, blank=True)
        projSupportLocBus = models.CharField(max_length=300, null = True, blank=True)
        proContribution = models.CharField(max_length=300, null = True, blank=True)
        feedback = models.CharField(max_length=500, null = True, blank=True)

        def save(self, *args, **kwargs):
                super(ApplicationData, self).save(*args, **kwargs)

        def __str__(self):
                return self.applicationID

        class Meta:
                verbose_name_plural = "ApplicationData"

        
        

        #need to create a class for budget profile and link to app data

#class BudgetProfile(models.Model):
        
        
        
