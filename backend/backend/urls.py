from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import (
    CreateUserView, UserListView, UserDetailView,
    AdministratorListView, AdministratorDetailView,
    EmployeeListView, EmployeeDetailView,
    SalaryListView, SalaryDetailView,
    TripListView, TripDetailView,
    VehicleListView, VehicleDetailView,
    SalaryReportListView, SalaryReportDetailView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/', CreateUserView.as_view(), name='register'),
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    
    path('api/admins/', AdministratorListView.as_view(), name='admin-list'),
    path('api/admins/<int:pk>/', AdministratorDetailView.as_view(), name='admin-detail'),
    
    path('api/employees/', EmployeeListView.as_view(), name='employee-list'),
    path('api/employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    
    path('api/salaries/', SalaryListView.as_view(), name='salary-list'),
    path('api/salaries/<int:pk>/', SalaryDetailView.as_view(), name='salary-detail'),
    
    path('api/trips/', TripListView.as_view(), name='trip-list'),
    path('api/trips/<int:pk>/', TripDetailView.as_view(), name='trip-detail'),
    
    path('api/vehicles/', VehicleListView.as_view(), name='vehicle-list'),
    path('api/vehicles/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    
    path('api/salary-reports/', SalaryReportListView.as_view(), name='salary-report-list'),
    path('api/salary-reports/<int:pk>/', SalaryReportDetailView.as_view(), name='salary-report-detail'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='get_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('api-auth/', include('rest_framework.urls')),
]
