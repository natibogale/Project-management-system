# Generated by Django 3.0.3 on 2020-10-14 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recordOfficer', '0016_teamleaderslettermessagesout_teamleadersmemomessages_teamleadersmemomessagesout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamleadersmemomessagesout',
            name='subject',
            field=models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='recordOfficer.OutgoingMemos', verbose_name='Subject'),
        ),
    ]
