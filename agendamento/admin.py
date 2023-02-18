from django.contrib import admin

from .models import Services, Employee, Client, Schedule

# Register your models here.


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "active"]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["user", "name", "position", "is_manager"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["phone", "address"]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = [
        "client",
        "employee",
        "service",
        "date",
        "status",
        "payment",
    ]
