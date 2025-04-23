from django.shortcuts import render ,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from datetime import datetime
from django.db.models import Q


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


def mentorcommunity(request):
    data=tbl_mentor.objects.get(id=request.session['mid'])
    dataCommunity=tbl_community_mentor.objects.filter(mentor=data)
    return render(request, 'Mentor/mentorcommunity.html', {'dataCommunity': dataCommunity})


def communitychatpage(request,id):
    user  = tbl_community.objects.get(id=id)
    mentor=tbl_community_mentor.objects.filter(community=user)

    return render(request,"Mentor/communityChat.html",{"user":user,'mentor':mentor})

def communityajaxchat(request):
    from_mentor = tbl_mentor.objects.get(id=request.session["mid"])
    to_community = tbl_community.objects.get(id=request.POST.get("tid"))
    tbl_communitychat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),mentor=from_mentor,community=to_community,chat_file=request.FILES.get("file"))
    return render(request,"Mentor/communityChat.html")

def communityajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_mentor.objects.get(id=request.session["mid"])
    chat_data = tbl_communitychat.objects.filter(community=tid).order_by('chat_time')
    return render(request,"Mentor/communityChatView.html",{"data":chat_data,'user':user})

def communityclearchat(request):
    tbl_communitychat.objects.filter(Q(mentor=request.session["mid"])).delete()
    return render(request,"Mentor/communityClearChat.html",{"msg":"Chat Deleted Sucessfully...."})