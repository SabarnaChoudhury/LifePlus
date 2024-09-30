from rest_framework import routers
from django.urls import path, include
from .views import PatientViewSet, DoctorViewSet, AppointmentViewSet

router = routers.DefaultRouter()
<<<<<<< Updated upstream
router.register(r'patients', PatientViewSet)  # Provides /patients/ and /patients/<id>/
router.register(r'doctors', DoctorViewSet)    # Provides /doctors/ and /doctors/<id>/
=======
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)
>>>>>>> Stashed changes

urlpatterns = [
    path('', include(router.urls)),
]
