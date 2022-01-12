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
        organisationName = models.CharField(max_length=200, null = True, blank=True)
        projectTitle = models.CharField(max_length=200, null = True, blank=True)
        CH_OSCR_number = models.CharField(max_length=20, unique=True, blank=True, null = True,)
        # Could take these out as they are basically users.
        contactName = models.CharField(max_length=200, null = True, blank=True)
        contactEmail = models.EmailField(max_length=254, null = True, blank=True)

        projectDesc = models.TextField(max_length=300, null = True, blank=True)
        userGroupDesc = models.TextField(max_length=300, null = True, blank=True)
        learningOpp = models.TextField(max_length=300, null = True, blank=True)
        keyPartnersWork = models.TextField(max_length=300, null = True, blank=True)
        projImpactClimate = models.TextField(max_length=300, null = True, blank=True)
        projSupportLocBus = models.TextField(max_length=300, null = True, blank=True)
        proContribution = models.TextField(max_length=300, null = True, blank=True)

        length = models.IntegerField(null=True, blank=True, db_column="Length of the Project")
        totalBudget =models.FloatField(null=True, blank=True, db_column="Total Budget for the Project")

        def save(self, *args, **kwargs):
                super(ApplicationData, self).save(*args, **kwargs)

        def __str__(self):
                return self.projectTitle

        class Meta:
                verbose_name_plural = "ApplicationData"

# Completed Application
class Project(models.Model):
    pass




        
        
        
