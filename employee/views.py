from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def employee(request):
    return render(request, 'employee/profile.html')

def salary(request):
    return HttpResponse('This is the salary page')
