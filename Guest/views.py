from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *



def user_form(request):
    userData=tbl_user.objects.all()
    districtData=tbl_district.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_user_name')
        email=request.POST.get('txt_user_email')
        password=request.POST.get('txt_user_password')
        address=request.POST.get('txt_user_address')
        photo=request.FILES.get('txt_user_photo')
        proof=request.FILES.get('txt_user_proof')
        contact=request.POST.get('txt_user_contact')
      
        username=tbl_user.objects.filter(user_name=name).count()
        useremail=tbl_user.objects.filter(user_email=email).count()
        if username > 0:
            return render(request,'Guest/user.html',{'msg':"User Already Exists"})
        elif useremail > 0:
            return render(request,'Guest/user.html',{'msg':"User Email Already Exists"})
        else:
            tbl_user.objects.create(
                user_name=name,
                user_email=email,
                user_password=password,
                user_address=address,
                user_photo=photo,
                user_proof=proof,
                user_contact=contact,
            )
        
        return redirect('User:homepage')
    else:
        return render(request,'Guest/user.html',{'disdata':districtData})
    
def ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get('did'))
    return render(request,'Guest/ajaxplace.html',{'place':place})

def login(request):
    if request.method == "POST":
        email = request.POST.get('txt_user_email')
        password = request.POST.get('txt_user_password')
        
        
        admin_count = tbi_Admin.objects.filter(admin_Email=email, admin_Password=password).count()
        if admin_count > 0:
            admin = tbi_Admin.objects.get(admin_Email=email, admin_Password=password)
            request.session['admin_id'] = admin.id  
            intended_action = request.session.pop('intended_action', None)
            if intended_action == 'join_lobby':
                return redirect('Guest:login')
            elif intended_action == 'explore_communities':
                return redirect('Guest:login')
            return redirect('admin:adminPannel')  
        
        
        user_count = tbl_user.objects.filter(user_email=email, user_password=password).count()
        if user_count > 0:
            user = tbl_user.objects.get(user_email=email, user_password=password)
            request.session['uid'] = user.id
            user_data = user
            intended_action = request.session.pop('intended_action', None)
            if intended_action == 'join_lobby':
                return redirect('Guest:login')
            elif intended_action == 'explore_communities':
                return redirect('Guest:login')
            return redirect('User:homepage')
        
        mentor_count = tbl_mentor.objects.filter(mentor_email=email, mentor_password=password).count()
        if mentor_count > 0:
            mentor =tbl_mentor.objects.get(mentor_email=email, mentor_password=password)
            request.session['mid'] = mentor.id  
            intended_action = request.session.pop('intended_action', None)
            if intended_action == 'join_lobby':
                return redirect('Guest:login')
            elif intended_action == 'explore_communities':
                return redirect('Guest:login')
            return redirect('Mentor:homepage')   
        
        return render(request, 'Guest/login.html', {'msg': "Invalid credentials"})
    else:
        return render(request, 'Guest/login.html')
    
    
#functions for join_lobby and explore_communities

# def join_lobby(request):
#     # Check if user, mentor, or admin is logged in
#     if request.session.get('uid') or request.session.get('mid') or request.session.get('admin_id'):
#         return redirect('User:chatpage')
#     else:
#         request.session['intended_action'] = 'join_lobby'
#         return redirect('Guest:login')

# def explore_communities(request):
#     if request.session.get('uid') or request.session.get('mid') or request.session.get('admin_id'):
#         return redirect('User:communityView')
#     else:
#         request.session['intended_action'] = 'explore_communities'
#         return redirect('Guest:login')

def req_mentor(request):
    data=tbl_mentor.objects.all()
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        experience=request.POST.get('txt_experience')
        Job=request.POST.get('txt_jobTitle')
        password=request.POST.get('txt_password')
        photo=request.FILES.get('txt_mentor_photo')
        tbl_mentor.objects.create(mentor_name=name,
                                  mentor_email=email,
                                  mentor_experience=experience,
                                  mentor_jobTitle=Job,
                                  mentor_password=password,
                                  mentor_photo=photo)
        return redirect('Guest:login')
    else:
        return render(request , 'Guest/MentorRegistartion.html',{'data': data})
    
def index(request):
    return render(request,'Guest/index.html')



def userview(request):
    data=tbl_user.objects.all()
    return render(request, 'Guest/userview.html',{'data':data})

def logout(request):
    if 'uid' in request.session:
        del request.session['uid']
    if 'mid' in request.session:
        del request.session['mid']
    if 'admin_id' in request.session:
        del request.session['admin_id']
    return redirect('Guest:index')
