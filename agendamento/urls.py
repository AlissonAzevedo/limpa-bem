# rest_framework
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

# app
from .api.viewsets import (
    ServicesViewsets,
    EmployeeViewsets,
    ClientViewsets,
    ScheduleViewsets,
)


router = DefaultRouter()

router.register(r"services", ServicesViewsets)
router.register(r"employee", EmployeeViewsets)
router.register(r"client", ClientViewsets)
router.register(r"schedule", ScheduleViewsets)

urlpatterns = router.urls
