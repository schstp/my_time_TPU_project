from django.shortcuts import render
from django.http import Http404

def home(request):
    if request.user.is_authenticated:
        return render(request, 'main/base.html')
    raise Http404()


