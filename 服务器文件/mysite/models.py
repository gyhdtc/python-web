from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	user_id = models.CharField(max_length=10,default='')
	user_email = models.EmailField(max_length=30,default='')
	user_password = models.CharField(max_length=20,default='')