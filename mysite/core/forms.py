from django import forms
from django.db import models
from .models import *


class Bar(forms.Form):
    def __init__(self, fields, *args, **kwargs):
        super(Bar, self).__init__(*args, **kwargs)
        for i in range(len(fields)):
            self.fields['%s' %fields[i]] = forms.CharField()

class Foo(forms.Form):
    field = forms.CharField()


class base_form(forms.Form):
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    #forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    end_time = forms.TimeField(widget=forms.TimeInput(format='%I:%M:%p',attrs={'type': 'time'}))
    profession = forms.CharField(max_length=100)
    career = forms.CharField(max_length=100)
    #DateTimeField(input_formats='%H:%M %p'

class pre_text(forms.Form):
    aboutme=models.TextField(blank=True, verbose_name=('About Me'))

class main_form(forms.Form):
    profession = forms.CharField(max_length=100)
    stream = forms.CharField(max_length=100)
    hobbies = forms.CharField(max_length=100)

class Model1ModelForm(forms.ModelForm):
    class Meta:
        model = Model1
        fields = ('name', )


class am_pm(forms.Form):
    on_6am = forms.CharField(max_length=100)
    on_7am = forms.CharField(max_length=100)
    on_8am = forms.CharField(max_length=100)
    on_9am = forms.CharField(max_length=100)
    on_10am = forms.CharField(max_length=100)
    on_11am = forms.CharField(max_length=100)
    on_12am = forms.CharField(max_length=100)
    on_1pm = forms.CharField(max_length=100)
    on_2pm = forms.CharField(max_length=100)
    on_3pm = forms.CharField(max_length=100)
    on_4pm = forms.CharField(max_length=100)
    on_5pm = forms.CharField(max_length=100)
    on_6pm = forms.CharField(max_length=100)
    on_7pm = forms.CharField(max_length=100)
    on_8pm = forms.CharField(max_length=100)
    on_9pm = forms.CharField(max_length=100)
