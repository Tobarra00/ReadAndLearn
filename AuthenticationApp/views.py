from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class Register(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register/register.html', {'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('lists', kwargs={'username': user.username}))
        else:
            return render(request, 'register/register.html', {'form': form})
    
class Authenticate(View):
    
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login/login.html', {'form': form})
        
    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('lists', kwargs={'username': username}))
        else: 
            messages.error(request, 'Wrong user and password')
            return render(request, 'login/login.html', {'form': form})
        
    
def close_session(request):
    
    logout(request)
    return redirect(reverse('index'))