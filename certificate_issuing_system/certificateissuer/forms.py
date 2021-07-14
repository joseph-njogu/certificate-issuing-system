from django import forms
from .models import *
# from django.contrib.auth.forms import AuthenticationForm

class studentForm(forms.ModelForm):
	firstname=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Name'}))
	lastname=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Name'}))
	country=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Name'}))
	city=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Name'}))
	marital_status=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Name'}))
	gender=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Your Name'}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Enter Email Address'}))
	phonenumber=forms.CharField(widget=forms.TextInput(attrs={'size':13,'placeholder':'Enter your phone number'}))
	Idno_or_passport=forms.IntegerField(widget=forms.NumberInput(attrs={'size':8, 'placeholder':'Enter your ID or passport number'}))
	zipcode=forms.IntegerField(widget=forms.NumberInput(attrs={'size':5,'placeholder':'Enter zip code'}))
	# profile_pic = forms.ImageField(label = 'Profile Pic')
	date_of_birth=forms.DateTimeField(widget=forms.DateInput(attrs={'placeholder':'Date of Birth'}))
	course=forms.CharField(widget=forms.TextInput(attrs={'size':30,'placeholder':'Course Applying'}))

	class Meta:
		model = student
		fields = ('firstname','lastname','email','phonenumber','country','city','marital_status','gender','zipcode','Idno_or_passport','course')
