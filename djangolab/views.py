from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from .models import Student
from .forms import PatientForm
from .forms import RegistrationForm
from .forms import ProjectSubmissionForm


def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pword = request.POST.get('password')

        try:
            student = Student.objects.get(username=uname)
            
            if pword == student.password:
                return redirect('dashboard') 
            else:
                return HttpResponse('Invalid username/password')
                
        except Student.DoesNotExist:
            return HttpResponse('Invalid username/password')

    return render(request, 'login.html')

def dashboard_view(request):
    return HttpResponse('Welcome to Dashboard!')

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponse('<h2>Patient data stored successfully!</h2>')
    else:
        form = PatientForm()

    return render(request, 'patient_form.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            user_instance = form.save(commit=False)
            raw_password = form.cleaned_data['password']
            user_instance.password = make_password(raw_password)
            
            user_instance.save()
            
            return HttpResponse('<h2>Registration successful! Data stored.</h2>')
    else:
        form = RegistrationForm()

    return render(request, 'registration_form.html', {'form': form})

def upload_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            uploaded_file = form.cleaned_data['upload_file']
            
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            
            return HttpResponse(f"<h2>Success! '{uploaded_file.name}' was uploaded.</h2>")
    else:
        form = ImageUploadForm()

    return render(request, 'upload_form.html', {'form': form})

def submit_project(request):
    if request.method == 'POST':
        form = ProjectSubmissionForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Project submitted and saved to database successfully!</h2>")
    else:
        form = ProjectSubmissionForm()

    return render(request, 'project_form.html', {'form': form})