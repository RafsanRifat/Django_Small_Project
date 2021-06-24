from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect



def home(request):
    return render(request, 'index.html')

# def about(request):
#     return render(request, 'index.html')

def about(request):
    return HttpResponseRedirect(request.about)




