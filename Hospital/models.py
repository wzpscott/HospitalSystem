from django.db import models


gender_choices = (
        ('male', "男"),
        ('female', "女"),
    )


class Patient(models.Model):

    name = models.CharField(max_length=10)  # 姓名
    password = models.CharField(max_length=32)  # 密码
    gender = models.CharField(max_length=32, choices=gender_choices)  # 性别
    identity_card_no = models.CharField(max_length=32, unique=True)  # 身份证号

    medical_insurance = models.BooleanField()  # 是否有医保
    telephone_no = models.CharField(max_length=32)  # 电话号码
    birth_date = models.DateField()  # 出生日期
    create_time = models.DateTimeField(auto_now_add=True)  # 注册时间

    def __str__(self):
        return self.name


class Doctor(models.Model):
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
    name = models.CharField(max_length=10)  # 姓名
    password = models.CharField(max_length=32)  # 密码
    gender = models.CharField(max_length=32, choices=gender_choices)  # 性别
    identity_card_no = models.CharField(max_length=32, unique=True)  # 身份证号

    department = models.CharField(max_length=64, choices=department_choices)  # 科室
    title = models.CharField(max_length=64, choices=title_choices)  # 职称
    description = models.TextField(max_length=500, default='暂无简介')  # 简介

    create_time = models.DateTimeField(auto_now_add=True)  # 注册时间

    def __str__(self):
        return self.id.__str__()+'-'+self.name+'-'+self.get_department_display()


class Appointment(models.Model):
    time_choices = (
        ('Morning','上午'),
        ('Afternoon','下午')
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE) # 患者
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # 医生
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    appointment_date = models.DateTimeField()  # 预约日期
    appointment_time = models.CharField(max_length=10, choices=time_choices)  # 预约时间（上下午）
    isActive = models.BooleanField(default=True)  # 是否有效

    def __str__(self):
        return self.patient.name+'-'+self.doctor.name+'-'+self.appointment_date.__str__()+self.get_appointment_time_display()

    class Meta:
        ordering = ["-create_time"]


class Diagnosis(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # 患者
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # 医生
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True)  # 对应的挂号
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    detail = models.TextField()  # 诊断详情

    def __str__(self):
        return self.patient.name+'-'+self.doctor.name+'-'+self.create_time.__str__()

    class Meta:
        ordering = ["-create_time"]


class Medicine(models.Model):
    unit_choices = (
        ('g', '克'),
        ('ml', '毫升'),
        ('box', '盒')
    )
    name = models.CharField(max_length=50, unique=True)  # 药品名称
    inventory = models.IntegerField()  # 库存量
    unit = models.CharField(max_length=10, choices=unit_choices)  # 单位
    price = models.DecimalField(max_digits=7, decimal_places=2)  # 单价

    def __str__(self):
        return self.name


class MedicineRequest(models.Model):
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    amount = models.IntegerField()

    # class Meta:
    #     unique_together = ("diagnosis", "medicine")

    def __str__(self):
        return self.diagnosis.id.__str__()+':'+self.medicine.name+self.amount.__str__()+self.medicine.get_unit_display()


class Bill(models.Model):
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.diagnosis.id.__str__()+'账单'



