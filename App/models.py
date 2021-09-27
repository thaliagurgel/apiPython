from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)

class Companies (models.Model):
    CompanyID = models.AutoField(primary_key=True)
    CompanyName = models.CharField(max_length=100)
    CompanyCNPJ = models.CharField(max_length=20)
    CompanyDepartment = models.CharField(max_length=50)
    CompanyAdress = models.CharField(max_length=100)
    CompanyPhone = models.CharField(max_length=20)
    PhotoFileName = models.CharField(max_length=100)