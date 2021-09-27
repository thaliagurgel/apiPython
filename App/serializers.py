from rest_framework import serializers
from App.models import Departments, Companies

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                  'DepartmentName')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ('CompanyID',
                'CompanyName',
                'CompanyCNPJ',
                'CompanyDepartment',
                'CompanyAdress',
                'CompanyPhone' ,
                'PhotoFileName' )