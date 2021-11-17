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