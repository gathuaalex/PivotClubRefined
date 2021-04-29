from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from accounts.forms import SignUpForm,ProfileForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import Profile
from .decorators import allowed_users
# Create your views here.
def signup(request):
    form = SignUpForm()
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username,password=raw_password)
                login(request,user)
                messages.success(request,'Account was created for '+ username)
                return redirect('signin')
            else:
                form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')
                

    context = {}
    return render(request, 'signin.html', context)
    

def signout(request):
    logout(request)
    return redirect('signin')


@allowed_users(allowed_roles=['Members'])
def accountSettings(request):
    member = request.user.Members
    form = ProfileForm(instance=member)

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=member)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request,'userprofile.html',context)
        