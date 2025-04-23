from django.db import models
from Admin.models import *
from Guest.models import *
from django.db.models import Q




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
    mentor=models.ForeignKey(tbl_mentor,on_delete=models.CASCADE,null=True)
    community = models.ForeignKey(tbl_community,on_delete=models.CASCADE,null=True)

# class tbl_dm(models.Model):
#     dm_from=models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="dm_from")
#     dm_to=models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="dm_to")
#     dm_message=models.CharField(max_length=30)
#     dm_status=models.IntegerField(default=0)
#     dm_date_time=models.DateTimeField(auto_now_add=True)
#     dm_photo=models.FileField(upload_to='ChatFiels/')
#     dm_files=models.FileField(upload_to='ChatFiels/')

class tbl_dm(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_fromd")
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_tod")

class tbl_notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE, related_name='notifications')  
    from_user = models.ForeignKey(tbl_user, on_delete=models.CASCADE, related_name='sent_requests', null=True, blank=True) 
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)  

class tbl_friend(models.Model):
    user1 = models.ForeignKey(tbl_user, on_delete=models.CASCADE, related_name='friends1', null=True)
    user2 = models.ForeignKey(tbl_user, on_delete=models.CASCADE, related_name='friends2', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    friend_status = models.IntegerField(default=0)  # 0=pending, 1=accepted, 2=rejected
