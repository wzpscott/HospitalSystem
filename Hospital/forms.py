from django import forms


class LoginForm(forms.Form):
    ID = forms.CharField(label="ID", max_length=128)
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)


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
