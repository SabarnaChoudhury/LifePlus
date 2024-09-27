from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Hospital Management API")




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('patients.urls')),
    path('', home),# This includes your patient list endpoint
]
