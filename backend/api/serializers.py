from rest_framework import serializers
from .models import User, Administrator, Employee, Salary, Trip, Vehicle, SalaryReport

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

# Administrator Serializer
class AdministratorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Administrator
        fields = ['admin_id', 'user', 'salary_report']

# Employee Serializer
class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = ['employee_id', 'user']

# Salary Serializer
class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'

# Trip Serializer
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

# Vehicle Serializer
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

# Salary Report Serializer
class SalaryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryReport
        fields = '__all__'
