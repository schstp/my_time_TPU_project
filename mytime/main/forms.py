from django import forms

class DateForm(forms.Form):

    date = forms.DateTimeField(
        required=False,
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#task-group-container"',
            'id': 'datetime-input',
            'style': 'display: none;',
        })
    )

