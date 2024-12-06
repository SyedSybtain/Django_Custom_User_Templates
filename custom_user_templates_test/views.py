from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    
    return render(request, 'home.html')


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('base')
    else:
        form = UserCreationForm()
        
    my_context = {'form': form }

    return render(request, 'registration/register.html', my_context)