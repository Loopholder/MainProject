from django.db import models
from Guest.models import *


class tbl_district(models.Model):
    district_name= models.CharField(max_length=30)


class tbi_Admin(models.Model):
    admin_Name=models.CharField(max_length=30)
    admin_Contact=models.CharField(max_length=30)
    admin_Email=models.CharField(max_length=30)
    admin_Password=models.CharField(max_length=30)

#table for place.html (page)

class tbl_place(models.Model):
     place_name=models.CharField(max_length=50)
     district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=30)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=30)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_community(models.Model):
    community_name=models.CharField(max_length=30)
    community_discription=models.CharField(max_length=30)
    community_Date=models.DateField(auto_now_add=True)
    community_status=models.IntegerField(default=0)




class tbl_community_mentor(models.Model):
    mentor=models.ForeignKey(tbl_mentor,on_delete=models.CASCADE)
    community=models.ForeignKey(tbl_community,on_delete=models.CASCADE)
    community_mentor_status=models.IntegerField(default=0)



