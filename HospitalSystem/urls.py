"""HospitalSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from Hospital import doctorViews, patientViews, views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.root),
    path('index/', views.index),
    path('doctor/login/', doctorViews.login),
    path('doctor/logout/', doctorViews.logout),
    path('doctor/register/', doctorViews.register),
    path('doctor/', doctorViews.index),
    path('doctor/pendingDiagnosis/', doctorViews.pendingDiagnosis),
    path('doctor/pendingDiagnosis/detail', doctorViews.pendingDiagnosisDetail),
    path('doctor/diagnosis/', doctorViews.diagnosis),
    path('doctor/diagnosis/detail', doctorViews.diagnosisDetail),
    path('doctor/info/', doctorViews.info),
    path('doctor/info_edit_description/', doctorViews.info_edit_description),
    path('patient/login/', patientViews.login),
    path('patient/logout/', patientViews.logout),
    path('patient/register/', patientViews.register),
    path('patient/index/', patientViews.index),
    path('patient/info/', patientViews.info),
    path('patient/diagnosis/', patientViews.diagnosis),
    path('patient/diagnosis/detail', patientViews.diagnosisDetail),
    path('patient/makeAppointment', patientViews.makeAppointment),
    path('patient/makeAppointment/detail', patientViews.appointmentDetail),
    path('patient/appointment', patientViews.appointment)
]

urlpatterns += staticfiles_urlpatterns()