from django.shortcuts import render
from .forms import *
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


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            print(form.cleaned_data)
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                return HttpResponse("Logged In")
    else:
        if request.user.is_authenticated:
            return HttpResponse('Already Login')
    loginform = LoginForm()
    return render(request, "account/login.html", {"loginform": loginform})
