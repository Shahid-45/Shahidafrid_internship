from unicodedata import name
from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('addEmployee', views.addEmployee, name="addEmployee"),
    path('editEmployee/<int:id>',views.editEmployee, name="editEmployee"),
    path('deleteEmployee/<int:id>',views.deleteEmployee, name="deleteEmployee"),
    path('crud',views.index, name="crud"),
    path('qrgen',views.qr, name="qr"),
    path('captcha',views.cap, name="cap")
    ]

