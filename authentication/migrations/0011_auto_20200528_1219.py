# Generated by Django 3.0.3 on 2020-05-28 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20200528_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilePicture',
            field=models.ImageField(default='Profile_Pictures/default.png', upload_to='Profile_Pictures/', verbose_name='Profile Picture'),
        ),
    ]
