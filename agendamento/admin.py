from django.contrib import admin

from .models import Services, Employee, Client, Schedule, Attendant

# Register your models here.


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "active"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "position", "is_manager"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "address"]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = [
        "client",
        "helper",
        "service",
        "date",
        "status",
        "payment",
        "service_price",
        "service_value",
    ]

@admin.register(Attendant)
class AttendantAdmin(admin.ModelAdmin):
    list_display = ["name", "user", "schedule_list"]
