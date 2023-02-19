# django
from django.contrib.auth.models import User

# app
from agendamento.models import Services, Employee, Client, Schedule, Attendant

# rest_framework
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ["id", "name", "price", "active"]


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ["id", "user", "name", "position", "is_manager", "get_position"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            "id",
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
        fields = [
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

    def create(self, validated_data):
        client_data = validated_data.pop("client")
        client = Client.objects.create(**client_data)
        schedule = Schedule.objects.create(client=client, **validated_data)
        return schedule


class AttendantSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    schedule = ScheduleSerializer(
        read_only=True, required=False, allow_null=True, many=True
    )

    class Meta:
        model = Attendant
        fields = ["id", "name", "user", "schedule"]


class AttendantesListTodaySerializer(serializers.ModelSerializer):
    user = UserSerializer()
    schedule = ScheduleSerializer(
        read_only=True, required=False, allow_null=True, many=True
    )

    class Meta:
        model = Attendant
        fields = ["id", "name", "user", "schedule"]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        try:
            employee = Employee.objects.get(user=self.user)
            data["employee_id"] = employee.id
        except Exception as e:
            employee = Employee.objects.create(user=self.user, name=self.user.username)
            data["employee_id"] = employee.id

        return data
