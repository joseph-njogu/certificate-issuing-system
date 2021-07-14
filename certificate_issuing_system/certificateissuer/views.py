from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http  import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# from django.contrib.auth import authenticate, login, logout
def index(request):
	return render(request, "index.html")

def studentdetails(request):
    if request.method == 'POST':
        form = studentForm(request.POST)       
        if form.is_valid():
            student = form.save()
            student.save()        
            return redirect('index')
    else:
        form = studentForm()
    return render(request, 'register/register.html', {'form': form})
# class StudentList(ListView):
#     model = student
#  
def studentslist(request):
    model = student
    num_students = student.objects.all().count()
    Students_registered = student.objects.all()
    return render(request,'registered_students.html',context={'num_students': num_students, 'Students_registered': Students_registered
        }
    )
