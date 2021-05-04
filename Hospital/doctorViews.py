from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.DoctorRegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            name = register_form.cleaned_data.get('name')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            gender = register_form.cleaned_data.get('gender')
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
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            ID = login_form.cleaned_data.get('ID')
            password = login_form.cleaned_data.get('password')

            doctor = models.Doctor.objects.filter(id=ID)
            if not doctor:
                message = '用户不存在'
                return render(request, 'doctor/login.html', locals())
            doctor = doctor[0]

            if doctor.password != password:
                message = '密码错误'
                return render(request, 'doctor/login.html', locals())
            request.session['is_login'] = True
            request.session['login_type'] = 'doctor'
            request.session['ID'] = ID
            return redirect('/doctor/index/')
        else:
            return render(request, 'doctor/login.html', locals())

    login_form = forms.LoginForm()
    return render(request, 'doctor/login.html', locals())


def logout(request):
    if request.session.get('is_login', None):
        request.session['is_login'] = False
        request.session['login_type'] = None
        request.session['ID'] = None
        return redirect('/index/')


def index(request):
    return render(request, 'doctor/index.html', locals())


def info(request):
    pass


def pendingDiagnosis(request):
    pass


def diagnosis(request):
    pass


def diagnosisDetail(request):
    pass