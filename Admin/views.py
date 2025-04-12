from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from Guest.models import *

def district(request):
    districtA=tbl_district.objects.all()
    if request.method=='POST':
        tbl_district.objects.create(district_name= request.POST.get('txt_district'))
        return redirect('admin:district')
    else:
        return render(request,'Admin/district.html',{'a':districtA})


   #delete district 
def delete_district(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('admin:district')


#edit district 
def edit_district(request, did):
    temp_district=tbl_district.objects.get(id=did)
 
    if request.method=='POST':
        temp_district.district_name=request.POST.get('txt_district')
        temp_district.save()
        return redirect('admin:district')
    else:
        return render(request,'admin/district.html',{'edit_var':temp_district})

def Admin_reg(request):
    reg=tbi_Admin.objects.all()
    if request.method=='POST':
        tbi_Admin.objects.create(
            admin_Name=request.POST.get('txt_admin_name'),
            admin_Contact=request.POST.get('txt_admin_contact'),
            admin_Email=request.POST.get('txt_admin_email'),
            admin_Password=request.POST.get('txt_admin_password'),
            )
        return redirect('admin:Admin_reg')
    else:
         return render(request,'Admin/Adminregistrationform.html',{'b':reg})
    

def Place(request):
    districtData=tbl_district.objects.all()
    data = tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txt_place')
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=placeName,district=dis)
        return render(request,"Admin/Place.html",{'data':data})
    else:
        return render(request,'Admin/place.html',{"districtData":districtData})

# table for category file 


def category(request):
    categoryData=tbl_category.objects.all()
    if request.method=="POST":
        tbl_category.objects.create(category_name= request.POST.get('txt_category'))
        return redirect('admin:category')
    else:
        return render(request,"Admin/category.html",{'categoryData':categoryData})
    

    #  "sub_categoryData" (a varible use to take data from the table (tbl_sub_category))
    # "sub_cat" (a varible use to take data from the table (tbl_category))
    # ""
def sub_cat(request):
    sub_categoryData=tbl_subcategory.objects.all()
    cate=tbl_category.objects.all()
    if request.method=="POST":
        sub_Category_name=request.POST.get('txt_sub_category')
        cat=tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_subcategory.objects.create(subcategory_name=sub_Category_name,category=cat)
        return redirect('admin:sub_cat')
    else:
        return render(request,"Admin/sub_category.html",{'sub_category':sub_categoryData,'cate':cate})
    
def delete_subcat(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return redirect("admin:sub_cat")

def edit_subcat(request,eid):
     edit_var=tbl_subcategory.objects.get(id=eid)
     cate=tbl_category.objects.all()
     if request.method=="POST":
        edit_var.subcategory_name=request.POST.get('txt_sub_category')
        edit_var.save()
        return redirect("admin:sub_cat")
     else:
        return render(request,"admin/sub_category.html",{'editvar':edit_var,'cate':cate})
     
#compalint replay

def complaint_replay(request,cid):
    data=tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        data.complaint_replay=request.POST.get("txt_replay")
        data.complaint_status=1
        data.save()
        return redirect("admin:complaint_view")
    else:
        return render(request, 'admin/replay.html')

def complaint_view(request):
    compalint=tbl_complaint.objects.all()
    return render(request , 'admin/view_complaint.html', {'comp':compalint})


#community 
    
def community_data(request):
    data=tbl_community.objects.all()
    if request.method=="POST":
        tbl_community.objects.create(community_name=request.POST.get('txt_community'),
                                     community_discription=request.POST.get('txt_discription'))
        return redirect('admin:community')
    else:
        return render(request , 'admin/community.html',{'data': data})


def dlt_community(request,did):
    tbl_community.objects.get(id=did).delete()
    return redirect("admin:community")

def edt_community(request,eid):
    data=tbl_community.objects.get(id=eid)
    if request.method=="POST":
        data.community_name=request.POST.get('txt_community')
        data.community_discription=request.POST.get('txt_discription')
        data.save(update_fields=['community_name', 'community_discription'])
        return redirect("admin:community")   
    else:
        return  render(request , 'admin/community.html' , {'c_data':data}) 
            
def dlt_mentor(request,did):
    tbl_mentor.objects.get(id=did).delete()
    return redirect('admin:m_reg')
 
#view community

def viewcommunity(request):
    data=tbl_community.objects.all()
    return render(request, 'admin/viewcommunity.html',{'data':data})

#add mentor

def addmentor(request,id):
    data=tbl_community_mentor.objects.all()
    mentor=tbl_mentor.objects.all()
    community=tbl_community.objects.get(id=id)
    if request.method=="POST":
        mentor=tbl_mentor.objects.get(id=request.POST.get('sel_mentor'))
        tbl_community_mentor.objects.create(mentor=mentor,community=community)
        return redirect("admin:v_community")
    else:
        return render(request,'admin/addmentor.html',{'mentor':mentor,'data':data})
def editmentor(request,id): 
    mentor=tbl_mentor.objects.all()
    men=tbl_community_mentor.objects.get(id=id)
    if request.method=="POST":
        men.mentor=tbl_mentor.objects.get(id=request.POST.get('sel_mentor'))
        men.save()
        return redirect("admin:v_community")
    else:
        return render(request,'admin/addmentor.html',{'editmentor':men,'mentor':mentor})  

def feedback(request):
    feedback=tbl_feedback.objects.all()
    if request.method=="POST":
        return redirect("admin:viewfeedback")
    else:
        return render(request, 'admin/viewfeedback.html', {'data':feedback})

#admin pannel

def adminPannel(request):
    return render(request, 'admin/adminPannel.html')

def mentorView(request):
    data=tbl_mentor.objects.all()
    return render(request, 'admin/MentorView.html' ,{'data':data})

def viewcommunitymentor(request,id):
    mentor=tbl_community_mentor.objects.filter(mentor=id)
    return render(request,'admin/viewcommunity.html',{'mentor':mentor})
