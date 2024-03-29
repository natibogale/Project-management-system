# Generated by Django 3.0.3 on 2020-07-05 07:31

import director.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0011_auto_20200528_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=500, verbose_name='Project Name')),
                ('contractorName', models.CharField(max_length=500, verbose_name="Contractor's Name")),
                ('consultantName', models.CharField(max_length=500, verbose_name="Consultant's Name")),
                ('worksContractAmount_original', models.CharField(max_length=500, verbose_name='Works Contract Amount - Original')),
                ('worksContractAmount_revised', models.CharField(max_length=500, verbose_name='Works Contract Amount - Revised')),
                ('contractType', models.CharField(max_length=500, verbose_name='Contract Type')),
                ('roadSurfaceType', models.CharField(max_length=500, verbose_name='Road Surface Type')),
                ('designStandard', models.CharField(max_length=500, verbose_name='Design Standard')),
                ('location_region', models.CharField(max_length=500, verbose_name='Location - Region')),
                ('location_zone', models.CharField(max_length=500, verbose_name='Location - Zone')),
                ('location_woreda', models.CharField(max_length=500, verbose_name='Location - Woreda')),
                ('designControlPoints', models.CharField(max_length=500, verbose_name='Design Control Points')),
                ('worksContractSigningDate', models.DateField(max_length=100, verbose_name='Works Contract Signing Date')),
                ('worksContractCommencementDate', models.DateField(max_length=100, verbose_name='Works Contract Commencement Date')),
                ('worksContractCompletionDate_original', models.DateField(max_length=500, verbose_name='Works Contract Completion Date - Original')),
                ('worksContractCompletionDate_revised', models.DateField(max_length=500, verbose_name='Works Contract Completion Date - Revised')),
                ('servicesContractSigningDate', models.DateField(max_length=100, verbose_name='Services Contract Signing Date')),
                ('servicesContractAmount', models.CharField(max_length=500, verbose_name='Services Contract Amount')),
                ('servicesContractCommencementDate', models.DateField(max_length=500, verbose_name='Services Contract Commencement Date')),
                ('servicesContractCompletionDate_original', models.DateField(max_length=500, verbose_name='Services Contract Completion Date - Original')),
                ('servicesContractCompletionDate_revised', models.DateField(max_length=500, verbose_name='Services Contract Completion Date - Revised')),
                ('expectedProjectCompletionDate', models.DateField(max_length=500, verbose_name='Expected Project Completion Date')),
                ('projectStartPoint_easting', models.CharField(max_length=500, verbose_name='Project Start Point - Easting')),
                ('projectStartPoint_northing', models.CharField(max_length=500, verbose_name='Project Start Point - Northing')),
                ('projectEndPoint_easting', models.CharField(max_length=500, verbose_name='Project End Point - Easting')),
                ('projectEndPoint_northing', models.CharField(max_length=500, verbose_name='Project End Point - Northing')),
                ('startPointDistancefromAA', models.CharField(max_length=500, verbose_name='Start Point Distance from AA')),
                ('projectLength', models.CharField(max_length=500, verbose_name='Project Length')),
                ('variationOrders_number', models.CharField(max_length=500, verbose_name='Variation Orders - Number')),
                ('variationOrders_amount', models.CharField(max_length=500, verbose_name='Variation Orders - Amount')),
                ('variationOrders_approvalDate', models.DateField(max_length=500, verbose_name='Variation Orders - Approval Date')),
                ('variationOrders_reason', models.CharField(max_length=500, verbose_name='Variation Orders - Reason')),
                ('extentionOfTime_number', models.CharField(max_length=500, verbose_name='Extention of Time - Number')),
                ('extentionOfTime_amount', models.CharField(max_length=500, verbose_name='Extention of Time - Amount')),
                ('extentionOfTime_approvalDate', models.DateField(max_length=500, verbose_name='Extention of Time - Approval Date')),
                ('extentionOfTime_reason', models.CharField(max_length=500, verbose_name='Extention of Time- Reason')),
                ('ERAPlanThisMonth_physical', models.CharField(max_length=500, verbose_name='ERA Plan This Month - Physical')),
                ('ERAPlanThisQuarter_physical', models.CharField(max_length=500, verbose_name='ERA Plan This Quarter - Physical')),
                ('ERAPlanThisFY_physical', models.CharField(max_length=500, verbose_name='ERA Plan This FY - Physical')),
                ('ERAPlanToDate_physical', models.CharField(max_length=500, verbose_name='ERA Plan To Date - Physical')),
                ('accomplishmentThisMonth_physical', models.CharField(max_length=500, verbose_name='Accomplishment This Month - Physical')),
                ('accomplishmentThisQuarter_physical', models.CharField(max_length=500, verbose_name='Accomplishment This Quarter - Physical')),
                ('accomplishmentThisFY_physical', models.CharField(max_length=500, verbose_name='Accomplishment This FY - Physical')),
                ('accomplishmentToDate_physical', models.CharField(max_length=500, verbose_name='Accomplishment To Date - Physical')),
                ('ERAPlanThisMonth_financial', models.CharField(max_length=500, verbose_name='ERA Plan This Month - Financial')),
                ('ERAPlanThisQuarter_financial', models.CharField(max_length=500, verbose_name='ERA Plan This Quarter - Financial')),
                ('ERAPlanThisFY_financial', models.CharField(max_length=500, verbose_name='ERA Plan This FY - Financial')),
                ('ERAPlanToDate_financial', models.CharField(max_length=500, verbose_name='ERA Plan To Date - Financial')),
                ('accomplishmentThisMonth_financial', models.CharField(max_length=500, verbose_name='Accomplishment This Month - Financial')),
                ('accomplishmentThisQuarter_financial', models.CharField(max_length=500, verbose_name='Accomplishment This Quarter - Financial')),
                ('accomplishmentThisFY_financial', models.CharField(max_length=500, verbose_name='Accomplishment This FY - Financial')),
                ('accomplishmentToDate_financial', models.CharField(max_length=500, verbose_name='Accomplishment To Date - Financial')),
                ('IPCPaymentThisFY', models.CharField(max_length=500, verbose_name='IPC Payment This FY')),
                ('IPCPaymentToDate', models.CharField(max_length=500, verbose_name='IPC Payment To Date')),
                ('budgetAllocated_FY', models.CharField(max_length=500, verbose_name='Budget Allocated - FY')),
                ('environmentalSafetyAndOccupationalHealthManagementPlan', models.FileField(upload_to='project_documents/', validators=[director.models.validate_file], verbose_name='Environmental, Safety and Occupational Health Management Plan')),
                ('qualityAssurancePlan', models.FileField(upload_to='project_documents/', validators=[director.models.validate_file], verbose_name='Quality Assurance Plan')),
                ('approvedWorkProgram', models.CharField(max_length=500, verbose_name='Approved Work Program')),
                ('revisedWorkProgram', models.CharField(max_length=500, verbose_name='Revised Work Program')),
                ('financeSource_works', models.CharField(max_length=500, verbose_name='Finance Source - Works')),
                ('financeSource_services', models.CharField(max_length=500, verbose_name='Finance Source - Services')),
                ('majorProjectChallenges', models.CharField(max_length=500, verbose_name='Major Project Challenges')),
                ('quantityChangeAmount', models.CharField(max_length=500, verbose_name='Quantity Change Amount')),
                ('escalationAmount', models.CharField(max_length=500, verbose_name='Escalation Amount')),
                ('interestForLatePayment', models.CharField(max_length=500, verbose_name='Interest for Late Payment')),
                ('legslationCost', models.CharField(max_length=500, verbose_name='Legslation Cost')),
                ('costClaim', models.CharField(max_length=500, verbose_name='Cost Claim')),
                ('feeforDREService', models.CharField(max_length=500, verbose_name='Fee for DRE Service')),
                ('author', models.CharField(default='User', max_length=400, verbose_name='Author')),
                ('dateAdded', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Added')),
                ('assignedTo', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='authentication.Teams', verbose_name='Project Assigned To')),
                ('directorate', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='authentication.Directorates', verbose_name='Directorate')),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectMessages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=500, verbose_name='Message')),
                ('dateSent', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Sent')),
                ('author', models.CharField(default='User', max_length=400, verbose_name='Author')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='director.Projects', verbose_name='Project')),
            ],
            options={
                'verbose_name_plural': 'Project Messages',
            },
        ),
        migrations.CreateModel(
            name='OtherProjectAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attributeName', models.CharField(max_length=500, verbose_name='Attribute Name')),
                ('data', models.CharField(max_length=500, verbose_name='Data')),
                ('dateAdded', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Added')),
                ('author', models.CharField(default='User', max_length=400, verbose_name='Author')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='director.Projects', verbose_name='Project')),
            ],
            options={
                'verbose_name_plural': 'Other Project Attributes',
            },
        ),
    ]
