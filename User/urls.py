from django.urls import path
from User import views
app_name='User'

urlpatterns=[
    path('myprofile/',views.myprofile,name='myprofile'),
    path('homepage/',views.homepage,name='homepage'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changePassword/',views.changePassword,name='changePassword'),

    path('complaint/', views.complaint, name='complaint'),

    path('feedback/',views.FeedBack, name='feedback'),
    path('dlt_feedback/<int:did>',views.dlt_feedback,name='dlt_feedback'),
    path('edt_feedback/<int:eid>', views.edt_feedback,name='edt_feedback'),


    #lobby chat
    path('chatpage/',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    # path('ajaxphoto/',views.ajaxphoto,name="ajaxphoto"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('communityView/',views.communityView,name='communityView'),

    #communityChat

    path('communitychatpage/<int:id>',views.communitychatpage,name="communitychatpage"),
    path('communityajaxchat/',views.communityajaxchat,name="communityajaxchat"),
    path('communityajaxchatview/',views.communityajaxchatview,name="communityajaxchatview"),
    # path('ajaxphoto/',views.ajaxphoto,name="ajaxphoto"),
    path('communityclearchat/',views.communityclearchat,name="communityclearchat"),

    #payment path setting

    path('paymentCodeText/',views.paymentCodeText,name='paymentCodeText'),

    #findFriend

    path('findFriend/',views.findFriend,name='findFriend'),
    path('ajax_search_user/', views.ajax_search_user, name='ajax_search_user'),
    
    path('notification/', views.notification_list, name='notification'),
    path('send_friend_request/', views.send_friend_request, name='send_friend_request'),
    path('handle_notification/', views.handle_notification, name='handle_notification'),


    path('dmchatpage/<int:id>',views.dmchatpage,name="dmchatpage"),
    path('dmajaxchat/',views.dmajaxchat,name="dmajaxchat"),
    path('dmajaxchatview/',views.dmajaxchatview,name="dmajaxchatview"),
    # path('ajaxphoto/',views.ajaxphoto,name="ajaxphoto"),
    path('dmclearchat/',views.dmclearchat,name="dmclearchat"),

]