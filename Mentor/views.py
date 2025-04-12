from django.shortcuts import render ,redirect
from Admin.models import *


def homepage(request):
    return render(request,'Mentor/Homepage.html')

def myprofile(request):
    myprofile=tbl_mentor.objects.get(id=request.session['mid'])
    return render(request,'Mentor/Myprofile.html',{'myprofile':myprofile})

def editprofile(request):
    editData=tbl_mentor.objects.get(id=request.session['mid'])
    if request.method=="POST":
        editData.mentor_name=request.POST.get('txt_name')
        editData.mentor_email=request.POST.get('txt_email')
        editData.mentor_jobTitle=request.POST.get('txt_jobtitle')
        editData.mentor_experience=request.POST.get('txt_experience')
        editData.save()
        return redirect('Mentor:myprofile')
    else:
        return render (request,'Mentor/Editprofile.html',{'editData':editData})
    
def changePassword(request):
    mentor=tbl_mentor.objects.get(id=request.session['mid'])
    if request.method=="POST":
        old=request.POST.get('txt_user_oldp')
        new=request.POST.get('txt_user_newp')
        confirm=request.POST.get('txt_user_conp')
        if mentor.mentor_password==old:
            if new==confirm:
                mentor.mentor_password=new
                mentor.save()
                return redirect('Guest:login')
            else:
                return render (request,'Mentor/changepassword.html',{'msg':"Password Mismatch"})
        else:
            return render (request,'Mentor/changepassword.html',{'msg':"Password Invalid"})
    else:
        return render (request,'Mentor/changepassword.html')

