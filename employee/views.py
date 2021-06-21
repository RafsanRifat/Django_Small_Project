from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def employee(response):
    return HttpResponse('This is employee home page')

def salary(response):
    return HttpResponse('This is the salary page')
