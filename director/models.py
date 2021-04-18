from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
from django.core.validators import *
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from authentication.models import *
from django.utils import timezone
from django.conf import settings
from django.http import HttpResponse

def validate_file(value):
    filesize= value.size
    if filesize > 10485760:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    import os
    ext = os.path.splitext(value.name)[1]
    if settings.DEBUG:
        if not ext in settings.LETTER_EXT:
            raise ValidationError(u'File type not supported! Please upload only: .pdf, .doc, .docx, .rtf, .zip, .rar, .jpg, .jpeg, .png, .txt files.')

def dir(request):
    dir_from_views = request.user.directorate


class Projects(models.Model):
    projectName = models.TextField( verbose_name="Project Name", max_length=500 )
    contractorName = models.CharField(verbose_name="Contractor's Name", max_length=500)
    consultantName = models.CharField(verbose_name="Consultant's Name", max_length=500)
    worksContractAmount_original = models.CharField(verbose_name="Works Contract Amount - Original", blank=True, max_length=500)
    worksContractAmount_revised = models.CharField(verbose_name="Works Contract Amount - Revised", blank=True, max_length=500)
    contractType = models.CharField(verbose_name="Contract Type", blank=True, max_length=500)
    roadSurfaceType = models.CharField(verbose_name="Road Surface Type", blank=True, max_length=500)
    designStandard = models.CharField(verbose_name="Design Standard", blank=True, max_length=500)
    location_region = models.CharField(verbose_name="Location - Region", blank=True, max_length=500)
    location_zone = models.CharField(verbose_name="Location - Zone", blank=True, max_length=500)
    location_woreda = models.CharField(verbose_name="Location - Woreda", blank=True, max_length=500)
    designControlPoints = models.CharField(verbose_name="Design Control Points", blank=True, max_length=500)
    worksContractSigningDate = models.DateField( verbose_name="Works Contract Signing Date", blank=True,null=True, max_length=100)
    worksContractCommencementDate = models.DateField( verbose_name="Works Contract Commencement Date", blank=True, max_length=100)
    worksContractCompletionDate_original = models.DateField( verbose_name="Works Contract Completion Date - Original", blank=True, max_length=500)
    worksContractCompletionDate_revised = models.DateField( verbose_name="Works Contract Completion Date - Revised", blank=True, max_length=500)
    servicesContractSigningDate = models.DateField( verbose_name="Services Contract Signing Date", blank=True, max_length=100)
    servicesContractAmount = models.CharField(verbose_name="Services Contract Amount", blank=True, max_length=500)
    servicesContractCommencementDate = models.DateField( verbose_name="Services Contract Commencement Date", blank=True, max_length=500)
    servicesContractCompletionDate_original = models.DateField( verbose_name="Services Contract Completion Date - Original", blank=True, max_length=500)
    servicesContractCompletionDate_revised= models.DateField( verbose_name="Services Contract Completion Date - Revised", blank=True, max_length=500)
    expectedProjectCompletionDate = models.DateField( verbose_name="Expected Project Completion Date", blank=True, max_length=500)
    projectStartPoint_easting = models.CharField(verbose_name="Project Start Point - Easting", blank=True, max_length=500)
    projectStartPoint_northing = models.CharField(verbose_name="Project Start Point - Northing", blank=True, max_length=500)
    projectEndPoint_easting = models.CharField(verbose_name="Project End Point - Easting", blank=True, max_length=500)
    projectEndPoint_northing = models.CharField(verbose_name="Project End Point - Northing", blank=True, max_length=500)
    startPointDistancefromAA = models.CharField(verbose_name="Start Point Distance from AA", blank=True, max_length=500)
    projectLength = models.CharField(verbose_name="Project Length", blank=True, max_length=500)
    variationOrders_number = models.CharField(verbose_name="Variation Orders - Number", blank=True, max_length=500)
    variationOrders_amount = models.CharField(verbose_name="Variation Orders - Amount", blank=True, max_length=500)
    variationOrders_approvalDate = models.DateField( verbose_name="Variation Orders - Approval Date", blank=True, max_length=500)
    variationOrders_reason = models.CharField(verbose_name="Variation Orders - Reason", blank=True, max_length=500)
    extentionOfTime_number = models.CharField(verbose_name="Extention of Time - Number", blank=True, max_length=500)
    extentionOfTime_amount = models.CharField(verbose_name="Extention of Time - Amount", blank=True, max_length=500)
    extentionOfTime_approvalDate = models.DateField( verbose_name="Extention of Time - Approval Date", blank=True, max_length=500)
    extentionOfTime_reason = models.CharField(verbose_name="Extention of Time- Reason", blank=True, max_length=500)
    ERAPlanThisMonth_physical = models.CharField(verbose_name="ERA Plan This Month - Physical", blank=True, max_length=500)
    ERAPlanThisQuarter_physical= models.CharField(verbose_name="ERA Plan This Quarter - Physical", blank=True, max_length=500)
    ERAPlanThisFY_physical= models.CharField(verbose_name="ERA Plan This FY - Physical", blank=True, max_length=500)
    ERAPlanToDate_physical= models.CharField(verbose_name="ERA Plan To Date - Physical", blank=True, max_length=500)
    accomplishmentThisMonth_physical = models.CharField(verbose_name="Accomplishment This Month - Physical", blank=True, max_length=500)
    accomplishmentThisQuarter_physical= models.CharField(verbose_name="Accomplishment This Quarter - Physical", blank=True, max_length=500)
    accomplishmentThisFY_physical= models.CharField(verbose_name="Accomplishment This FY - Physical", blank=True, max_length=500)
    accomplishmentToDate_physical= models.CharField(verbose_name="Accomplishment To Date - Physical", blank=True, max_length=500)
    ERAPlanThisMonth_financial = models.CharField(verbose_name="ERA Plan This Month - Financial", blank=True, max_length=500)
    ERAPlanThisQuarter_financial= models.CharField(verbose_name="ERA Plan This Quarter - Financial", blank=True, max_length=500)
    ERAPlanThisFY_financial= models.CharField(verbose_name="ERA Plan This FY - Financial", blank=True, max_length=500)
    ERAPlanToDate_financial= models.CharField(verbose_name="ERA Plan To Date - Financial", blank=True, max_length=500)
    accomplishmentThisMonth_financial = models.CharField(verbose_name="Accomplishment This Month - Financial", blank=True, max_length=500)
    accomplishmentThisQuarter_financial= models.CharField(verbose_name="Accomplishment This Quarter - Financial", blank=True, max_length=500)
    accomplishmentThisFY_financial= models.CharField(verbose_name="Accomplishment This FY - Financial", blank=True, max_length=500)
    accomplishmentToDate_financial= models.CharField(verbose_name="Accomplishment To Date - Financial", blank=True, max_length=500)
    IPCPaymentThisFY= models.CharField(verbose_name="IPC Payment This FY", blank=True, max_length=500)
    IPCPaymentToDate= models.CharField(verbose_name="IPC Payment To Date", blank=True, max_length=500)
    budgetAllocated_FY = models.CharField(verbose_name="Budget Allocated - FY", blank=True, max_length=500)
    environmentalSafetyAndOccupationalHealthManagementPlan= models.FileField(upload_to='project_documents/', blank=True,verbose_name="Environmental, Safety and Occupational Health Management Plan", validators=[validate_file])
    qualityAssurancePlan = models.FileField(upload_to='project_documents/',verbose_name="Quality Assurance Plan", blank=True, validators=[validate_file])
    approvedWorkProgram = models.CharField(verbose_name="Approved Work Program", blank=True, max_length=500)
    revisedWorkProgram= models.CharField(verbose_name="Revised Work Program", blank=True, max_length=500)
    financeSource_works= models.CharField(verbose_name="Finance Source - Works", blank=True, max_length=500)
    financeSource_services= models.CharField(verbose_name="Finance Source - Services", blank=True, max_length=500)
    majorProjectChallenges = models.CharField(verbose_name="Major Project Challenges", blank=True, max_length=500)
    quantityChangeAmount = models.CharField(verbose_name="Quantity Change Amount", blank=True, max_length=500)
    escalationAmount= models.CharField(verbose_name="Escalation Amount", blank=True, max_length=500)
    interestForLatePayment = models.CharField(verbose_name="Interest for Late Payment", blank=True, max_length=500)
    legslationCost = models.CharField(verbose_name="Legslation Cost", blank=True, max_length=500)
    costClaim = models.CharField(verbose_name="Cost Claim", blank=True, max_length=500)
    feeforDREService = models.CharField(verbose_name="Fee for DRE Service", blank=True, max_length=500)
    assignedTo = models.ForeignKey('authentication.Teams', on_delete=models.CASCADE ,max_length=200, verbose_name="Project Assigned To Team")
    assignedToLE = models.CharField(default="Lead Engineer",max_length=200, verbose_name="Project Assigned To Lead Engineer")
    assignedToPE = models.CharField(default="Project Engineer",max_length=200, verbose_name="Project Assigned To Project Engineer")
    dateAdded = models.DateTimeField(default=timezone.now,verbose_name="Date Added")
    lastEdit = models.DateTimeField(auto_now=True, verbose_name="Last Edit")
    author = models.CharField(max_length=400 ,verbose_name="Author")
    directorate = models.ForeignKey('authentication.Directorates', on_delete=models.CASCADE, max_length=200, verbose_name="Directorate")


    def __str__(self):
        return f'{self.projectName} '
    class Meta:
        verbose_name_plural = ("Projects")




class ProjectMessages(models.Model):
    project = models.ForeignKey('Projects', on_delete=models.CASCADE,verbose_name="Project")
    message = models.TextField(max_length=500, verbose_name="Message")
    dateSent = models.DateTimeField(default=timezone.now,verbose_name="Date Sent")
    author = models.CharField(max_length=400, default='User' ,verbose_name="Author")





    def __str__(self):
        return f'{self.project} '
    class Meta:
        verbose_name_plural = ("Project Messages")




class OtherProjectAttributes(models.Model):
    project = models.ForeignKey('Projects', on_delete=models.CASCADE,verbose_name="Project")
    attributeName = models.CharField(max_length=500, verbose_name="Attribute Name")
    data = models.CharField(max_length=500, verbose_name="Data")
    dateAdded = models.DateTimeField(default=timezone.now,verbose_name="Date Added")
    author = models.CharField(max_length=400, default='User' ,verbose_name="Author")


    def __str__(self):
        return f'{self.project} '
    class Meta:
        verbose_name_plural = ("Other Project Attributes")
