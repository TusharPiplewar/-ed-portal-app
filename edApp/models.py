from django.db import models
#from django_countries import CountryField
from django_countries.fields import CountryField
# Create your models here.
class edsystango(models.Model):
    name=models.CharField(max_length=60)
    description=models.TextField(max_length=200)

class ClassesForm(models.Model):
    nameofclass=models.CharField(max_length=60)
    monthlyfees=models.IntegerField(max_length=20)

class InstituteForm(models.Model):
    Yourinstituename=models.CharField(max_length=60)
    Targetline=models.CharField(max_length=60)
    Institutelogo=models.FileField(upload_to='images/')
    Phone=models.CharField(max_length=12)
    Website=models.CharField(max_length=60)
    Address=models.CharField(max_length=60)
    country = CountryField(blank_label='(select country)')

class rulesForm(models.Model):
    description=models.TextField(max_length=500)


class feesForm(models.Model):
    Admissionfee=models.CharField(max_length=60)
    Registrationfee=models.IntegerField(max_length=20)
    Art_material=models.CharField(max_length=60)
    Transport=models.CharField(max_length=60)
    Books=models.CharField(max_length=60)
    Uniform=models.CharField(max_length=60)
    Fine=models.CharField(max_length=60)
    Others=models.CharField(max_length=60)
