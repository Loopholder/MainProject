from django.db import models
from Admin.models import *

class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_email=models.CharField(max_length=30)
    user_password=models.CharField(max_length=30)
    user_address=models.CharField(max_length=30)
    user_photo=models.FileField(upload_to='Assets/Files/User')
    user_proof=models.FileField(upload_to='Assets/Files/User')
    user_contact=models.CharField(max_length=30)
    

class tbl_mentor(models.Model):
    mentor_name=models.CharField(max_length=30)
    mentor_email=models.CharField(max_length=30)
    mentor_password=models.CharField(max_length=30)
    mentor_experience=models.CharField(max_length=30)
    mentor_jobTitle=models.CharField(max_length=30)
    mentor_status=models.IntegerField(default=0)
    mentor_photo=models.FileField(upload_to='Assets/Files/Mentor')

