# Generated by Django 3.0.3 on 2020-04-04 10:12

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directorates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directorates', models.CharField(max_length=500)),
                ('director', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Directorates',
            },
        ),
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default=django.contrib.auth.models.User, max_length=400)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectName', models.CharField(max_length=600)),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='OutgoingMemos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(verbose_name='Subject')),
                ('dateWritten', models.DateField(verbose_name='Date Written')),
                ('signatore', models.CharField(max_length=400, verbose_name='Signatore')),
                ('cc', models.CharField(max_length=400, verbose_name='CC')),
                ('pageNumber', models.PositiveIntegerField(verbose_name='Page Number')),
                ('author', models.CharField(default=django.contrib.auth.models.User, max_length=400, verbose_name='Author')),
                ('dateAdded', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Added')),
                ('lastEdit', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last Edit')),
                ('lastEditBy', models.CharField(default=django.contrib.auth.models.User, max_length=400, verbose_name='Last Edit By')),
                ('file', models.FileField(upload_to='outgoing_documents/', verbose_name='File')),
                ('directorate', models.CharField(max_length=200, verbose_name='Directorate')),
                ('seen', models.CharField(default='false', max_length=200, verbose_name='Seen')),
                ('level', models.PositiveIntegerField(default=1, verbose_name='Level')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordOfficer.Projects', verbose_name='Project')),
                ('sentTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordOfficer.Directorates', verbose_name='Sent To')),
            ],
            options={
                'verbose_name_plural': 'Outgoing Memos',
            },
        ),
        migrations.CreateModel(
            name='OutgoingLetters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(verbose_name='Subject')),
                ('referenceNumber', models.TextField(unique=True, verbose_name='Reference Number')),
                ('dateWritten', models.DateField(verbose_name='Date Written')),
                ('dateDelivered', models.DateField(verbose_name='Date Received')),
                ('signatore', models.CharField(max_length=400, verbose_name='Signatore')),
                ('sentTo', models.CharField(max_length=400, verbose_name='Sent To')),
                ('cc', models.CharField(max_length=400, verbose_name='CC')),
                ('type', models.CharField(choices=[('Claim/Vo', 'Claim/Vo'), ('Correspondence', 'Correspondence'), ('Report', 'Report'), ('Payment', 'Payment'), ('Row Document', 'Row Document')], max_length=100, verbose_name='Type')),
                ('pageNumber', models.PositiveIntegerField(verbose_name='Page Number')),
                ('author', models.CharField(default=django.contrib.auth.models.User, max_length=400, verbose_name='Author')),
                ('dateAdded', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Added')),
                ('lastEdit', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last Edit')),
                ('lastEditBy', models.CharField(default=django.contrib.auth.models.User, max_length=400, verbose_name='Last Edit By')),
                ('file', models.FileField(upload_to='outgoing_documents/', verbose_name='File')),
                ('directorate', models.CharField(max_length=200, verbose_name='Directorate')),
                ('seen', models.CharField(default='false', max_length=200, verbose_name='Seen')),
                ('level', models.PositiveIntegerField(default=1, verbose_name='Level')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordOfficer.Projects', verbose_name='Project')),
            ],
            options={
                'verbose_name_plural': 'Outgoing Letters',
            },
        ),
        migrations.CreateModel(
            name='IncomingMemos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(verbose_name='Subject')),
                ('dateWritten', models.DateField(verbose_name='Date Written')),
                ('signatore', models.CharField(max_length=400, verbose_name='Signatore')),
                ('cc', models.CharField(max_length=400, verbose_name='CC')),
                ('pageNumber', models.PositiveIntegerField(verbose_name='Page Number')),
                ('author', models.CharField(default=django.contrib.auth.models.User, max_length=400, verbose_name='Author')),
                ('dateAdded', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Added')),
                ('lastEdit', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last Edit')),
                ('lastEditBy', models.CharField(default=django.contrib.auth.models.User, max_length=400, verbose_name='Last Edit By')),
                ('file', models.FileField(upload_to='incoming_documents/', verbose_name='File')),
                ('directorate', models.CharField(max_length=200, verbose_name='Directorate')),
                ('seen', models.CharField(default='false', max_length=200, verbose_name='Seen')),
                ('level', models.PositiveIntegerField(default=1, verbose_name='Level')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordOfficer.Projects', verbose_name='Project')),
                ('receivedFrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordOfficer.Directorates', verbose_name='Received From')),
            ],
            options={
                'verbose_name_plural': 'Incoming Memos',
            },
        ),
        migrations.CreateModel(
            name='IncomingLetters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(verbose_name='Subject')),
                ('referenceNumber', models.TextField(unique=True, verbose_name='Reference Number')),
                ('dateWritten', models.DateField(verbose_name='Date Written')),
                ('dateReceived', models.DateField(verbose_name='Date Received')),
                ('signatore', models.CharField(max_length=400, verbose_name='Signatore')),
                ('receivedFrom', models.CharField(max_length=400, verbose_name='Received From')),
                ('cc', models.CharField(max_length=400, verbose_name='CC')),
                ('type', models.CharField(choices=[('Claim/Vo', 'Claim/Vo'), ('Correspondence', 'Correspondence'), ('Report', 'Report'), ('Payment', 'Payment'), ('Row Document', 'Row Document')], max_length=100, verbose_name='Type')),
                ('pageNumber', models.PositiveIntegerField(verbose_name='Page Number')),
                ('author', models.CharField(default=django.contrib.auth.models.User, max_length=400, verbose_name='Author')),
                ('dateAdded', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date Added')),
                ('lastEdit', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last Edit')),
                ('lastEditBy', models.CharField(default=django.contrib.auth.models.User, max_length=400, verbose_name='Last Edit By')),
                ('file', models.FileField(upload_to='incoming_documents/', verbose_name='File')),
                ('directorate', models.CharField(max_length=200, verbose_name='Directorate')),
                ('seen', models.CharField(default='false', max_length=200, verbose_name='Seen')),
                ('level', models.PositiveIntegerField(default=1, verbose_name='Level')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recordOfficer.Projects', verbose_name='Project')),
            ],
            options={
                'verbose_name_plural': 'Incoming Letters',
            },
        ),
    ]
