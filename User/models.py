from django.db import models
from Admin.models import *
from Guest.models import *



class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=30)
    complaint_content=models.CharField(max_length=30)
    complaint_replay=models.CharField(max_length=30)
    complaint_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    complaint_date=models.DateField(auto_now_add=True)

class tbl_feedback(models.Model):
    fb_content=models.CharField(max_length=30)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    fb_date=models.DateField(auto_now_add=True)

class tbl_lobby(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    
class tbl_communitychat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user = models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    community = models.ForeignKey(tbl_community,on_delete=models.CASCADE,null=True)

class tbl_dm(models.Model):
    dm_from=models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="dm_from")
    dm_to=models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="dm_to")
    dm_message=models.CharField(max_length=30)
    dm_status=models.IntegerField(default=0)
    dm_date_time=models.DateTimeField(auto_now_add=True)
    dm_photo=models.FileField(upload_to='ChatFiels/')
    dm_files=models.FileField(upload_to='ChatFiels/')

