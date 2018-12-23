from django.shortcuts import render

def home(request):

    context = {

    }
    return render(request, 'guest/home.html', context)

def support(request):

    context = {
        'title': 'Support',
    }
    return render(request, 'guest/support.html', context)

def login(request):

    return render(request, 'registration/login.html')

def logout(request):

    return render(request, 'registration/logged_out.html')
