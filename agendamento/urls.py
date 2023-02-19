# rest_framework
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

# app
from .api.viewsets import (
    ServicesViewsets,
    EmployeeViewsets,
    AttendantesListTodayViewsets,
    ClientViewsets,
    ScheduleViewsets,
    AttendantViewsets
)


router = DefaultRouter()

router.register(r"services", ServicesViewsets)
router.register(r"employee", EmployeeViewsets)
router.register(r"attendants-list-today", AttendantesListTodayViewsets, "list-today")
router.register(r"client", ClientViewsets)
router.register(r"schedule", ScheduleViewsets)
router.register(r"attendant", AttendantViewsets)

urlpatterns = router.urls
