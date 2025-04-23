from django.urls import path
from Mentor import views
app_name='Mentor'

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('changePassword/',views.changePassword,name="changePassword"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('mentorcommunity',views.mentorcommunity,name='mentorcommunity'),

     path('communitychatpage/<int:id>',views.communitychatpage,name="communitychatpage"),
    path('communityajaxchat/',views.communityajaxchat,name="communityajaxchat"),
    path('communityajaxchatview/',views.communityajaxchatview,name="communityajaxchatview"),
    path('communityclearchat/',views.communityclearchat,name="communityclearchat"),
]