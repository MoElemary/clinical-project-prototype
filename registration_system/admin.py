from django.contrib import admin

# Register your models here.
from .models import Nurses, NursingTeam, NursingSupervision, CleaningIndividuals, CleaningTeam, CleaningSupervision
from .models import Admission, Patient, Doctor
admin.site.register(Nurses)
admin.site.register(NursingTeam)
admin.site.register(NursingSupervision)
admin.site.register(CleaningIndividuals)
admin.site.register(CleaningTeam)
admin.site.register(CleaningSupervision)
admin.site.register(Admission)
admin.site.register(Patient)
admin.site.register(Doctor)
