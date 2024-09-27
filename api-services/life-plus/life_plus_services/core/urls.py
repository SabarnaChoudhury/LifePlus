from rest_framework import routers
from django.urls import path, include
from .views import PatientViewSet, DoctorViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
