from django import forms
from .models import Patient
from .models import AppUser
from .models import StudentProject
import os, re

class PatientForm(forms.ModelForm):
    dob = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        error_messages={'invalid': 'DOB must be in YYYY-MM-DD format.'}
    )

    class Meta:
        model = Patient
        fields = ['name', 'patient_id', 'mobile', 'gender', 'address', 'dob', 'doctor_name']
        widgets = {
        'address': forms.Textarea(attrs={'rows': 1, 'cols': 30}) 
    }

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        
        if not re.match(r'^(98|97|96)\d{8}$', mobile):
            raise forms.ValidationError("Mobile must be 10 digits and start with 98, 97, or 96.")
        
        return mobile
    
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AppUser
        fields = ['full_name', 'email', 'username', 'password']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if not re.match(r'^[A-Za-z]+[0-9]+$', username):
            raise forms.ValidationError("Username must start with letters and end with numbers (e.g., admin123).")
        
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if len(password) <= 8:
            raise forms.ValidationError("Password must be strictly more than 8 characters long.")
        
        return password
    
class ImageUploadForm(forms.Form):
    upload_file = forms.FileField()

    def clean_upload_file(self):
        file = self.cleaned_data.get('upload_file')
        
        if file:
            ext = os.path.splitext(file.name)[1].lower().replace('.', '')
            valid_extensions = ['jpg', 'jpeg', 'png', 'gif']
            
            if ext not in valid_extensions:
                raise forms.ValidationError("Unsupported file extension. Only jpg, jpeg, png, and gif are allowed.")
            
            max_size = 2 * 1024 * 1024 
            
            if file.size >= max_size:
                raise forms.ValidationError("File size must be strictly less than 2MB.")
                
        return file

class ProjectSubmissionForm(forms.ModelForm):
    class Meta:
        model = StudentProject
        fields = ['tu_reg_no', 'email', 'project_file']

    def clean_project_file(self):
        file = self.cleaned_data.get('project_file')
        
        if file:
            max_size = 5 * 1024 * 1024 
            if file.size >= max_size:
                raise forms.ValidationError("File size must be strictly less than 5MB.")

            ext = os.path.splitext(file.name)[1].lower().replace('.', '')
            valid_extensions = ['pdf', 'doc', 'docx', 'ppt', 'pptx', 'jpeg']
            
            if ext not in valid_extensions:
                raise forms.ValidationError(
                    f"Unsupported file format. Allowed formats are: {', '.join(valid_extensions)}"
                )

        return file