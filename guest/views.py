from django.shortcuts import render

def home(request):
    context = {

    }
    return render(request, 'guest/home.html', context)

def blog(request):
    context = {
        'title': 'Blog',
    }
    return render(request, 'guest/blog.html', context)

def support(request):
    context = {
        'title': 'Support',
    }
    return render(request, 'guest/support.html', context)