from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    patient_id = models.CharField(max_length=50, unique=True)
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField(blank=True, null=True) # Optional
    dob = models.DateField()
    doctor_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'patients'

    def __str__(self):
        return self.name
    
class AppUser(models.Model):
    full_name = models.CharField(max_length=40)
    
    email = models.EmailField(unique=True)
    
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
class StudentProject(models.Model):
    tu_reg_no = models.CharField(max_length=50, verbose_name="TU Registration Number")
    email = models.EmailField(verbose_name="Email Address")
    project_file = models.FileField(upload_to='projects/', verbose_name="Upload your Project File")

    def __str__(self):
        return self.tu_reg_no