from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from .forms import ContactForm

def contactForm(reguest):
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            recipient_list = ['mytimeteam@mail.ru']

            try:
                send_mail(subject, message + '\nПолучено от: ' + sender, 'mytimeteam@mail.ru', recipient_list)
            except BadHeaderError: #Защита от уязвимости
                return HttpResponse('Invalid header found')

            return HttpResponseRedirect('/support/thanks')

    else:
        form = ContactForm()

    context = {
        'title': 'Support',
        'form': form,
        'username': auth.get_user(reguest).username
    }

    return render(reguest, 'feedback/support.html', context)

def thanks(reguest):
    context = {
        'Title': 'Thanks',
        'thanks': 'Thank you!'
    }

    return render(reguest, 'feedback/thanks.html', context)