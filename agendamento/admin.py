from django.contrib import admin

from .models import Services, Employee, Client, Schedule, Attendant

# Register your models here.


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "active"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "name", "position", "is_manager"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "phone", "address"]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
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
    list_display = ["id", "name", "user", "schedule_list"]
