# Generated by Django 4.0 on 2021-12-31 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_system', '0009_alter_nursingsupervision_responsible_group_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nurses',
            name='Id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
