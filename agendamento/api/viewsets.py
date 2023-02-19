# app
from agendamento.models import Services, Employee, Client, Schedule, Attendant
from agendamento.api.serializers import (
    ServicesSerializer,
    EmployeeSerializer,
    ClientSerializer,
    ScheduleSerializer,
    AttendantSerializer,
    AttendantesListTodaySerializer
)
from agendamento.api.serializers import MyTokenObtainPairSerializer

# rest_framework
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView


class ServicesViewsets(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class EmployeeViewsets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AttendantesListTodayViewsets(viewsets.ModelViewSet):
    queryset = Attendant.objects.filter_today()
    serializer_class = AttendantesListTodaySerializer


class AttendantViewsets(viewsets.ModelViewSet):
    queryset = Attendant.objects.all()
    serializer_class = AttendantSerializer


class ClientViewsets(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ScheduleViewsets(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer