from django.shortcuts import render,redirect
from User.models import *
from Guest.models import *
from datetime import datetime
from django.db.models import Q
def myprofile(request):
    profileData=tbl_user.objects.get(id=request.session['uid'])
    return render (request,'User/myprofile.html',{'profileData':profileData})

def homepage(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    return render (request,'User/homepage.html',{'data':data})

def editprofile(request):
    editData=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        editData.user_name=request.POST.get('txt_user_name')
        editData.user_email=request.POST.get('txt_user_email')
        editData.user_contact=request.POST.get('txt_user_contact')
        editData.user_address=request.POST.get('txt_user_address')
        editData.save()
        return redirect('User:myprofile')
    else:
        return render (request,'User/editprofile.html',{'editData':editData})
    
def changePassword(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        old=request.POST.get('txt_user_oldp')
        new=request.POST.get('txt_user_newp')
        confirm=request.POST.get('txt_user_conp')
        if user.user_password==old:
            if new==confirm:
                user.user_password=new
                user.save()
                return redirect('User:myprofile')
            else:
                return render (request,'User/changepassword.html',{'msg':"Password Mismatch"})
        else:
            return render (request,'User/changepassword.html',{'msg':"Password Invalid"})
    else:
        return render (request,'User/changepassword.html')
    

#complaint

def complaint(request):
    comp=tbl_complaint.objects.all()
    if request.method=="POST":
        title=request.POST.get("txt_user_title")
        content=request.POST.get("txt_user_content")
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content, user=tbl_user.objects.get(id=request.session["uid"]))

        return redirect('User:complaint')
    else:
        return render(request,'User/complaint.html',{'complaint':comp})
    

#feedback
    
def FeedBack(request):
    fb=tbl_feedback.objects.all()
    if request.method=="POST":
        content=request.POST.get("txt_content")
        tbl_feedback.objects.create(fb_content=content,user=tbl_user.objects.get(id=request.session['uid']))
        return redirect('User:feedback')
    else:
        return render(request , 'User/feedback.html',{'feed':fb})
        
#delete_feedback

def dlt_feedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect('User:feedback')

def edt_feedback(request,eid):
    temp_data=tbl_feedback.objects.get(id=eid)
    if request.method=="POST":
        temp_data.fb_content=request.POST.get("txt_content")
        temp_data.save()
        return redirect('User:feedback')
    else:
        return render(request, 'User/feedback.html',{'td':temp_data})

#lobby chat function 

def chatpage(request):
    user  = tbl_user.objects.get(id=request.session['uid'])
    return render(request,"User/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    # to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_lobby.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user=from_user,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    # tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_lobby.objects.all().order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,'user':user})

def clearchat(request):
    tbl_lobby.objects.filter(Q(user=request.session["uid"])).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})





# def chatpage(request):
#     """Render the chat page with user details."""
#     user = tbl_user.objects.get(id=request.session['uid'])
#     users = tbl_user.objects.exclude(id=user.id)  # Fetch all users except the current user
#     return render(request, "User/Chat.html", {"user": user, "users": users})

# def ajaxchat(request):
#     """Handle new chat messages, store text and files."""
#     user = tbl_user.objects.get(id=request.session["uid"])
#     tbl_lobby.objects.create(
#         chat_content=request.POST.get("msg"),
#         chat_time=datetime.now(),
#         chat_file=request.FILES.get("file"),
#         user=user  # Associate the message with the user
#     )
#     return render(request, "User/Chat.html")

# def ajaxchatview(request):
#     """Retrieve all messages for the group chat."""
#     chat_data = tbl_lobby.objects.all().order_by('chat_time')  # Fetch all group messages
#     return render(request, "User/ChatView.html", {"data": chat_data})

# def clearchat(request):
#     """Clears all messages from the group chat."""
#     tbl_lobby.objects.all().delete()  # Delete all messages
#     return render(request, "User/ClearChat.html", {"msg": "Group chat cleared successfully."})



def communityView(request):
    data=tbl_community.objects.all()
    return render(request, 'User/communityView.html',{'data':data})


# community chat functions

def communitychatpage(request,id):
    user  = tbl_community.objects.get(id=id)
    mentor=tbl_community_mentor.objects.filter(community=user)

    return render(request,"User/communityChat.html",{"user":user,'mentor':mentor})

def communityajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_community = tbl_community.objects.get(id=request.POST.get("tid"))
    tbl_communitychat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user=from_user,community=to_community,chat_file=request.FILES.get("file"))
    return render(request,"User/communityChat.html")

def communityajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_communitychat.objects.filter(community=tid).order_by('chat_time')
    return render(request,"User/communityChatView.html",{"data":chat_data,'user':user})

def communityclearchat(request):
    tbl_communitychat.objects.filter(Q(user=request.session["uid"])).delete()
    return render(request,"User/communityClearChat.html",{"msg":"Chat Deleted Sucessfully...."})

#payment functions

def paymentCodeText(request):
     return render('User/paymentCodeText.html')