from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userProfile(models.Model):
	user = models.OneToOneField(User, related_name="useract")
	usrType = models.CharField(max_length=2, choices=(('ST','Student'),('PR','Partner'),), default='ST')

'''
class posts(models.Model):
	user = models.ForeignKey(User, related_name="post_author")
	datetime = 
	title = 
	body = 

'''