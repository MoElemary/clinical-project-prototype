# Generated by Django 4.0 on 2021-12-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration_system', '0003_nursingteam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nursingteam',
            name='group_number',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
