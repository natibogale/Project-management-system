from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import User
from .models import *
from django.core.validators import validate_slug, validate_email
from django.contrib.admin.widgets import AdminDateWidget

class ToDoForm(forms.Form):
    todo = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    date = forms.DateField(
        widget=DatePickerInput(format='%m/%d/%Y')
    )



class DateInput(forms.DateInput):
    input_type = 'date'

class incomingLettersForm(forms.ModelForm):
    # dateWritten = forms.DateField(widget=AdminDateWidget())
    # dateReceived = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    class Meta:
        model = IncomingLetters
        fields = ['subject', 'referenceNumber','signatore','receivedFrom',
                    'cc','dateWritten','dateReceived','project','type','pageNumber','file'
                    ]

        widgets = {
            'dateWritten': DateInput(),
            'dateReceived': DateInput(),
        }

    # def __init__(self, *args, **kwargs):
    #     super(incomingLettersForm, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].disabled = True






        # widgets = {
        #     'dateWritten': DatePickerInput(), # default date-format %m/%d/%Y will be used
        #     'dateReceived': DatePickerInput(format='%Y-%m-%d'), # specify date-frmat
        # }


    # def clean_referenceNumber(self):
    #     passed = self.cleaned_data['referenceNumber']
    #     print ("#####################################",passed)
    #     for instance in IncomingLetters.objects.all():
    #         if instance.referenceNumber == passed:
    #             raise forms.ValidationError("A letter with this Reference Number exists. Make sure it is unique!")
    #     return passed


class outgoingLettersForm(forms.ModelForm):
    # dateWritten = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # dateDelivered = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))

    class Meta:
        model = OutgoingLetters
        fields = ['subject', 'referenceNumber','signatore','sentTo','cc','dateDelivered','dateWritten',
                  'project','type','pageNumber','file']
        widgets = {
            'dateWritten': DateInput(),
            'dateDelivered': DateInput(),
        }

    # def clean_referenceNumber(self):
    #     passed = self.cleaned_data['referenceNumber']
    #     print ("#####################################",passed)
    #     for instance in OutgoingLetters.objects.all():
    #         if instance.referenceNumber == passed:
    #             raise forms.ValidationError("A letter with this Reference Number exists. Make sure it is unique!")
    #     return passed


class incomingMemosForm(forms.ModelForm):
    # dateWritten = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    class Meta:
        model = IncomingMemos
        fields = ['subject','signatore','receivedFrom',
                  'cc','dateWritten','project','pageNumber',
                  'file']

        widgets = {
            'dateWritten': DateInput(),
        }

class outgoingMemosForm(forms.ModelForm):
    # dateWritten = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    class Meta:
        model = OutgoingMemos
        fields = ['subject','signatore','sentTo',
                 'cc','dateWritten','project','pageNumber',
                  'file']
        widgets = {
            'dateWritten': DateInput(),
        }
