from django.shortcuts import render
from .models import Nurses
from django.http import HttpResponse
#since we don't need simple http response we may delete it from the import library

# Create your views here.

# Nurses_i = [
#
#     {
#         'Id': '',
#         'First_name': '',
#         'Last_name': '',
#         'Email': '',
#         'Password': '',
#         'group_number': '',
#         'Supervisor': '',
#         'Assigned_Room': '',
#         'Assigned_Patient': ''
#     },
#     {
#         'Id': '',
#         'First_name': '',
#         'Last_name': '',
#         'Email': '',
#         'Password': '',
#         'group_number': '',
#         'Supervisor': '',
#         'Assigned_Room': '',
#         'Assigned_Patient': ''
#     }
#
#
# ]


def homepage(user_response):
    contex = {
        'Nurse':Nurses.objects.all()

    }
    return render(user_response, 'registration_system/home.html', contex)


def about_us(user_response):
    return render(user_response, 'registration_system/about.html',{'title':'about'})


# def Admin_view(user_response):
#     return render(user_response, 'registration_system/Admin.html')
