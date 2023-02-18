# django
from django.contrib.auth.models import User

# app
from agendamento.models import Services, Employee, Client, Schedule

# rest_framework
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {'password': {'write_only': True}}


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ["name", "price", "active"]


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ["user", "name", "position", "is_manager", "get_position"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "name",
            "street",
            "number",
            "district",
            "city",
            "state",
            "zipcode",
            "phone",
        ]


class ScheduleSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Schedule
        fields = ["client", "employee", "service", "date", "status", "payment"]
