from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from hospital.models import Patient, Doctor


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            print("USER CREATED:", user.username, user.role)  # DEBUG

            if user.role == 'patient':
                Patient.objects.create(user=user)

            elif user.role == 'doctor':
                Doctor.objects.create(user=user)

            return redirect('login')

        else:
            print("FORM ERRORS:", form.errors)  # DEBUG

    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        print("LOGIN TRY:", username, password)   # DEBUG
        print("USER:", user)                      # DEBUG

        if user is not None:
            login(request, user)

            print("ROLE:", user.role)  # DEBUG

            if user.role == 'patient':
                return redirect('/hospital/patient/')
            elif user.role == 'doctor':
                return redirect('/hospital/doctor/')
            else:
                return redirect('/admin/')
        else:
            error = "Invalid credentials"

    return render(request, 'accounts/login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('login')

'''from django.shortcuts import render,redirect 
from django.contrib.auth import authenticate,login, logout
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login.html')
    else:
        form = CustomUserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})
def login_view(request):
    
        error = None
        if request.method == 'POST':'''


        
        



        

















