from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        # Validation
        if not all([username, email, password, password2]):
            return render(request, 'authentication/register.html', {
                'error': 'All fields are required',
                'username': username,
                'email': email
            })
            
        if password != password2:
            return render(request, 'authentication/register.html', {
                'error': 'Passwords do not match',
                'username': username,
                'email': email
            })
            
        if User.objects.filter(username=username).exists():
            return render(request, 'authentication/register.html', {
                'error': 'Username already exists',
                'email': email
            })
            
        if User.objects.filter(email=email).exists():
            return render(request, 'authentication/register.html', {
                'error': 'Email already in use',
                'username': username
            })
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        # Create profile
        profile = Profile.objects.create(user=user)
        
        # Auto login
        login(request, user)
        
        return redirect('home')


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not all([username, password]):
            return render(request, 'authentication/login.html', {
                'error': 'Username and password are required',
                'username': username
            })
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            return render(request, 'authentication/login.html', {
                'error': 'Invalid username or password',
                'username': username
            })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=request.user)
            
        return render(request, 'authentication/profile.html', {'profile': profile})
    
    def post(self, request):
        try:
            profile = request.user.profile
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=request.user)
            
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        profile.address = address
        profile.phone = phone
        profile.save()
        
        return redirect('profile') 