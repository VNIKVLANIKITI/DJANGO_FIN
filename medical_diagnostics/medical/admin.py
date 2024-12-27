from django.contrib import admin
from users.models import User
from medical.models import MedicalService, Appointment, Doctor

admin.site.register(User)
admin.site.register(MedicalService)
admin.site.register(Appointment)
admin.site.register(Doctor)
