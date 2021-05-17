from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone

from . import models
from . import forms


def entry(request):
    pass


def register(request):
    if request.session.get('is_login', None):
        login_type = request.session['login_type']
        return redirect(f'/{login_type}/index/')

    if request.method == 'POST':
        register_form = forms.PatientRegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            name = register_form.cleaned_data.get('name')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            # gender = register_form.cleaned_data.get('gender')
            gender = request.POST.get('gender')
            identity_card_no = register_form.cleaned_data.get('identity_card_no')
            # medical_insurance = register_form.cleaned_data.get('medical_insurance')
            medical_insurance = request.POST.get('medical_insurance')
            telephone_no = register_form.cleaned_data.get('telephone_no')
            birth_date = register_form.cleaned_data.get('birth_date')
            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'patient/register.html', locals())
            else:
                same_ic = models.Patient.objects.filter(identity_card_no=identity_card_no)
                if same_ic:
                    message = '身份证号已经注册'
                    return render(request, 'patient/register.html', locals())

                new_patient = models.Patient()
                new_patient.name = name
                new_patient.password = password1
                new_patient.gender = gender
                new_patient.identity_card_no = identity_card_no
                new_patient.medical_insurance = medical_insurance
                new_patient.telephone_no = telephone_no
                new_patient.birth_date = birth_date
                new_patient.save()

                return redirect('/patient/login/')
        else:
            return render(request, 'patient/register.html', locals())
    register_form = forms.PatientRegisterForm()
    return render(request, 'patient/register.html', locals())


def login(request):
    if request.session.get('is_login', None):
        login_type = request.session['login_type']
        return redirect(f'/{login_type}/index/')
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            identity_card_no = login_form.cleaned_data.get('identity_card_no')
            password = login_form.cleaned_data.get('password')
            patient = models.Patient.objects.filter(identity_card_no=identity_card_no)
            if not patient:
                message = '用户不存在'
                return render(request, 'patient/login.html', locals())
            patient = patient[0]

            if patient.password != password:
                message = '密码错误'
                return render(request, 'patient/login.html', locals())
            request.session['is_login'] = True
            request.session['login_type'] = 'patient'
            request.session['identity_card_no'] = identity_card_no
            return redirect('/patient/index/')
        else:
            return render(request, 'patient/login.html', locals())

    login_form = forms.LoginForm()
    return render(request, 'patient/login.html', locals())


def logout(request):
    if request.session.get('is_login', None):
        request.session['is_login'] = False
        request.session['login_type'] = None
        request.session['ID'] = None
        return redirect('/Hospital/')


def index(request):
    return render(request, 'patient/index.html', locals())


def info(request):
    identity_card_no = request.session['identity_card_no']
    patient = models.Patient.objects.get(identity_card_no=identity_card_no)
    return render(request, 'patient/info.html', {'patient': patient})


def makeAppointment(request):
    records = models.Doctor.objects.all()
    if request.method == 'POST':
        appointment = models.Appointment()
        appointment.patient = models.Patient.objects.get(identity_card_no=request.session['identity_card_no'])
        appointment.doctor = models.Doctor.objects.get(identity_card_no=request.POST.get('appointment_doctor_id'))
        appointment.appointment_time = request.POST.get('appointment_time')
        appointment.appointment_date = request.POST.get('appointment_date')
        appointment.isActive = True
        appointment.save()
        request.session['appointment_id'] = appointment.id
        return redirect('/patient/makeAppointment/detail')
    return render(request, 'patient/makeAppointment.html', locals())


def appointmentDetail(request):
    appointment = models.Appointment.objects.get(id=request.session['appointment_id'])
    return render(request, 'patient/appointmentDetail.html', locals())


def appointment(request):
    identity_card_no = request.session['identity_card_no']
    patient = models.Patient.objects.get(identity_card_no=identity_card_no)
    appointments = models.Appointment.objects.filter(patient=patient)
    return render(request, 'patient/appointment.html', locals())


def diagnosis(request):
    identity_card_no = request.session['identity_card_no']
    patient = models.Patient.objects.get(identity_card_no=identity_card_no)
    diagnosis_records = models.Diagnosis.objects.filter(patient=patient)
    if request.method == 'POST':
        request.session['diagnosis'] = request.POST.get('diagnosis')
        return redirect('/patient/diagnosis/detail')
    return render(request, 'patient/diagnosis.html', locals())


def diagnosisDetail(request):
    record = models.Diagnosis.objects.get(id=request.session['diagnosis'])
    medicines = models.MedicineRequest.objects.filter(diagnosis=record)
    return render(request, 'patient/detail.html', locals())


def bill(request):
    pass


def billDetail(request):
    pass


