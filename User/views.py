from django.shortcuts import render,redirect
from User.models import *
from Guest.models import *
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def myprofile(request):
    profileData=tbl_user.objects.get(id=request.session['uid'])
    return render (request,'User/myprofile.html',{'profileData':profileData})

def homepage(request):
    # Check if user is logged in
    if 'uid' in request.session:
        user_data = tbl_user.objects.get(id=request.session['uid'])
        return render(request, 'User/homepage.html', {'user_data': user_data})
    else:
        # If not logged in, redirect to login page
        return redirect('Guest:login')

def editprofile(request):
    editData=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        username=tbl_user.objects.filter(user_name=request.POST.get('txt_user_name')).count()
        useremail=tbl_user.objects.filter(user_email=request.POST.get('txt_user_email')).count()
        if username > 0:
            return render(request,'User/editprofile.html',{'editData':editData,'msg':"User Already Exists"})
        elif useremail > 0:
            return render(request,'User/editprofile.html',{'editData':editData,'msg':"User Email Already Exists"})
        else:
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
    user_data = tbl_user.objects.get(id=request.session['uid'])
    comp = tbl_complaint.objects.all()
    if request.method=="POST":
        title = request.POST.get("txt_user_title")
        content = request.POST.get("txt_user_content")
        tbl_complaint.objects.create(complaint_title=title, complaint_content=content, user=user_data)
        return redirect('User:complaint')
    else:
        return render(request, 'User/complaint.html', {'complaint': comp, 'user_data': user_data})
    

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


#findFriend

def notification_list(request):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    user = tbl_user.objects.get(id=request.session['uid'])
    notifications = tbl_notification.objects.filter(user=user).order_by('-date')
    return render(request, 'User/notification.html', {'notifications': notifications})

def findFriend(request):
    user_data = tbl_user.objects.get(id=request.session['uid'])
    # Find all accepted friends (friend_status=1)
    friends = tbl_friend.objects.filter(
        (Q(user1=user_data) | Q(user2=user_data)) & Q(friend_status=1)
    )
    # Build a list of the friend user objects (the other user in the pair)
    contacts = []
    for f in friends:
        if f.user1 == user_data:
            contacts.append(f.user2)
        else:
            contacts.append(f.user1)
    # Find users who accepted MY request (I sent, they accepted)
    accepted_by_others = tbl_notification.objects.filter(from_user=user_data, status=1).select_related('user')
    accepted_users = [n.user for n in accepted_by_others]
    return render(request, 'User/findFriend.html', {'user_data': user_data, 'contacts': contacts, 'accepted_users': accepted_users})

from django.http import JsonResponse
from django.db.models import Q

def ajax_search_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user_profile = tbl_user.objects.get(user_name=username)
            already_requested = False
            if 'uid' in request.session:
                me = tbl_user.objects.get(id=request.session['uid'])
                already_requested = tbl_notification.objects.filter(user=user_profile, from_user=me, status=0).exists()
            return render(request, 'User/search_user_result.html', {'user_found': True, 'user_profile': user_profile, 'already_requested': already_requested})
        except tbl_user.DoesNotExist:
            return render(request, 'User/search_user_result.html', {'user_found': False})
    return render(request, 'User/search_user_result.html', {'user_found': False})

def send_friend_request(request):
    if request.method == 'POST' and 'uid' in request.session:
        from_user = tbl_user.objects.get(id=request.session['uid'])
        to_user_id = request.POST.get('to_user_id')
        try:
            to_user = tbl_user.objects.get(id=to_user_id)
            if tbl_notification.objects.filter(user=to_user, from_user=from_user, status=0).exists():
                return JsonResponse({'success': False, 'msg': 'Request already sent.'})
            tbl_notification.objects.create(user=to_user, from_user=from_user, status=0)
            return JsonResponse({'success': True, 'msg': 'Friend request sent!'})
        except tbl_user.DoesNotExist:
            return JsonResponse({'success': False, 'msg': 'User does not exist.'})
    return JsonResponse({'success': False, 'msg': 'Invalid request.'})

def handle_notification(request):
    if request.method == 'POST' and 'uid' in request.session:
        notif_id = request.POST.get('notification_id')
        action = request.POST.get('action')
        try:
            notif = tbl_notification.objects.get(notification_id=notif_id, user_id=request.session['uid'], status=0)
            
            if action == 'accept':
                notif.status = 1  # Update status to 1 for accept
                notif.save()
                return JsonResponse({'success': True, 'msg': 'Friend request accepted.'})
            
            elif action == 'reject':
                notif.status = 2  # Update status to 2 for reject
                notif.save()
                return JsonResponse({'success': True, 'msg': 'Friend request rejected.'})
                
        except tbl_notification.DoesNotExist:
            return JsonResponse({'success': False, 'msg': 'Notification not found.'})
    return JsonResponse({'success': False, 'msg': 'Invalid request.'})

def notification_list(request):
    if 'uid' not in request.session:
        return redirect('Guest:login')
    user = tbl_user.objects.get(id=request.session['uid'])
    notifications = tbl_notification.objects.filter(user=user, status=0).order_by('-date')
    return render(request, 'User/notification.html', {'notifications': notifications})

def dmchatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"User/DmChat.html",{"user":user})

def dmajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_dm.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"User/DmChat.html")

def dmajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_dm.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"User/DmChatView.html",{"data":chat_data,"tid":int(tid)})

def dmclearchat(request):
    tbl_dm.objects.filter(Q(user_from=request.session["uid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"User/DmClearChat.html",{"msg":"Chat Deleted Sucessfully...."})