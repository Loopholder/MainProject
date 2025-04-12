from django.urls import path
from Guest import views
app_name='Guest'

urlpatterns = [
    path('user_form/',views.user_form,name='user_form'),
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
    path('login/',views.login,name="login"),
    path('',views.index, name='index'),
    path('userview/',views.userview,name='userview'),
    path('mentor/',views.req_mentor,name='m_reg'),
]