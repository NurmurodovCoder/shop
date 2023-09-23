from django.shortcuts import render, redirect
from django.core.cache import cache

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate


from .forms import Account
from .sms import send_sms

def register(request):
    model=0
    if request.method == 'POST':
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        phone_number = request.POST['phone_number']
        city = request.POST['city']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
            if phone_number.isdigit() and len(phone_number) == 12:
                send_sms(phone_number) # sms ketdi
                return redirect('account:code', phone_number=phone_number, last_name=last_name, first_name=first_name, city=city, password1=password1)

            else:
                messages.info(request, "Telefon raqam xato !")

        else:
            messages.info(request, "Parollar bir xil emas , qayta urinib koring !")


    context = {
        'model':model
    }
    return render(request, 'register.html', context)

def code(request, last_name, first_name, phone_number, city, password1):
    model = 1
    if request.method == 'POST':
        code = request.POST['code']
        if cache.get(phone_number) == int(code):
            user = Account.objects.create_user(last_name=last_name, first_name=first_name, phone_number=phone_number, city=city, password=password1)
            user.save()
            messages.success(request, "Royhatdan otdingiz !")
            return redirect('index')

        else:    
            messages.info(request, "Parol xato !")

    context = {
        'model':model
    }
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        print(phone_number, password)
        user = authenticate(request, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Tizimga muvaffaqiyatli kirdingiz")
            return redirect('store')
        else:
            messages.info(request, "Xatolik bor. Qayta tekshiring !!!")
    return render(request, "signin.html")


def logout_user(request):
    logout(request)
    messages.success(request, "Tizimdan chiqdingiz !")

    return redirect('store')