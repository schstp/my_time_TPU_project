from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


User._meta.get_field('email')._unique = True


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, *kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text ='''
        Пароль как минимум должен состоять из 8 символов,
        он не должен содержать только цифры 
        и не должен быть похож на логин или email'''
