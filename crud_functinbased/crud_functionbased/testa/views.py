from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def reg(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, 'your account has been successfully created !!')
             # this is shorcut method
            messages.info(request, 'you can login !!')

    else:
        fm = StudentRegistration()

    return render(request, 'testa/userregistration.html', {'form': fm})

def sign_up(request):

    if request.method == 'post':
        fm = UserCreationForm(request.post)
        if fm.is_valid():
            fm.save()
    else:
        fm = UserCreationForm()
    return render(request, 'testa/sign_up.html', {'form': fm})


