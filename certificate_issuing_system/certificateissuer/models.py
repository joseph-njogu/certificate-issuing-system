from django.db import models
from certificate_issuing_system.settings import *
#use this to generate our custom digital signature
from django.contrib.auth.hashers import make_password
# Create your models here.
class student(models.Model):
	# profile_pic = models.ImageField(upload_to = "profile/",null=True)
	firstname = models.CharField(max_length =30)
	lastname = models.CharField(max_length =30)
	Idno_or_passport = models.IntegerField()
	email = models.EmailField(max_length =50, unique=True)
	phonenumber = models.CharField(max_length=13)
	country = models.CharField(max_length =30)
	city = models.CharField(max_length =30)
	zipcode = models.IntegerField()
	course = models.CharField(max_length =30)
	date_of_birt = models.DateTimeField(auto_now= True)
	marital_status = models.CharField(max_length =30)
	gender = models.CharField(max_length =30)
	USERNAME_FIELD='email'
	digital_signature = models.CharField(max_length=500)

	# def save(self, **kwargs):
	# 	salt = "C8E7279CD035B23FCB9C0F1F954DFF5B3"
	# 	# salt = bytes(SECURE_STRING_SALT, encoding="raw_unicode_escape") 
	# 	digital_signature = make_password(self.email, salt)
	# 	save(**kwargs)

	REQUIRED_FIELDS=['*']
	objects = models.Manager()
