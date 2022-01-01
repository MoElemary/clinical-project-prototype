from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
# Create your models here.


class Patient(models.Model):
    Id = models.IntegerField(primary_key=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Address = models.CharField(max_length=150)
    Phone_number = models.IntegerField(max_length=15)
    Contact_relatives = models.CharField(max_length=200)
    Assigned_doctor = models.CharField(max_length=200, default='')
    Assigned_room = models.IntegerField(max_length=5, default='0')
    Medical_record = models.URLField("Click here for medical record")
    X_ray_pictures = models.ImageField(null=True, blank=True, upload_to="images/")


class Doctor(models.Model):
    Id = models.BigAutoField(primary_key=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Address = models.CharField(max_length=150)
    Phone_number = models.IntegerField(max_length=15)
    Assigned_Patients = models.CharField(max_length=150)
    Assigned_rooms = models.IntegerField(max_length=5)



class Admission(models.Model):
    Id = models.BigAutoField(primary_key = True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Salary = models.IntegerField()


class NursingTeam(models.Model):
    group_number = models.IntegerField(primary_key=True)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Assigned_patients_Nurses = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Supervisor = models.CharField(max_length=50)
    Assigned_Rooms = models.IntegerField()
    Assigned_Patients = models.CharField(max_length=50)
    shift_time = models.IntegerField()

    def __int__(self):
        return self.group_number


class Nurses(models.Model):
    Id = models.BigAutoField(primary_key=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    # Email = models.CharField(max_length=100)
    # Password = models.CharField(max_length=100)
    group_number_nurses = models.ForeignKey(NursingTeam, on_delete=models.CASCADE)
    #group_number = models.IntegerField()
    Supervisor = models.CharField(max_length=50)
    Assigned_Rooms = models.IntegerField()
    Assigned_Patients = models.CharField(max_length=50)
    Salary = models.IntegerField(max_length=50, null=True)

    def __str__(self):
        return self.First_name + "  " + self.Last_name


class NursingSupervision(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Full_name = models.CharField(max_length=100)
    Responsible_group_number = models.ForeignKey(NursingTeam, on_delete=models.CASCADE)
    Salary = models.IntegerField(max_length=50, null=True)

    def __str__(self):
        return self.Full_name

    # class NursingTeam(models.Model):
#     Id = models.BigAutoField(primary_key=True)
#     Email = models.CharField(max_length=100)
#     group_number = models.IntegerField()
#     Supervisor = models.CharField(max_length=50)
#     Assigned_Rooms = models.IntegerField()
#     Assigned_Patients = models.CharField(max_length=50)


    # def __str__(self):
    #     return self.First_name


class CleaningTeam(models.Model):
    group_number = models.IntegerField(primary_key=True)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    Supervisor = models.CharField(max_length=50)
    Assigned_Rooms = models.IntegerField()
    shift_time = models.IntegerField(default='0')


class CleaningIndividuals(models.Model):
    Id = models.IntegerField(primary_key=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    group_number = models.ForeignKey(CleaningTeam, on_delete=models.CASCADE)
    Supervisor = models.CharField(max_length=50)
    Assigned_Rooms = models.IntegerField()
    Salary = models.IntegerField(max_length=50, null=True)

    def __str__(self):
        return self.First_name + "  " + self.Last_name
        #return self.Id


class CleaningSupervision(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Full_name = models.CharField(max_length=100)
    Responsible_group_number = models.ForeignKey(CleaningTeam, on_delete=models.CASCADE)
    Salary = models.IntegerField(max_length=50, null=True)

    def __str__(self):
        return self.Full_name
#
# class CleaningTeam(models.Model):
#     Id = models.BigAutoField(primary_key=True)
#     First_name = models.CharField(max_length=50)
#     Last_name = models.CharField(max_length=50)
#     Email = models.CharField(max_length=100)
#     Password = models.CharField(max_length=100)
#     group_number = models.IntegerField()
#     Supervisor = models.CharField(max_length=50)
#     Assigned_Room = models.IntegerField()
