from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .models import Profile
from .forms import UserForm, ProfileForm

# Create your views here.
class EmployeesList(ListView):
    model = User, Profile
    queryset = Profile.objects.all()
    context_object_name = 'employees'
    template_name = 'Employees/profile_list.html'

class EmployeeProfile(View):
    def get(self, request, pk):
        employee = User.objects.get(pk=pk)
        avatar = employee.profile
        bound_form = ProfileForm(instance=avatar)
        return render(request, 'Employees/employee_profile.html', context={'form': bound_form ,'employee': employee, 'avatar': avatar})

    def post(self, request, pk):
        employee = User.objects.get(pk=pk)
        avatar = employee.profile
        bound_form = ProfileForm(request.POST, request.FILES, instance=avatar)

        if bound_form.is_valid():
            new_avatar = bound_form.save()
            return redirect('/employees/')
        return render(request, 'Employees/employee_profile.html', context={'form': bound_form ,'employee': employee, 'avatar': avatar})

class ProfileUpdate(View):
    def get(self, request, pk):
        profile = User.objects.get(pk=pk)
        bound_form = UserForm(instance=profile)
        return render(request, 'Employees/employee_profile_update.html', context={'form': bound_form, 'profile': profile})

    def post(self, request, pk):
        profile = User.objects.get(pk=pk)
        bound_form = UserForm(request.POST, instance=profile)

        if bound_form.is_valid():
            new_profile = bound_form.save()
            return redirect('/employees/')
        return render(request, 'Employees/employee_profile_update.html', context={'form': bound_form, 'profile': profile})
