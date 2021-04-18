from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.core.validators import *
from authentication.models import *
from director.models import *


TYPES = (
            ('Claim/Vo','Claim/Vo'),
            ('Correspondence','Correspondence'),
            ('Report','Report'),
            ('Payment','Payment'),
            ('Row Document','Row Document'),
            )



def validate_file(value):
    filesize= value.size
    if filesize > 10485760:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    import os
    ext = os.path.splitext(value.name)[1]
    if settings.DEBUG:
        if not ext in settings.LETTER_EXT:
            raise ValidationError(u'File type not supported! Please upload only: .pdf, .doc, .docx, .rtf, .zip, .rar, .jpg, .jpeg, .png, .txt files.')








class IncomingLetters(models.Model):
    subject = models.TextField(verbose_name="Subject")
    referenceNumber = models.TextField(unique=True, verbose_name="Reference Number")
    dateWritten = models.DateField(verbose_name="Date Written")
    dateReceived = models.DateField(verbose_name="Date Received")
    signatore = models.CharField(max_length=400, verbose_name="Signatore")
    receivedFrom = models.CharField(max_length=400, verbose_name="Received From")
    cc= models.CharField(max_length=400,verbose_name="CC")
    project = models.ForeignKey('director.Projects', on_delete=models.CASCADE, verbose_name="Project")
    type = models.CharField(choices=TYPES,   max_length=100, verbose_name="Type")
    pageNumber = models.PositiveIntegerField(verbose_name="Page Number")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")
    dateAdded = models.DateTimeField(default=timezone.now,verbose_name="Date Added")
    lastEdit = models.DateTimeField(auto_now=True, verbose_name="Last Edit")
    file = models.FileField(upload_to='incoming_documents/',verbose_name="File", validators=[validate_file])
    directorate = models.ForeignKey('authentication.Directorates', on_delete=models.CASCADE, max_length=200, verbose_name="Directorate")
    seen = models.CharField(max_length=200, default="false", verbose_name="Seen")
    forwardedTo = models.CharField(max_length=200, default="Director", verbose_name="Forwarded To")
    level = models.PositiveIntegerField(default=1, verbose_name="Level")
    byDirector = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Director")
    byTeamleader = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Team Leader")
    byleadengineer = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Lead Engineer")
    byprojectengineer = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Project Engineer")


    def __str__(self):
        return f'{self.referenceNumber} '
    class Meta:
        verbose_name_plural = ("Incoming Letters")

    def save(self, *args, **kwargs):
        is_new = not self.pk
        super().save(*args, **kwargs)
        if is_new:
            DirectorsLetterMessages.objects.create(referenceNumber=self)
            TeamLeadersLetterMessages.objects.create(referenceNumber=self)
            LeadEngineersLetterMessages.objects.create(referenceNumber=self)
            ProjectEngineersLetterMessages.objects.create(referenceNumber=self)

    # def get_absolute_url(self):
    #     return reverse('letter-detail-1', kwargs={'pk' : self.pk})




class DirectorsLetterMessages(models.Model):
    referenceNumber = models.ForeignKey('IncomingLetters', on_delete=models.CASCADE, max_length=200, verbose_name="Reference Number")
    messageTo = models.CharField(max_length=200, default="Team Leader", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.referenceNumber} '
    class Meta:
        verbose_name_plural = ("Directors Letter Messages")


class TeamLeadersLetterMessages(models.Model):
    referenceNumber = models.ForeignKey('IncomingLetters', on_delete=models.CASCADE, max_length=200, verbose_name="Reference Number")
    messageTo = models.CharField(max_length=200, default="Lead Engineer", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.referenceNumber} '
    class Meta:
        verbose_name_plural = ("Team Leaders Letter Messages")


class LeadEngineersLetterMessages(models.Model):
    referenceNumber = models.ForeignKey('IncomingLetters', on_delete=models.CASCADE, max_length=200, verbose_name="Reference Number")
    messageTo = models.CharField(max_length=200, default="Project Engineer", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.referenceNumber} '
    class Meta:
        verbose_name_plural = ("Lead Engineers Letter Messages")



class ProjectEngineersLetterMessages(models.Model):
    referenceNumber = models.ForeignKey('IncomingLetters', on_delete=models.CASCADE, max_length=200, verbose_name="Reference Number")
    messageTo = models.CharField(max_length=200, default="Lead Engineer", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.referenceNumber} '
    class Meta:
        verbose_name_plural = ("Project Engineer Letter Messages")






class OutgoingLetters(models.Model):
    subject = models.TextField(verbose_name="Subject")
    referenceNumber = models.TextField(unique=True,verbose_name="Reference Number")
    dateWritten = models.DateField(verbose_name="Date Written")
    dateDelivered = models.DateField(verbose_name="Date Received")
    signatore = models.CharField(max_length=400, verbose_name="Signatore")
    sentTo = models.CharField(max_length=400, verbose_name="Sent To")
    cc= models.CharField(max_length=400, verbose_name="CC")
    project = models.ForeignKey('director.Projects', on_delete=models.CASCADE,verbose_name="Project")
    type = models.CharField(choices=TYPES, max_length=100,verbose_name="Type")
    pageNumber = models.PositiveIntegerField( verbose_name="Page Number")
    author = models.CharField(max_length=400, default=User, verbose_name="Author" )
    dateAdded = models.DateTimeField(default=timezone.now, verbose_name="Date Added")
    lastEdit = models.DateTimeField(auto_now=True, verbose_name="Last Edit")
    file = models.FileField(upload_to='outgoing_documents/', verbose_name="File", validators=[validate_file])
    directorate = models.ForeignKey('authentication.Directorates', on_delete=models.CASCADE, max_length=200, verbose_name="Directorate")
    seen = models.CharField(max_length=200, default="false", verbose_name="Seen")
    forwardedTo = models.CharField(max_length=200, default="Director", verbose_name="Forwarded To")
    level = models.PositiveIntegerField(default=1, verbose_name="Level")
    byDirector = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Director")
    byTeamleader = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Team Leader")
    byleadengineer = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Lead Engineer")
    byprojectengineer = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Project Engineer")

    def __str__(self):
        return f'{self.referenceNumber} '
    class Meta:
        verbose_name_plural = ("Outgoing Letters")

    def save(self, *args, **kwargs):
        is_new = not self.pk
        super().save(*args, **kwargs)
        if is_new:
            DirectorsLetterMessagesOut.objects.create(referenceNumber=self)
            TeamLeadersLetterMessagesOut.objects.create(referenceNumber=self)
            LeadEngineersLetterMessagesOut.objects.create(referenceNumber=self)
            ProjectEngineersLetterMessagesOut.objects.create(referenceNumber=self)



class DirectorsLetterMessagesOut(models.Model):
    referenceNumber = models.ForeignKey('OutgoingLetters', on_delete=models.CASCADE, max_length=200, verbose_name="Reference Number")
    messageTo = models.CharField(max_length=200, default="Team Leader", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.referenceNumber} '
    class Meta:
        verbose_name_plural = ("Directors Letter Messages Out")

class TeamLeadersLetterMessagesOut(models.Model):
    referenceNumber = models.ForeignKey('OutgoingLetters', on_delete=models.CASCADE, max_length=200, verbose_name="Reference Number")
    messageTo = models.CharField(max_length=200, default="Lead Engineer", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.referenceNumber} '
    class Meta:
        verbose_name_plural = ("Team Leaders Letter Messages Out")


class LeadEngineersLetterMessagesOut(models.Model):
    referenceNumber = models.ForeignKey('OutgoingLetters', on_delete=models.CASCADE, max_length=200, verbose_name="Reference Number")
    messageTo = models.CharField(max_length=200, default="Project Engineer", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.referenceNumber} '
    class Meta:
        verbose_name_plural = ("Lead Engineers Letter Messages Out")


class ProjectEngineersLetterMessagesOut(models.Model):
    referenceNumber = models.ForeignKey('OutgoingLetters', on_delete=models.CASCADE, max_length=200, verbose_name="Reference Number")
    messageTo = models.CharField(max_length=200, default="Lead Engineer", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.referenceNumber} '
    class Meta:
        verbose_name_plural = ("Project Engineers Letter Messages Out")


class IncomingMemos(models.Model):
    subject = models.TextField(verbose_name="Subject")
    dateWritten = models.DateField(verbose_name="Date Written")
    signatore = models.CharField(max_length=400, verbose_name="Signatore")
    receivedFrom = models.ForeignKey('authentication.Directorates', on_delete=models.CASCADE, verbose_name="Received From")
    cc= models.CharField(max_length=400, verbose_name="CC")
    project = models.ForeignKey('director.Projects', on_delete=models.CASCADE, verbose_name="Project")
    pageNumber = models.PositiveIntegerField(verbose_name="Page Number")
    author = models.CharField(max_length=400, default=User, verbose_name="Author")
    dateAdded = models.DateTimeField(default=timezone.now, verbose_name="Date Added")
    lastEdit = models.DateTimeField(auto_now=True, verbose_name="Last Edit")
    file = models.FileField(upload_to='incoming_documents/', verbose_name="File", validators=[validate_file])
    directorate = models.CharField( max_length=200, verbose_name="Directorate")
    seen = models.CharField(max_length=200, default="false", verbose_name="Seen")
    forwardedTo = models.CharField(max_length=200, default="Director", verbose_name="Forwarded To")
    level = models.PositiveIntegerField(default=1, verbose_name="Level")
    byDirector = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Director")
    byTeamleader = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Team Leader")
    byleadengineer = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Lead Engineer")
    byprojectengineer = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Project Engineer")

    def __str__(self):
        return f'{self.subject}'
    class Meta:
        verbose_name_plural = ("Incoming Memos")

    def save(self, *args, **kwargs):
        is_new = not self.pk
        super().save(*args, **kwargs)
        if is_new:
            DirectorsMemoMessages.objects.create(subject=self)
            TeamLeadersMemoMessages.objects.create(subject=self)
            LeadEngineersMemoMessages.objects.create(subject=self)
            ProjectEngineersMemoMessages.objects.create(subject=self)





class DirectorsMemoMessages(models.Model):
    subject = models.ForeignKey('IncomingMemos', on_delete=models.CASCADE, max_length=200, verbose_name="Subject")
    messageTo = models.CharField(max_length=200, default="Team Leader", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")


    def __str__(self):
        return f'{self.subject} '
    class Meta:
        verbose_name_plural = ("Directors Memo Messages")

class TeamLeadersMemoMessages(models.Model):
    subject = models.ForeignKey('IncomingMemos', on_delete=models.CASCADE, max_length=200, verbose_name="Subject")
    messageTo = models.CharField(max_length=200, default="Lead Engineer", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.subject} '
    class Meta:
        verbose_name_plural = ("Team Leaders Memo Messages")



class LeadEngineersMemoMessages(models.Model):
    subject = models.ForeignKey('IncomingMemos', on_delete=models.CASCADE, max_length=200, verbose_name="Subject")
    messageTo = models.CharField(max_length=200, default="Project Engineer", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.subject} '
    class Meta:
        verbose_name_plural = ("Lead Engineers Memo Messages")

class ProjectEngineersMemoMessages(models.Model):
    subject = models.ForeignKey('IncomingMemos', on_delete=models.CASCADE, max_length=200, verbose_name="Subject")
    messageTo = models.CharField(max_length=200, default="Lead Engineer", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.subject} '
    class Meta:
        verbose_name_plural = ("Project Engineers Memo Messages")


class OutgoingMemos(models.Model):
    subject = models.TextField(verbose_name="Subject")
    dateWritten = models.DateField(verbose_name="Date Written")
    signatore = models.CharField(max_length=400, verbose_name="Signatore")
    sentTo = models.ForeignKey('authentication.Directorates', on_delete=models.CASCADE,verbose_name="Sent To")
    cc= models.CharField(max_length=400, verbose_name="CC")
    project = models.ForeignKey('director.Projects', on_delete=models.CASCADE, verbose_name="Project")
    pageNumber = models.PositiveIntegerField(verbose_name="Page Number")
    author = models.CharField(max_length=400, default=User , verbose_name="Author")
    dateAdded = models.DateTimeField(default=timezone.now, verbose_name="Date Added")
    lastEdit = models.DateTimeField(auto_now=True, verbose_name="Last Edit")
    file = models.FileField(upload_to='outgoing_documents/', verbose_name="File", validators=[validate_file])
    directorate = models.CharField(max_length=200, verbose_name="Directorate")
    seen = models.CharField(max_length=200, default="false", verbose_name="Seen")
    forwardedTo = models.CharField(max_length=200, default="Director", verbose_name="Forwarded To")
    level = models.PositiveIntegerField(default=1, verbose_name="Level")
    byDirector = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Director")
    byTeamleader = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Team Leader")
    byleadengineer = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Lead Engineer")
    byprojectengineer = models.CharField(max_length=200, default="no",null=True, verbose_name="Seen by Project Engineer")


    def __str__(self):
        return f'{self.subject}'
    class Meta:
        verbose_name_plural = ("Outgoing Memos")

    def save(self, *args, **kwargs):
        is_new = not self.pk
        super().save(*args, **kwargs)
        if is_new:
            DirectorsMemoMessagesOut.objects.create(subject=self)
            TeamLeadersMemoMessagesOut.objects.create(subject=self)
            LeadEngineersMemoMessagesOut.objects.create(subject=self)
            ProjectEngineersMemoMessagesOut.objects.create(subject=self)






class DirectorsMemoMessagesOut(models.Model):
    subject = models.ForeignKey('OutgoingMemos', on_delete=models.CASCADE, max_length=200, verbose_name="Subject")
    messageTo = models.CharField(max_length=200, default="Team Leader", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.referenceNumber} '
    class Meta:
        verbose_name_plural = ("Directors Memo Messages Out")




class TeamLeadersMemoMessagesOut(models.Model):
    subject = models.ForeignKey('OutgoingMemos', on_delete=models.CASCADE, max_length=200, verbose_name="Subject")
    messageTo = models.CharField(max_length=200, default="Lead Engineer", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.subject} '
    class Meta:
        verbose_name_plural = ("Team Leaders Memo Messages Out")


class LeadEngineersMemoMessagesOut(models.Model):
    subject = models.ForeignKey('OutgoingMemos', on_delete=models.CASCADE, max_length=200, verbose_name="Subject")
    messageTo = models.CharField(max_length=200, default="Project Engineer", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.subject} '
    class Meta:
        verbose_name_plural = ("Lead Engineers Memo Messages Out")
    


class ProjectEngineersMemoMessagesOut(models.Model):
    subject = models.ForeignKey('OutgoingMemos', on_delete=models.CASCADE, max_length=200, verbose_name="Subject")
    messageTo = models.CharField(max_length=200, default="Lead Engineer", verbose_name="Message To")
    message = models.TextField( default="Message", verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default=User ,verbose_name="Author")




    # def save(self, *args, **kwargs):
    #     self.author = self.user
    #     super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.subject} '
    class Meta:
        verbose_name_plural = ("Project Engineers Memo Messages Out")