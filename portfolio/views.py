from django.shortcuts import render
from django.http import HttpResponse
from .models import HeroSection

# Create your views here.

def portfolio(request):
    herodata = HeroSection.objects.all()
    context  = {
        'hero':herodata
    }
    return render(request, 'index.html',context)

#rafsan
