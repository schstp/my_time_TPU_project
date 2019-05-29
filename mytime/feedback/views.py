from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from .forms import ContactForm

def contactForm(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if request.user.is_authenticated:
            del form.fields['sender']

        if form.is_valid():
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']

            recipient_list = ['myTime.help.team@gmail.com']

            if request.user.is_authenticated:
                sender = request.user.email
            else:
                sender = form.cleaned_data['sender']

            message = name + '\n' + message + '\nПолучено от: ' + sender

            try:
                send_mail(subject, message, 'myTime.help.team@gmail.com', recipient_list)
            except BadHeaderError:
                return HttpResponse('Invalid header found')

            return HttpResponseRedirect('/support/thanks')

    else:
        form = ContactForm()
        if request.user.is_authenticated:
            del form.fields['sender']

    context = {
        'title': 'Support',
        'form': form,
        'username': auth.get_user(request).username
    }

    return render(request, 'feedback/support.html', context)

def thanks(reguest):
    context = {
        'Title': 'Thanks',
        'thanks': 'Thank you!'
    }

    return render(reguest, 'feedback/thanks.html', context)