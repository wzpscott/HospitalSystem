from django.contrib import admin
from . import models

admin.site.register(models.Patient)
admin.site.register(models.Doctor)
admin.site.register(models.Appointment)
admin.site.register(models.Diagnosis)
admin.site.register(models.Medicine)
admin.site.register(models.MedicineRequest)
admin.site.register(models.Bill)