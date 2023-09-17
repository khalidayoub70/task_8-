from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render
from .models import Intern
from .forms import TaskForm
from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate


def home_page(request):
    # return HttpResponse('<b>Hello Interns<b>')
    return render(request, 'home.html')
# Create your views here.
def submit_work(request):
    interns = Intern.objects.all()
    
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect or display a success message
            return HttpResponseRedirect('/success/')
    else:
        form = TaskForm()
        print('internlist',interns)
    
    return render(request, 'home.html', {'form': form, 'interns': interns})
def Success(request):
    # return HttpResponse('<b>Hello Interns<b>')
    return render(request, 'success.html')
def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        my_user = User.objects.create_user(uname, password=password)
        my_user.save()
        print(uname, password)
        return redirect('login')

    return render(request, 'signup.html')
def login_page(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)

        if user is not None:
            login(request,user)
            return redirect('authorized')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request, 'login.html')


#def accounts(request):
#    return render(request, 'welcome.html',{'today': datetime.today()})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'authorized.html',{})

def dummy(request):
    data={
        'clist':['a','b','c','d','e','f','g','h','i','j']
    }
    return render(request,'dummy.html',data)