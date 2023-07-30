from django.contrib import admin
from demoapp.models import employee
# Register your models here.
class employeeadmin(admin.ModelAdmin):
    emp_admin=['empNo','empName','empAddress']
admin.site.register(employee,employeeadmin)