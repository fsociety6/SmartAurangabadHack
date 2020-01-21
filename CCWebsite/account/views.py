from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from .forms import LoginForm, UserExtendedForm, UserForm
from django.http import HttpResponse


# Create your views here.
def register(request):
    if request.method == "POST":
        userform = UserForm(data=request.POST)
        userextendedform = UserExtendedForm(data=request.POST)
        if userform.is_valid() and userextendedform.is_valid():
            user = userform.save()
            userextended = userextendedform.save(commit=False)
            userextended.user_object = user
            userextended.save()
            return HttpResponse('signed Up')
    else:
        userform = UserForm()
        userextendedform = UserExtendedForm()
    return render(request, 'account/register.html',
                  {"userform": userform, 'userextendedform': userextendedform})


def user_login_view(request):
    if request.method == "POST":
        loginform = AuthenticationForm(request,data=request.POST)
        if loginform.is_valid():
            cd = loginform.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponse("Login SuccessFully !!!")
            else:
                return HttpResponse("UnSuccessFully Login !!!")
    else:
        loginform = AuthenticationForm
    return render(request, "account/login.html", {"loginform": loginform})
