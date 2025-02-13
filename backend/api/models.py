from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):
    cellphone_no = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    philhealth_no = models.CharField(max_length=20, unique=True)
    pag_ibig_no = models.CharField(max_length=20, unique=True)
    sss_no = models.CharField(max_length=20, unique=True)
    groups = models.ManyToManyField(
        'auth.Group', related_name='api_users', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='api_users_permissions', blank=True
    )

# Administrator Model
class Administrator(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary_report = models.ForeignKey('SalaryReport', on_delete=models.CASCADE)

# Employee Model
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    salary = models.ForeignKey('Salary', on_delete=models.CASCADE)
    employee_type = models.CharField(max_length=50)

# Salary Model
class Salary(models.Model):
    salary_id = models.AutoField(primary_key=True)
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    deductions = models.DecimalField(max_digits=10, decimal_places=2)
    bonuses = models.DecimalField(max_digits=10, decimal_places=2)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    multipliers = models.DecimalField(max_digits=5, decimal_places=2)
    overtime = models.DecimalField(max_digits=10, decimal_places=2)
    additionals = models.DecimalField(max_digits=10, decimal_places=2)

# Trip Model
class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE)
    destination = models.CharField(max_length=255)
    distance_traveled = models.DecimalField(max_digits=10, decimal_places=2)
    num_of_drops = models.IntegerField()
    curr_drops = models.IntegerField()
    client_info = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

# Vehicle Model
class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    vehicle_type = models.CharField(max_length=50)

# Salary Report Model
class SalaryReport(models.Model):
    salary_report_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
