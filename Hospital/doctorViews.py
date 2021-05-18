from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms


def register(request):
    if request.session.get('is_login', None):
        login_type = request.session['login_type']
        return redirect(f'/{login_type}/index')

    if request.method == 'POST':
        register_form = forms.DoctorRegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            name = register_form.cleaned_data.get('name')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            # gender = register_form.cleaned_data.get('gender')
            gender = request.POST.get('gender')
            identity_card_no = register_form.cleaned_data.get('identity_card_no')
            department = register_form.cleaned_data.get('department')
            title = register_form.cleaned_data.get('title')
            description = register_form.cleaned_data.get('description')
            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'doctor/register.html', locals())
            else:
                same_ic = models.Doctor.objects.filter(identity_card_no=identity_card_no)
                if same_ic:
                    message = '身份证号已经注册'
                    return render(request, 'doctor/register.html', locals())

                new_doctor = models.Doctor()
                new_doctor.name = name
                new_doctor.password = password1
                new_doctor.gender = gender
                new_doctor.identity_card_no = identity_card_no
                new_doctor.department = department
                new_doctor.title = title
                new_doctor.description = description
                new_doctor.save()

                return redirect('/doctor/login/')
        else:
            return render(request, 'doctor/register.html', locals())
    register_form = forms.DoctorRegisterForm()
    return render(request, 'doctor/register.html', locals())


def login(request):
    if request.session.get('is_login', None):
        login_type = request.session['login_type']
        return redirect(f'/{login_type}/index')
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            identity_card_no = login_form.cleaned_data.get('identity_card_no')
            password = login_form.cleaned_data.get('password')

            doctor = models.Doctor.objects.filter(identity_card_no=identity_card_no)
            if not doctor:
                message = '用户不存在'
                return render(request, 'doctor/login.html', locals())
            doctor = doctor[0]

            if doctor.password != password:
                message = '密码错误'
                return render(request, 'doctor/login.html', locals())
            request.session['is_login'] = True
            request.session['login_type'] = 'doctor'
            request.session['identity_card_no'] = identity_card_no
            return redirect('/doctor/index')
        else:
            return render(request, 'doctor/login.html', locals())

    login_form = forms.LoginForm()
    return render(request, 'doctor/login.html', locals())


def logout(request):
    if request.session.get('is_login', None):
        request.session['is_login'] = False
        request.session['login_type'] = None
        request.session['ID'] = None
        return redirect('/Hospital/')


def index(request):
    return render(request, 'doctor/index.html', locals())


def info(request):
    identity_card_no = request.session['identity_card_no']
    doctor = models.Doctor.objects.get(identity_card_no=identity_card_no)
    return render(request, 'doctor/info.html', {'doctor': doctor})


def info_edit_description(request):
    identity_card_no = request.session['identity_card_no']
    doctor = models.Doctor.objects.get(identity_card_no=identity_card_no)
    if request.method == 'POST':
        description_form = forms.DescriptionModifyForm(request.POST)
        if description_form.is_valid():
            doctor.description = description_form.cleaned_data.get('description')
            doctor.save()
            message = '修改成功!'
        else:
            message = '输入不合法!'
        return redirect('/doctor/info/')
    else:
        description_form = forms.DescriptionModifyForm(initial={'description': doctor.description})
        return render(request, 'doctor/info_edit_description.html', locals())


def pendingDiagnosis(request):
    identity_card_no = request.session['identity_card_no']
    doctor = models.Doctor.objects.get(identity_card_no=identity_card_no)
    appointment_records = models.Appointment.objects.filter(doctor=doctor, isActive=True)
    if request.method == 'POST':
        request.session['appointment_id'] = request.POST.get('appointment')
        return redirect('/doctor/pendingDiagnosis/detail')
    return render(request, 'doctor/pending.html', locals())


def pendingDiagnosisDetail(request):
    identity_card_no = request.session['identity_card_no']
    doctor = models.Doctor.objects.get(identity_card_no=identity_card_no)

    appointment_id = request.session['appointment_id']
    appointment = models.Appointment.objects.get(id=appointment_id)

    if models.Diagnosis.objects.filter(appointment=appointment):
        diag = models.Diagnosis.objects.filter(appointment=appointment)[0]
    else:
        diag = models.Diagnosis()
        diag.doctor = doctor
        diag.patient = appointment.patient
        diag.appointment = appointment
        diag.save()

    initial_formset = []
    for req in models.MedicineRequest.objects.filter(diagnosis=diag):
        initial_formset.append({'medicine': req.medicine, 'amount': req.amount})

    if request.method == 'POST':
        detail_form = forms.DiagnosisDetailForm(request.POST)
        medicine_formset = forms.DiagnosisFormset(request.POST)

        if detail_form.is_valid() and medicine_formset.is_valid():
            detail = detail_form.cleaned_data.get('detail')
            diag.detail = detail
            diag.save()

            n = int(request.POST['form-TOTAL_FORMS'])
            data = medicine_formset.cleaned_data

            for i in range(n):
                medicine_name = data[i].get('medicine')
                medicine = models.Medicine.objects.get(name=medicine_name)
                amount = data[i].get('amount')
                medicine_request = models.MedicineRequest.objects.filter(medicine=medicine)
                if medicine_request:
                    medicine_request = medicine_request[0]
                    medicine_request.amount = amount
                else:
                    medicine_request = models.MedicineRequest()
                    medicine_request.diagnosis = diag
                    medicine_request.medicine = medicine
                    medicine_request.amount = amount
                medicine_request.save()

            detail_form = forms.DiagnosisDetailForm(initial={'detail': diag.detail})
            medicine_formset = forms.DiagnosisFormset(initial=initial_formset)

            return render(request, 'doctor/pending_detail.html', locals())

    else:
        detail_form = forms.DiagnosisDetailForm(initial={'detail':diag.detail})
        medicine_formset = forms.DiagnosisFormset(initial=initial_formset)
    return render(request, 'doctor/pending_detail.html', locals())


def diagnosis(request):
    identity_card_no = request.session['identity_card_no']
    doctor = models.Doctor.objects.get(identity_card_no=identity_card_no)
    diagnosis_records = models.Diagnosis.objects.filter(doctor=doctor)
    if request.method == 'POST':
        request.session['diagnosis'] = request.POST.get('diagnosis')
        return redirect('/doctor/diagnosis/detail')
    return render(request, 'doctor/diagnosis.html', locals())


def diagnosisDetail(request):
    record = models.Diagnosis.objects.get(id=request.session['diagnosis'])
    medicines = models.MedicineRequest.objects.filter(diagnosis=record)

    return render(request, 'doctor/detail.html', locals())

