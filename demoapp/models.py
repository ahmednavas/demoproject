from django.db import models

# Create your models here.
class employee(models.Model):
    empNo=models.IntegerField()
    empName=models.CharField(max_length=30)
    empAddress=models.CharField(max_length=50)
def __str__(self,empName):
    return 'employee'+empName