from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . import models
from . import forms

from .doctorViews import generate_bill

def entry(request):
    pass


def register(request):
    # if request.session.get('is_login', None):
    #     login_type = request.session['login_type']
    #     return redirect(f'/{login_type}/index/')

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
    # if request.session.get('is_login', None):
    #     login_type = request.session['login_type']
    #     return redirect(f'/{login_type}/index/')
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
            return redirect('/patient/info/')
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
    return render(request, 'patient/index_old.html', locals())


def info(request):
    identity_card_no = request.session['identity_card_no']
    patient = models.Patient.objects.get(identity_card_no=identity_card_no)
    return render(request, 'patient/info.html', {'patient': patient})


def makeAppointment(request):
    patient = models.Patient.objects.get(identity_card_no=request.session['identity_card_no'])
    if request.method == 'POST':
        # 统计已有挂号数，假如超过两个不允许再挂号
        patient = models.Patient.objects.get(identity_card_no=request.session['identity_card_no'])
        num = len(models.Appointment.objects.filter(patient=patient, isActive=True))
        # 待修改
        if num > 100:
            message = '挂号多于两个'
            return render(request, 'patient/makeAppointment.html', locals())

        appointment = models.Appointment()
        appointment.patient = models.Patient.objects.get(identity_card_no=request.session['identity_card_no'])
        appointment.doctor = models.Doctor.objects.get(identity_card_no=request.POST.get('appointment_doctor_id'))
        appointment.appointment_time = request.POST.get('appointment_time')
        appointment.appointment_date = request.POST.get('appointment_date')

        appointment.isActive = True
        appointment.save()
        request.session['appointment_id'] = appointment.id

        return redirect('/patient/makeAppointment/detail')

    departs = [depart[0] for depart in models.Doctor.department_choices]
    departs_ = [depart[1] for depart in models.Doctor.department_choices]
    depart = request.GET.get('depart', departs_[0] if 'depart' not in request.session else request.session['depart'])
    request.session['depart'] = depart
    # print('科室', depart, departs_.index(depart))
    records = models.Doctor.objects.filter(department=departs[departs_.index(depart)])
    num_per_page = 5
    paginator = Paginator(records, num_per_page)
    page = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False
    page_range = paginator.get_elided_page_range(page, on_each_side=3, on_ends=2)
    return render(request, 'patient/makeAppointment.html', locals())


def appointmentDetail(request):
    appointment = models.Appointment.objects.get(id=request.session['appointment_id'])
    return render(request, 'patient/appointmentDetail.html', locals())


def appointment(request):
    identity_card_no = request.session['identity_card_no']
    patient = models.Patient.objects.get(identity_card_no=identity_card_no)
    appointments = models.Appointment.objects.filter(patient=patient)
    num_per_page = 5
    paginator = Paginator(appointments, num_per_page)
    page = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False
    page_range = paginator.get_elided_page_range(page, on_each_side=3, on_ends=2)
    return render(request, 'patient/appointment.html', locals())


def diagnosis(request):
    if request.method == 'POST':
        request.session['diagnosis'] = request.POST.get('diagnosis')
        return redirect('/patient/diagnosis/detail')
    identity_card_no = request.session['identity_card_no']
    patient = models.Patient.objects.get(identity_card_no=identity_card_no)
    diagnosis_records = models.Diagnosis.objects.filter(patient=patient)
    num_per_page = 5
    paginator = Paginator(diagnosis_records, num_per_page)
    page = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False
    page_range = paginator.get_elided_page_range(page, on_each_side=3, on_ends=2)
    return render(request, 'patient/diagnosis.html', locals())


def diagnosisDetail(request):
    record = models.Diagnosis.objects.get(id=request.session['diagnosis'])
    medicines = models.MedicineRequest.objects.filter(diagnosis=record)
    return render(request, 'patient/detail.html', locals())


def bill(request):
    if request.method == 'POST':
        request.session['bill'] = request.POST.get('bill')
        return redirect('/patient/bill/detail')
    identity_card_no = request.session['identity_card_no']
    patient = models.Patient.objects.get(identity_card_no=identity_card_no)
    bills = models.Bill.objects.filter(diagnosis__in=models.Diagnosis.objects.filter(patient=patient))

    num_per_page = 5
    paginator = Paginator(bills, num_per_page)
    page = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False
    page_range = paginator.get_elided_page_range(page, on_each_side=3, on_ends=2)
    return render(request, 'patient/bill.html', locals())


def billDetail(request):
    bill = models.Bill.objects.get(id=request.session['bill'])
    diag = bill.diagnosis
    patient = diag.patient
    bill_detail = generate_bill(diag)
    if request.method == 'POST':
        bill.is_active = False
        bill.save()
        message = '缴费成功'
        return render(request, 'patient/billDetail.html', locals())
    return render(request, 'patient/billDetail.html', locals())


