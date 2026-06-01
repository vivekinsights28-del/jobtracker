from django import forms
from django.forms import ModelForm
from .models import Job

class JobForm(ModelForm):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Rejected', 'Rejected'),
    ]

    status = forms.ChoiceField(choices=STATUS_CHOICES)
    date_applied = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Job
        fields = ['company', 'role', 'status', 'date_applied']
