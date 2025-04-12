from django.urls import path
from Admin import views
app_name='admin'

urlpatterns = [
    path('district/',views.district,name='district'),
    path('Admin_Registration/',views.Admin_reg,name='Admin_reg'),
    path('delete_district/<int:did>',views.delete_district,name='delete_district'),
    path('edit_district/<int:did>',views.edit_district,name='edit_district'),
    path('Place',views.Place,name='Place'),
    path('category',views.category,name='category'),
    path('sub_cat/',views.sub_cat,name='sub_cat'),
    path('delete_subcat/<int:did>',views.delete_subcat,name="delete_subcat"),
    path('edit_subcategory/<int:eid>' ,views.edit_subcat,name="edit_subcat"),
    path('complaint_replay/<int:cid>',views.complaint_replay,name='complaint_replay'),
    path('view_complaints/',views.complaint_view,name='complaint_view'),
    path('community/' , views.community_data,name='community'),
    path('edit_community_name/<int:eid>',views.edt_community, name='edt_community'),
    path('delete_community_name/<int:did>',views.dlt_community, name='dlt_community'),
    path('dlt_mentor/<int:did>',views.dlt_mentor,name='dlt_mentor'),
    path('viewcommunity/',views.viewcommunity,name='v_community'),
    path('addmentor/<int:id>',views.addmentor,name='addmentor'),
    path('editmentor/<int:id>',views.editmentor,name='editmentor'),
    path('viewfeedback/',views.feedback, name="viewfeedback"),
    path('adminPannel/',views.adminPannel,name='adminPannel'),
    path('mentorView/',views.mentorView,name="mentorView"),
    path('viewcommunitymentor/<int:id>',views.viewcommunitymentor,name="viewcommunitymentor")

]