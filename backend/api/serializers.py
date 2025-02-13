from rest_framework import serializers
from .models import User, Administrator, Employee, Salary, Trip, Vehicle, SalaryReport

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'cellphone_no', 'email', 'philhealth_no', 'pag_ibig_no', 'sss_no']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

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
        fields = ['employee_id', 'user', 'trip', 'salary', 'employee_type']

# Salary Serializer
class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ['salary_id', 'trip', 'deductions', 'bonuses', 'base_salary', 'multipliers', 'overtime', 'additionals']

# Trip Serializer
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['trip_id', 'vehicle', 'destination', 'distance_traveled', 'num_of_drops', 'curr_drops', 'client_info', 'start_date', 'end_date']

# Vehicle Serializer
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['vehicle_id', 'vehicle_type']

# Salary Report Serializer
class SalaryReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryReport
        fields = ['salary_report_id', 'employee', 'salary']
