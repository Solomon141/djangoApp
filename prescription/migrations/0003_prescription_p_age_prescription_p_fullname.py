# Generated by Django 4.2.7 on 2023-11-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0002_prescription_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='p_age',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='p_fullname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
