# Generated by Django 4.0 on 2021-12-31 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_system', '0016_doctor_patient_assigned_doctor_patient_assigned_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='X_ray_pictures',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]