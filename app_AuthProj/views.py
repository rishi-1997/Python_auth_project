from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app_AuthProj.forms import sign_up_form
# Create your views here.
def Home(request):
    return render(request,'AuthPro_app/Home.html')

@login_required
def python(request):
    return render(request,'AuthPro_app/python.html')
@login_required
def java(request):
    return render(request,'AuthPro_app/java.html')
@login_required
def aptitude(request):
    return render(request,'AuthPro_app/aptitude.html')
def sign_up(request):
    form = sign_up_form()
    if request.method == 'POST':
        form = sign_up_form(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login/')
    return render(request,'AuthPro_app/signup.html',{'form':form})
def logout(request):
    return render(request,'registration/logout.html')