from django.db import models

# Q1
class Student(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
# Q2
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
        db_table = 'patients'  # Forces the table name to be 'patients'

    def __str__(self):
        return self.name
    
#Q3
class AppUser(models.Model):
    # Rule 1: Length up to 40 characters
    full_name = models.CharField(max_length=40)
    
    # Rule 2: Must be a valid email address
    email = models.EmailField(unique=True)
    
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128) # 128 is standard for storing hashed passwords

    def __str__(self):
        return self.username
    
#Q5
class StudentProject(models.Model):
    # Registration number
    tu_reg_no = models.CharField(max_length=50, verbose_name="TU Registration Number")
    
    # Proper email format validation is built-in here
    email = models.EmailField(verbose_name="Email Address")
    
    # File upload field. Files will be saved in a 'projects/' folder
    project_file = models.FileField(upload_to='projects/', verbose_name="Upload your Project File")

    def __str__(self):
        return self.tu_reg_no