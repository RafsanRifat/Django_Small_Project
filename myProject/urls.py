
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls'), name='home'),
    # path('', views.home)
    # path('about/', views.about, name= 'about')

]
