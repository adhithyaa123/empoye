from django.db import models

# Create your models here.

class Employees(models.Model):

    name=models.CharField(max_length=200,null=True)

    designation=models.CharField(max_length=200,null=True)

    department=models.CharField(max_length=200,null=True)

    salary=models.IntegerField(null=True)

    contact=models.CharField(max_length=200,null=True)

    address=models.CharField(max_length=200,null=True)


