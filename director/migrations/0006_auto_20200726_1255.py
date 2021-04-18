# Generated by Django 3.0.3 on 2020-07-26 09:55

import director.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0005_projects_lastedit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='ERAPlanThisFY_financial',
            field=models.CharField(blank=True, max_length=500, verbose_name='ERA Plan This FY - Financial'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='ERAPlanThisFY_physical',
            field=models.CharField(blank=True, max_length=500, verbose_name='ERA Plan This FY - Physical'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='ERAPlanThisMonth_financial',
            field=models.CharField(blank=True, max_length=500, verbose_name='ERA Plan This Month - Financial'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='ERAPlanThisMonth_physical',
            field=models.CharField(blank=True, max_length=500, verbose_name='ERA Plan This Month - Physical'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='ERAPlanThisQuarter_financial',
            field=models.CharField(blank=True, max_length=500, verbose_name='ERA Plan This Quarter - Financial'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='ERAPlanThisQuarter_physical',
            field=models.CharField(blank=True, max_length=500, verbose_name='ERA Plan This Quarter - Physical'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='ERAPlanToDate_financial',
            field=models.CharField(blank=True, max_length=500, verbose_name='ERA Plan To Date - Financial'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='ERAPlanToDate_physical',
            field=models.CharField(blank=True, max_length=500, verbose_name='ERA Plan To Date - Physical'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='IPCPaymentThisFY',
            field=models.CharField(blank=True, max_length=500, verbose_name='IPC Payment This FY'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='IPCPaymentToDate',
            field=models.CharField(blank=True, max_length=500, verbose_name='IPC Payment To Date'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='accomplishmentThisFY_financial',
            field=models.CharField(blank=True, max_length=500, verbose_name='Accomplishment This FY - Financial'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='accomplishmentThisFY_physical',
            field=models.CharField(blank=True, max_length=500, verbose_name='Accomplishment This FY - Physical'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='accomplishmentThisMonth_financial',
            field=models.CharField(blank=True, max_length=500, verbose_name='Accomplishment This Month - Financial'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='accomplishmentThisMonth_physical',
            field=models.CharField(blank=True, max_length=500, verbose_name='Accomplishment This Month - Physical'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='accomplishmentThisQuarter_financial',
            field=models.CharField(blank=True, max_length=500, verbose_name='Accomplishment This Quarter - Financial'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='accomplishmentThisQuarter_physical',
            field=models.CharField(blank=True, max_length=500, verbose_name='Accomplishment This Quarter - Physical'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='accomplishmentToDate_financial',
            field=models.CharField(blank=True, max_length=500, verbose_name='Accomplishment To Date - Financial'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='accomplishmentToDate_physical',
            field=models.CharField(blank=True, max_length=500, verbose_name='Accomplishment To Date - Physical'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='approvedWorkProgram',
            field=models.CharField(blank=True, max_length=500, verbose_name='Approved Work Program'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='budgetAllocated_FY',
            field=models.CharField(blank=True, max_length=500, verbose_name='Budget Allocated - FY'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='contractType',
            field=models.CharField(blank=True, max_length=500, verbose_name='Contract Type'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='costClaim',
            field=models.CharField(blank=True, max_length=500, verbose_name='Cost Claim'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='designControlPoints',
            field=models.CharField(blank=True, max_length=500, verbose_name='Design Control Points'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='designStandard',
            field=models.CharField(blank=True, max_length=500, verbose_name='Design Standard'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='environmentalSafetyAndOccupationalHealthManagementPlan',
            field=models.FileField(blank=True, upload_to='project_documents/', validators=[director.models.validate_file], verbose_name='Environmental, Safety and Occupational Health Management Plan'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='escalationAmount',
            field=models.CharField(blank=True, max_length=500, verbose_name='Escalation Amount'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='expectedProjectCompletionDate',
            field=models.DateField(blank=True, max_length=500, verbose_name='Expected Project Completion Date'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='extentionOfTime_amount',
            field=models.CharField(blank=True, max_length=500, verbose_name='Extention of Time - Amount'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='extentionOfTime_approvalDate',
            field=models.DateField(blank=True, max_length=500, verbose_name='Extention of Time - Approval Date'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='extentionOfTime_number',
            field=models.CharField(blank=True, max_length=500, verbose_name='Extention of Time - Number'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='extentionOfTime_reason',
            field=models.CharField(blank=True, max_length=500, verbose_name='Extention of Time- Reason'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='feeforDREService',
            field=models.CharField(blank=True, max_length=500, verbose_name='Fee for DRE Service'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='financeSource_services',
            field=models.CharField(blank=True, max_length=500, verbose_name='Finance Source - Services'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='financeSource_works',
            field=models.CharField(blank=True, max_length=500, verbose_name='Finance Source - Works'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='interestForLatePayment',
            field=models.CharField(blank=True, max_length=500, verbose_name='Interest for Late Payment'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='legslationCost',
            field=models.CharField(blank=True, max_length=500, verbose_name='Legslation Cost'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='location_region',
            field=models.CharField(blank=True, max_length=500, verbose_name='Location - Region'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='location_woreda',
            field=models.CharField(blank=True, max_length=500, verbose_name='Location - Woreda'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='location_zone',
            field=models.CharField(blank=True, max_length=500, verbose_name='Location - Zone'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='majorProjectChallenges',
            field=models.CharField(blank=True, max_length=500, verbose_name='Major Project Challenges'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projectEndPoint_easting',
            field=models.CharField(blank=True, max_length=500, verbose_name='Project End Point - Easting'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projectEndPoint_northing',
            field=models.CharField(blank=True, max_length=500, verbose_name='Project End Point - Northing'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projectLength',
            field=models.CharField(blank=True, max_length=500, verbose_name='Project Length'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projectStartPoint_easting',
            field=models.CharField(blank=True, max_length=500, verbose_name='Project Start Point - Easting'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projectStartPoint_northing',
            field=models.CharField(blank=True, max_length=500, verbose_name='Project Start Point - Northing'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='qualityAssurancePlan',
            field=models.FileField(blank=True, upload_to='project_documents/', validators=[director.models.validate_file], verbose_name='Quality Assurance Plan'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='quantityChangeAmount',
            field=models.CharField(blank=True, max_length=500, verbose_name='Quantity Change Amount'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='revisedWorkProgram',
            field=models.CharField(blank=True, max_length=500, verbose_name='Revised Work Program'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='roadSurfaceType',
            field=models.CharField(blank=True, max_length=500, verbose_name='Road Surface Type'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='servicesContractAmount',
            field=models.CharField(blank=True, max_length=500, verbose_name='Services Contract Amount'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='servicesContractCommencementDate',
            field=models.DateField(blank=True, max_length=500, verbose_name='Services Contract Commencement Date'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='servicesContractCompletionDate_original',
            field=models.DateField(blank=True, max_length=500, verbose_name='Services Contract Completion Date - Original'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='servicesContractCompletionDate_revised',
            field=models.DateField(blank=True, max_length=500, verbose_name='Services Contract Completion Date - Revised'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='servicesContractSigningDate',
            field=models.DateField(blank=True, max_length=100, verbose_name='Services Contract Signing Date'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='startPointDistancefromAA',
            field=models.CharField(blank=True, max_length=500, verbose_name='Start Point Distance from AA'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='variationOrders_amount',
            field=models.CharField(blank=True, max_length=500, verbose_name='Variation Orders - Amount'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='variationOrders_approvalDate',
            field=models.DateField(blank=True, max_length=500, verbose_name='Variation Orders - Approval Date'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='variationOrders_number',
            field=models.CharField(blank=True, max_length=500, verbose_name='Variation Orders - Number'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='variationOrders_reason',
            field=models.CharField(blank=True, max_length=500, verbose_name='Variation Orders - Reason'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='worksContractAmount_original',
            field=models.CharField(blank=True, max_length=500, verbose_name='Works Contract Amount - Original'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='worksContractAmount_revised',
            field=models.CharField(blank=True, max_length=500, verbose_name='Works Contract Amount - Revised'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='worksContractCommencementDate',
            field=models.DateField(blank=True, max_length=100, verbose_name='Works Contract Commencement Date'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='worksContractCompletionDate_original',
            field=models.DateField(blank=True, max_length=500, verbose_name='Works Contract Completion Date - Original'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='worksContractCompletionDate_revised',
            field=models.DateField(blank=True, max_length=500, verbose_name='Works Contract Completion Date - Revised'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='worksContractSigningDate',
            field=models.DateField(blank=True, max_length=100, null=True, verbose_name='Works Contract Signing Date'),
        ),
    ]
