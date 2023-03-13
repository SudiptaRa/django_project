from django.db import models

# Create your models here.
# class Employee(models.Model):
#     empid=models.IntegerField()
#     empname=models.CharField(max_length=70)
#     empemail=models.EmailField(max_length=70)
#     emppassword=models.CharField(max_length=70)

class Employee_table(models.Model):
    id = models.AutoField(primary_key=True)
    empid=models.CharField(max_length=70,null=False)
    empname=models.CharField(max_length=70,default='(empty)')
    empemail=models.EmailField(max_length=70,default='Empty@xyz.com')
    emppassword=models.CharField(max_length=70,default='(empty)')
    empexp=models.IntegerField(default=0)
    

