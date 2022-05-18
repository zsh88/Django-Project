from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

#Define class --> Table into Relational Database 
class Department(models.Model):
    title = models.CharField(max_length=30)

class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)

class User_log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=200, default="")
    cur_date_time = models.DateTimeField(default=datetime.now)
    

# Create your models here.

