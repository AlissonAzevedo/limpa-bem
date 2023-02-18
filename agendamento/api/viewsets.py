# app
from agendamento.models import Services, Employee, Client, Schedule
from agendamento.api.serializers import (
    ServicesSerializer,
    EmployeeSerializer,
    ClientSerializer,
    ScheduleSerializer,
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


class ClientViewsets(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ScheduleViewsets(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer