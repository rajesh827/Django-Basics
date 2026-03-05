from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from .models import Student
from .forms import PatientForm
from .forms import RegistrationForm
from .forms import ProjectSubmissionForm


# Q1
def login_view(request):
    if request.method == 'POST':
        # 1. Accept username and password as arguments from the form
        uname = request.POST.get('username')
        pword = request.POST.get('password')

        try:
            # 2. Get the student from the Student table
            student = Student.objects.get(username=uname)
            
            # 3. Check if the plain-text password matches the hashed password in the DB
            # if check_password(pword, student.password):
            if pword == student.password:
                # Credentials match, redirect to dashboard
                return redirect('dashboard') 
            else:
                # Password did not match
                return HttpResponse('Invalid username/password')
                
        except Student.DoesNotExist:
            # Username was not found in the Student table
            return HttpResponse('Invalid username/password')

    # Render login page for GET requests
    return render(request, 'login.html')

def dashboard_view(request):
    return HttpResponse('Welcome to Dashboard!')

# Q2
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        
        # is_valid() triggers the validation rules we wrote in forms.py
        if form.is_valid():
            form.save() # Stores the data into the 'patients' table
            return HttpResponse('<h2>Patient data stored successfully!</h2>')
    else:
        # If GET request, show an empty form
        form = PatientForm()

    return render(request, 'patient_form.html', {'form': form})

#Q3
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        # is_valid() runs all the rules we defined in forms.py
        if form.is_valid():
            # commit=False creates the object but pauses before saving to the DB
            user_instance = form.save(commit=False)
            
            # Hash the password for security before storing it
            raw_password = form.cleaned_data['password']
            user_instance.password = make_password(raw_password)
            
            # Now store the data into the database
            user_instance.save()
            
            return HttpResponse('<h2>Registration successful! Data stored.</h2>')
    else:
        # If it's a normal visit to the page, show an empty form
        form = RegistrationForm()

    return render(request, 'registration_form.html', {'form': form})

#Q4
def upload_view(request):
    if request.method == 'POST':
        # You MUST include request.FILES to handle file uploads
        form = ImageUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Get the validated file
            uploaded_file = form.cleaned_data['upload_file']
            
            # Save the file to the server
            fs = FileSystemStorage()
            fs.save(uploaded_file.name, uploaded_file)
            
            return HttpResponse(f"<h2>Success! '{uploaded_file.name}' was uploaded.</h2>")
    else:
        # Show empty form on GET request
        form = ImageUploadForm()

    return render(request, 'upload_form.html', {'form': form})

#Q5
def submit_project(request):
    if request.method == 'POST':
        # Pass both POST data (text) and FILES data (the uploaded document)
        form = ProjectSubmissionForm(request.POST, request.FILES)
        
        # is_valid() checks if fields are empty, if email is correct, and runs our 5MB/extension checks
        if form.is_valid():
            # Automatically saves the tu_reg_no and email to the database, 
            # and saves the file to the media folder
            form.save()
            return HttpResponse("<h2>Project submitted and saved to database successfully!</h2>")
    else:
        form = ProjectSubmissionForm()

    return render(request, 'project_form.html', {'form': form})