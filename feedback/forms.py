from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'size':'40',
    'class': 'form-control', 'required': True, 'placeholder': "Имя"}), label = "Ваше имя:")
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'form-control',
    'placeholder': "Электронная почта"}), label = "Ваш e-mail:")
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':'40',
    'class': 'form-control', 'required': True, 'placeholder': "Возникшая проблема"}), label = "Тема:")
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows':5, 'style':'resize:none;',
    'placeholder': "Введите сообщение...", 'required': True}), label = "Сообщение:")