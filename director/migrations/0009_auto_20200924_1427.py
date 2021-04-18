# Generated by Django 3.0.3 on 2020-09-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('director', '0008_auto_20200924_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='expectedProjectCompletionDate',
            field=models.DateField(blank=True, max_length=500, verbose_name='Expected Project Completion Date'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='extentionOfTime_approvalDate',
            field=models.DateField(blank=True, max_length=500, verbose_name='Extention of Time - Approval Date'),
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
            name='variationOrders_approvalDate',
            field=models.DateField(blank=True, max_length=500, verbose_name='Variation Orders - Approval Date'),
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
