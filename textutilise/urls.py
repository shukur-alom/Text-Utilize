from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='Index'),
    path('analyze/', views.analyze, name='rempun'),
    path('about/', views.about, name='about'),
    path('con_us/', views.cont, name='Con_us'),
    
]
