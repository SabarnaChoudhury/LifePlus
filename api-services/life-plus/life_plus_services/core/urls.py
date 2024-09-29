from rest_framework import routers
from django.urls import path, include
from .views import PatientViewSet, DoctorViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)  # Provides /patients/ and /patients/<id>/
router.register(r'doctors', DoctorViewSet)    # Provides /doctors/ and /doctors/<id>/

urlpatterns = [
    path('', include(router.urls)),
]
