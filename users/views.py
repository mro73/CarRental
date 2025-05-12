from django.shortcuts import render
from . import forms

def register(request):
    if request.method == 'POST':
        form_user_register = forms.RegisterUserForm(request.POST)
        if form_user_register.is_valid():
            form_user_register.save()
            context = {'message': 'Success!'}
        else:
            print(form_user_register.error_messages)
            context = {'message': 'Zonk!'}
        print(context)
        return render(request, 'users/register.html.jinja', context=context)
    else:
        form_user_register = forms.RegisterUserForm()
        context = {'form_user_register': form_user_register}
        return render(request, 'users/register.html.jinja', context=context)

def login(request):
    return render(request, 'users/login.html.jinja')

def logout(request):
    return render(request, 'users/logout.html.jinja')