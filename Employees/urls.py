from django.urls import path
from .views import *

urlpatterns = [
    path('', EmployeesList.as_view(), name='profile_list_url'),
    path('profile/<int:pk>/', EmployeeProfile.as_view(), name='employee_profile_url'),
    path('profile/<int:pk>/update/', ProfileUpdate.as_view(), name='profile_update_url'),
]
