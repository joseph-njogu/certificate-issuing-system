from django.db import models

# Create your models here.
class student(models.Model):
	# profile_pic = models.ImageField(upload_to = "profile/",null=True)
	firstname = models.CharField(max_length =30)
	lastname = models.CharField(max_length =30)
	Idno_or_passport = models.IntegerField(8)
	email = models.EmailField(max_length =50, unique=True)
	phonenumber = models.CharField(max_length=13)
	country = models.CharField(max_length =30)
	city = models.CharField(max_length =30)
	zipcode = models.IntegerField(5)
	course = models.CharField(max_length =30)
	date_of_birt = models.DateTimeField(auto_now= True)
	marital_status = models.CharField(max_length =30)
	gender = models.CharField(max_length =30)
	USERNAME_FIELD='email'
	digital_signature = models.CharField(max_length=500)
	REQUIRED_FIELDS=['*']
	objects = models.Manager()
