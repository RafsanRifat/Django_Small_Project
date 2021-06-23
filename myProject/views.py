from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    text = {
        'name': 'Rafsan',
        'phone': +88011221122,
        'friends': ['Rafsan', 'Adil', 'Abir', 'Tamim', 'Arif',]

    }
    return render(request, 'index.html', text)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

