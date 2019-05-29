from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as login1
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your blog account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            context = 'На Ваш email было отправлено письмо для подтверждения аккаунта, после подтверждения вы сможете войти в аккаунт!'
            return render(request, 'registration/confirmation.html', {'context': context})
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login1(request, user)
        context = 'Подтверждение прошло успешно, теперь Вы можете войти в аккаунт!'
        return render(request, 'registration/confirmation.html', {'context': context})
    else:
        context = 'Ваш аккаунт уже активирован, если у Вас проблемы со входом обратитесь в службу поддержки!'
        return render(request, 'registration/confirmation.html', {'context': context})


