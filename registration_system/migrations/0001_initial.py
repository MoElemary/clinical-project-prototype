# Generated by Django 4.0 on 2021-12-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nurses',
            fields=[
                ('Id', models.BigAutoField(primary_key=True, serialize=False)),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('group_number', models.IntegerField()),
                ('Supervisor', models.CharField(max_length=50)),
                ('Assigned_Room', models.IntegerField()),
                ('Assigned_Patient', models.CharField(max_length=50)),
            ],
        ),
    ]
