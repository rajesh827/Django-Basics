from django import forms
from .models import Patient
from .models import AppUser
from .models import StudentProject
import os
import re

# Q2
class PatientForm(forms.ModelForm):
    # Enforce YYYY-MM-DD format strictly for DOB
    dob = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        error_messages={'invalid': 'DOB must be in YYYY-MM-DD format.'}
    )

    class Meta:
        model = Patient
        fields = ['name', 'patient_id', 'mobile', 'gender', 'address', 'dob', 'doctor_name']
        widgets = {
        'address': forms.Textarea(attrs={'rows': 1, 'cols': 30})  # smaller textarea
    }

    # Custom validation for Mobile number
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        
        # Regex explanation:
        # ^(98|97|96) : Starts with 98, 97, or 96
        # \d{7}$      : Followed by exactly 7 digits (making 10 total)
        if not re.match(r'^(98|97|96)\d{8}$', mobile):
            raise forms.ValidationError("Mobile must be 10 digits and start with 98, 97, or 96.")
        
        return mobile
    
#Q3
class RegistrationForm(forms.ModelForm):
    # Renders the password input as hidden dots (***)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AppUser
        fields = ['full_name', 'email', 'username', 'password']

    # Rule 3: Username must start with string (letters) followed by number(s)
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        # Regex explanation:
        # ^[A-Za-z]+ : Starts with one or more letters
        # [0-9]+$    : Ends with one or more numbers
        if not re.match(r'^[A-Za-z]+[0-9]+$', username):
            raise forms.ValidationError("Username must start with letters and end with numbers (e.g., admin123).")
        
        return username

    # Rule 4: Password length must be MORE than 8 characters (so 9 or more)
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if len(password) <= 8:
            raise forms.ValidationError("Password must be strictly more than 8 characters long.")
        
        return password
    
#Q4
class ImageUploadForm(forms.Form):
    # The file input field
    upload_file = forms.FileField()

    def clean_upload_file(self):
        file = self.cleaned_data.get('upload_file')
        
        if file:
            # 1. Validate File Extension
            # Extracts the extension (e.g., '.jpg') and removes the dot
            ext = os.path.splitext(file.name)[1].lower().replace('.', '')
            valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
            
            if ext not in valid_extensions:
                raise forms.ValidationError("Unsupported file extension. Only jpg, jpeg, png, and gif are allowed.")
            
            # 2. Validate File Size (Less than 2MB)
            max_size = 2 * 1024 * 1024 # 2 Megabytes in bytes
            
            if file.size >= max_size:
                raise forms.ValidationError("File size must be strictly less than 2MB.")
                
        return file

#Q5
class ProjectSubmissionForm(forms.ModelForm):
    class Meta: #this is a special class that tells Django which model to use and which fields to include
        model = StudentProject
        fields = ['tu_reg_no', 'email', 'project_file']

    def clean_project_file(self): # This method is automatically called when form.is_valid() is invoked in the view. It validates the uploaded file.
        file = self.cleaned_data.get('project_file')
        
        if file:
            # 1. Validate File Size (< 5MB)
            max_size = 5 * 1024 * 1024 # 5MB in bytes
            if file.size >= max_size:
                raise forms.ValidationError("File size must be strictly less than 5MB.")

            # 2. Validate File Extension
            # Extract the extension and make it lowercase
            ext = os.path.splitext(file.name)[1].lower().replace('.', '')
            valid_extensions = ['pdf', 'doc', 'docx', 'ppt', 'pptx', 'jpeg']
            
            if ext not in valid_extensions:
                raise forms.ValidationError(
                    f"Unsupported file format. Allowed formats are: {', '.join(valid_extensions)}"
                )

        return file