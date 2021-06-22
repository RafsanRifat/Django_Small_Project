from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request, 'employee/profile.html')

def employee(request):
    return render(request, 'employee.html')
