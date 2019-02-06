from rest_framework import routers
from accounts import api_views as myapp_views

router = routers.DefaultRouter()

router.register(r'servicios',myapp_views.ServiceViewset)
router.register(r'cita',myapp_views.AppointmentViewset)