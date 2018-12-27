from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(widget = forms.Textarea(attrs={'cols': 40, 'rows':5, 'style':'resize:none;',
    'placeholder': "Присоединяйтесь к обсуждению...", 'required': True}), label = "")
