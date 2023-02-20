# app
from agendamento.models import Services, Employee, Client, Schedule, Attendant
from agendamento.api.serializers import (
    ServicesSerializer,
    EmployeeSerializer,
    ClientSerializer,
    ScheduleSerializer,
    AttendantSerializer,
    AttendantesListTodaySerializer,
)
from agendamento.api.serializers import MyTokenObtainPairSerializer

# rest_framework
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.views import TokenObtainPairView


class ServicesViewsets(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    # permission_classes = [permissions.IsAuthenticated]


class EmployeeViewsets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AttendantesListTodayViewsets(viewsets.ModelViewSet):
    queryset = Attendant.objects.filter_today().distinct()
    serializer_class = AttendantesListTodaySerializer
    # permission_classes = [permissions.IsAuthenticated]


class AttendantViewsets(viewsets.ModelViewSet):
    queryset = Attendant.objects.all()
    serializer_class = AttendantSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ClientViewsets(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ScheduleViewsets(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
