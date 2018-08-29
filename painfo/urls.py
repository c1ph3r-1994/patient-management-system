from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login, logout
urlpatterns = [
   # url(r'^new_form/$', views.FileFieldView.as_view(), name='new_form'),
    url(r'^new_form/$', views.paform, name='new_form'),
    url(r'^home/$', views.home, name='index'),
    url(r'login/$',login,{'template_name':'painfo/login.html'}),
    url(r'logout/$',logout,{'template_name':'painfo/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^edit/$', views.edit_profile, name='change_password'),
    url(r'^patient_information/$', views.showp, name='show_patient_detail'),
    url(r'^edit_information/\d', views.edit_details, name='show_patient_details'),
    url(r'^searchpa/$', views.searchpa, name='show_patient'),
    url(r'^deletepa/$', views.deletepa, name='delete_patient'),
    url(r'^patient_information/\d', views.user_information, name='user_information'),
    url(r'^add_ipno/\d', views.add_ipno, name='Add_ipno'),
    url(r'^patient_photo/', views.patient_photo, name='Add_ipno'),
    url(r'^patient_information/delete_ipno/\d', views.delete_pa, name='delete_patient'),
    url(r'^ipno/add/', views.patient_photo_add, name='Add_doc'),
    url(r'^ipno/edit/', views.patient_photo_edit, name='edit_ipno'),
    url(r'^ipno/delete/', views.patient_photo_delete, name='delete_doc'),
    url(r'^patient_info_ipno/$', views.patient_ipno, name='patient_ipno'),
    url(r'^datesearch/$', views.datesearch, name='datesearch'),
    url(r'^typesearch/$', views.typesearch, name='typesearch'),
]
