# Generated by Django 3.2.7 on 2021-09-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('CompanyID', models.AutoField(primary_key=True, serialize=False)),
                ('CompanyName', models.CharField(max_length=100)),
                ('CompanyCNPJ', models.CharField(max_length=20)),
                ('CompanyDepartment', models.CharField(max_length=50)),
                ('CompanyAdress', models.CharField(max_length=100)),
                ('CompanyPhone', models.CharField(max_length=20)),
                ('PhotoFileName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('DepartmentId', models.AutoField(primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=100)),
            ],
        ),
    ]