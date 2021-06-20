from django.http import HttpResponse



def home(request):
    return HttpResponse('This is a home page')

def about(request):
    return HttpResponse('This is a about page')

def contact(request):
    return HttpResponse('This is a contact page')

def rafsan(request):
    return HttpResponse('This is the inner page')
