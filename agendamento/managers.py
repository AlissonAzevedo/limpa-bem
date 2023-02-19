from datetime import date
from django.db import models


class EmployeeQueryset(models.QuerySet):
    def filter_helpers(self):
        return self.filter(
            position="helper",
        )


class AttendantQueryset(models.QuerySet):
    def filter_today(self):
        today = date.today()
        return self.filter(schedule__date__date=today)
