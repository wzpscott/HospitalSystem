from django import forms
from django.forms import formset_factory,ModelForm
from . import models


class LoginForm(forms.Form):
    identity_card_no = forms.CharField(label="身份证号", max_length=128)
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)


class PatientRegisterForm(forms.Form):
    gender_choices = (
        ('male', "男"),
        ('female', "女"),
    )
    name = forms.CharField(max_length=10)  # 姓名
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput)  # 密码
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput)
    gender = forms.CharField(max_length=32, widget=forms.Select(choices=gender_choices))  # 性别
    identity_card_no = forms.CharField(max_length=32)  # 身份证号
    medical_insurance = forms.BooleanField()  # 是否有医保
    telephone_no = forms.CharField(max_length=32)  # 电话号码
    birth_date = forms.DateField(label='日期', widget=forms.DateInput(attrs={'type':'date'}))  # 出生日期

class DoctorRegisterForm(forms.Form):
    gender_choices = (
        ('male', "男"),
        ('female', "女"),
    )
    department_choices = (
        ('Department of Internal Medicine', '内科'),
        ('Department of Surgery', '外科'),
        ('Department of Pediatrics', '儿科'),
        ('Department of Obstetrics and Gynecology', '妇产科'),
        ('Department of Traditional Chinese Medicine', '中医科'),
        ('Department of Dermatology', '皮肤科'),
        ('Department of Oral Medicine', '口腔科')
    )
    title_choices = (
        ('director physician', '主任医师'),
        ('assistant director physician', '副主任医师'),
        ('physician', '医师')
    )
    name = forms.CharField(max_length=10)  # 姓名
    password1 = forms.CharField(max_length=32, widget=forms.PasswordInput)  # 密码
    password2 = forms.CharField(max_length=32, widget=forms.PasswordInput)
    gender = forms.CharField(max_length=32, widget=forms.Select(choices=gender_choices))  # 性别
    identity_card_no = forms.CharField(max_length=32)  # 身份证号

    department = forms.CharField(max_length=64, widget=forms.Select(choices=department_choices))  # 科室
    title = forms.CharField(max_length=64, widget=forms.Select(choices=title_choices))  # 职称
    description = forms.CharField(max_length=500, widget=forms.Textarea, required=False)  # 简介


class DescriptionModifyForm(forms.Form):
    description = forms.CharField(max_length=500, widget=forms.Textarea)


class DiagnosisDetailForm(forms.Form):
    detail = forms.CharField(max_length=500, widget=forms.Textarea)


class DiagnosisMedicineForm(forms.Form):
    medicine_choices = []
    for medicine in models.Medicine.objects.all():
        medicine_choices.append((medicine, medicine))
    medicine_choices = tuple(medicine_choices)
    medicine = forms.ChoiceField(choices=medicine_choices)
    amount = forms.IntegerField()


DiagnosisFormset = formset_factory(DiagnosisMedicineForm, extra=1)