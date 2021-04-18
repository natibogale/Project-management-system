from authentication.models import User
from bootstrap_datepicker_plus import DatePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from django import forms
from recordOfficer.models import *

from .models import *
from director.models import *

class DateInput(forms.DateInput):
    input_type = 'date'





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
        model = LeadEngineersLetterMessages
        exclude = ['dateSent','author']


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

class editProjects(forms.ModelForm):
    assignedToPE = forms.ChoiceField(choices =[])
    def __init__(self, *args, **kwargs):
        directorate = kwargs.pop('director')
        team = kwargs.pop('team')
        super(editProjects, self).__init__(*args, **kwargs)
        self.fields['assignedToPE'].choices = [(x.pk, x.firstName +"--"+ x.middleName + '-->Project Engineer-'+ 'for team' +x.team.team) for x in User.objects.filter(directorate=directorate, title='Project Engineer')]
    class Meta:
        model = Projects
        fields = ['assignedToPE']
        # exclude = ['directorate','author','dateAdded','assignedToLE','assignedToPE','lastEdit']

        # widgets = {
        #     'worksContractSigningDate': DateInput(),
        # 'worksContractCommencementDate': DateInput(),
        # 'worksContractCompletionDate_original': DateInput(),
        # 'worksContractCompletionDate_revised': DateInput(),
        # 'servicesContractSigningDate': DateInput(),
        # 'servicesContractCommencementDate': DateInput(),
        # 'servicesContractCompletionDate_original': DateInput(),
        # 'servicesContractCompletionDate_revised': DateInput(),
        # 'expectedProjectCompletionDate': DateInput(),
        # 'variationOrders_approvalDate': DateInput(),
        # 'extentionOfTime_approvalDate': DateInput(),
        # }


class projectDetailsForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].disabled = True
    assignedToLE =  forms.CharField(max_length = 150) 
    def __init__(self, *args, **kwargs):
        le = kwargs.pop('lead_engineer_id')
        super(projectDetailsForm, self).__init__(*args, **kwargs)
        print('ssssssssssssssssssssssssssssss')
        self.fields['assignedToLE'].value = [print (x.firstName +"--"+ x.middleName + '-->Lead Engineer-'+ 'for team' +x.team.team) for x in User.objects.filter(id=le, title='Lead Engineer')]
    class Meta:
        model = Projects
        # fields = '__all__'
        exclude = ['directorate','author','lastEdit'] 






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
        model = LeadEngineersLetterMessagesOut
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
        model = LeadEngineersMemoMessages
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
        model = LeadEngineersMemoMessagesOut
        exclude = ['dateSent','author']