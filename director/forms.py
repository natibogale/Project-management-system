from bootstrap_datepicker_plus import DatePickerInput
from django import forms
# from django.contrib.admin import widgets
# from django.contrib.auth.models import User
from .models import *

from recordOfficer.models import *

from authentication.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column












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




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('subject', css_class='form-group col-md-6 mb-0'),
                Column('referenceNumber', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('signatore', css_class='form-group col-md-4 mb-0'),
                Column('receivedFrom', css_class='form-group col-md-4 mb-0'),
                Column('cc', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('dateWritten', css_class='form-group col-md-2 mb-0'),
                Column('dateReceived', css_class='form-group col-md-2 mb-0'),
                Column('project', css_class='form-group col-md-4 mb-0'),
                Column('type', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('file', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
        )



class forwardMessage(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        firstName = kwargs.pop('firstName')
        middleName = kwargs.pop('middleName')
        referenceNumber = kwargs.pop('instance')
        super(forwardMessage, self).__init__(*args, **kwargs)
        # self.fields['messageTo'].set = firstName
        self.fields['messageTo'].initial = firstName + "  "+ middleName
        self.fields['messageTo'].disabled = True
        self.fields['referenceNumber'].initial = referenceNumber
        self.fields['referenceNumber'].disabled = True

    class Meta:
        model = DirectorsLetterMessages
        exclude = ['dateSent','author']




class outgoingLettersForm(forms.ModelForm):
    # dateWritten = forms.DateField(widget=AdminDateWidget())
    # dateReceived = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    class Meta:
        model = OutgoingLetters
        fields = ['subject', 'referenceNumber','signatore','sentTo',
                    'cc','dateWritten','dateDelivered','project','type','pageNumber','file'
                    ]




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('subject', css_class='form-group col-md-6 mb-0'),
                Column('referenceNumber', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('signatore', css_class='form-group col-md-4 mb-0'),
                Column('sentTo', css_class='form-group col-md-4 mb-0'),
                Column('cc', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('dateWritten', css_class='form-group col-md-2 mb-0'),
                Column('dateDelivered', css_class='form-group col-md-2 mb-0'),
                Column('project', css_class='form-group col-md-4 mb-0'),
                Column('type', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('file', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
        )

class forwardOutLetter(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        firstName = kwargs.pop('firstName')
        middleName = kwargs.pop('middleName')
        referenceNumber = kwargs.pop('instance')
        super(forwardOutLetter, self).__init__(*args, **kwargs)
        # self.fields['messageTo'].set = firstName
        self.fields['messageTo'].initial = firstName + "  "+ middleName
        self.fields['messageTo'].disabled = True
        self.fields['referenceNumber'].initial = referenceNumber
        self.fields['referenceNumber'].disabled = True

    class Meta:
        model = DirectorsLetterMessagesOut
        exclude = ['dateSent','author']







class incomingMemosForm(forms.ModelForm):
    # dateWritten = forms.DateField(widget=AdminDateWidget())
    # dateReceived = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    class Meta:
        model = IncomingMemos
        fields = [ 'subject','dateWritten','signatore','receivedFrom','cc','project','file'
                    ]




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('subject', css_class='form-group col-md-6 mb-0'),
                Column('dateWritten', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('signatore', css_class='form-group col-md-4 mb-0'),
                Column('receivedFrom', css_class='form-group col-md-4 mb-0'),
                Column('cc', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('project', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('file', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
        )



class forwardInMemo(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        firstName = kwargs.pop('firstName')
        middleName = kwargs.pop('middleName')
        subject = kwargs.pop('instance')
        super(forwardInMemo, self).__init__(*args, **kwargs)
        # self.fields['messageTo'].set = firstName
        self.fields['messageTo'].initial = firstName + "  "+ middleName
        self.fields['messageTo'].disabled = True
        self.fields['subject'].initial = subject
        self.fields['subject'].disabled = True

    class Meta:
        model = DirectorsMemoMessages
        exclude = ['dateSent','author']





class outgoingMemosForm(forms.ModelForm):
    # dateWritten = forms.DateField(widget=AdminDateWidget())
    # dateReceived = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    class Meta:
        model = OutgoingMemos
        fields = [ 'subject','dateWritten','signatore','sentTo','cc','project','file'
                    ]




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].disabled = True

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('subject', css_class='form-group col-md-6 mb-0'),
                Column('dateWritten', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('signatore', css_class='form-group col-md-4 mb-0'),
                Column('sentTo', css_class='form-group col-md-4 mb-0'),
                Column('cc', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('project', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('file', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
        )



class forwardOutMemo(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        firstName = kwargs.pop('firstName')
        middleName = kwargs.pop('middleName')
        subject = kwargs.pop('instance')
        super(forwardOutMemo, self).__init__(*args, **kwargs)
        # self.fields['messageTo'].set = firstName
        self.fields['messageTo'].initial = firstName + "  "+ middleName
        self.fields['messageTo'].disabled = True
        self.fields['subject'].initial = subject
        self.fields['subject'].disabled = True

    class Meta:
        model = DirectorsMemoMessagesOut
        exclude = ['dateSent','author']



class projectDetailsForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].disabled = True

    class Meta:
        model = Projects
        # fields = '__all__'
        exclude = ['directorate','author','lastEdit'] 


class editProjects(forms.ModelForm):

    class Meta:
        model = Projects
        # fields = '__all__'
        exclude = ['directorate','author','dateAdded','assignedToLE','assignedToPE','lastEdit']

        widgets = {
            'worksContractSigningDate': DateInput(),
        'worksContractCommencementDate': DateInput(),
        'worksContractCompletionDate_original': DateInput(),
        'worksContractCompletionDate_revised': DateInput(),
        'servicesContractSigningDate': DateInput(),
        'servicesContractCommencementDate': DateInput(),
        'servicesContractCompletionDate_original': DateInput(),
        'servicesContractCompletionDate_revised': DateInput(),
        'expectedProjectCompletionDate': DateInput(),
        'variationOrders_approvalDate': DateInput(),
        'extentionOfTime_approvalDate': DateInput(),
        }



class addProjectsForm(forms.ModelForm):
    # worksContractSigningDate = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # worksContractCommencementDate = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # worksContractCompletionDate_original = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # worksContractCompletionDate_revised = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # servicesContractSigningDate = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # servicesContractCommencementDate = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # servicesContractCompletionDate_original = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # servicesContractCompletionDate_revised=  forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # expectedProjectCompletionDate = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # variationOrders_approvalDate = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))
    # extentionOfTime_approvalDate =  forms.DateField(widget=DatePickerInput(format='%Y-%m-%d'))



    assignedTo = forms.ChoiceField(choices = [])
    def __init__(self, *args, **kwargs):
        directorate = kwargs.pop('director')
        super(addProjectsForm, self).__init__(*args, **kwargs)
        self.fields['assignedTo'].choices = [(x.pk, x.firstName +"--"+ x.middleName + '-->Team Leader-'+ 'for team' +x.team.team) for x in User.objects.filter(directorate=directorate, title='Team Leader')]
        # self.fields['assignedTo'].queryset = User.objects.filter(directorate=directorate, title='Team Leader')
        # user_choices = User.objects.all()
        # print(user_choices)
        # for choice in user_choices:
        #     self.choices.append(
        #         (choice.id, choice.username)
        #             )




    class Meta:
        model = Projects
        # fields = '__all__'
        exclude = ['directorate','author','dateAdded','lastEdit','assignedToLE','assignedToPE']

        widgets = {
            'worksContractSigningDate': DateInput(),
        'worksContractCommencementDate': DateInput(),
        'worksContractCompletionDate_original': DateInput(),
        'worksContractCompletionDate_revised': DateInput(),
        'servicesContractSigningDate': DateInput(),
        'servicesContractCommencementDate': DateInput(),
        'servicesContractCompletionDate_original': DateInput(),
        'servicesContractCompletionDate_revised': DateInput(),
        'expectedProjectCompletionDate': DateInput(),
        'variationOrders_approvalDate': DateInput(),
        'extentionOfTime_approvalDate': DateInput(),
        }
    #
    # def save_model(self, request, obj, form, change):
    #     obj.directorate = request.user.directorate
    #     super().save_model(request, obj, form, change)


    # def form_valid(self, form, request):
    #     form.instance.author = request.user
    #     form.instance.directorate = request.user.directorate
    #     return super().form_valid(form)

    # def __init__(self, *args, **kwargs):
    #     super(addProjectsForm, self).__init__(*args, **kwargs)
    #     self.fields['directorate'].hidden = True
    #     self.fields['author'].disabled = True

    # def clean_directorate(self):
    #     self.cleaned_data['directorate'] = request.user.directorate
    #     # print ("#####################################",passed)
    #     # for instance in OutgoingLetters.objects.all():
    #     #     if instance.referenceNumber == passed:
    #     #         raise forms.ValidationError("A letter with this Reference Number exists. Make sure it is unique!")
    #     # return passed
