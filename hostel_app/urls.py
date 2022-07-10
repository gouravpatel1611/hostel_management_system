from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('admin_login/', views.admin_login, name='admin_login'),
    path('newadmin',views.newadmin, name='newadmin'),
    path('addadmin',views.addadmin, name='addadmin'),
    path('check_admin_pass/', views.check_admin_pass, name='check_admin_pass'),

    path('student_login/', views.student_login, name='warden_login'),
    path('newstudent',views.newstudent, name='newstudent'),
    path('addstudent',views.addstudent, name='addstudent'),
    path('check_student_pass', views.check_student_pass, name='check_student_pass'),


    path('guard_login/', views.guard_login, name='warden_login'),
    path('newguard',views.newguard, name='newguard'),
    path('addguard',views.addguard, name='addguard'),
    path('check_guard_pass', views.check_guard_pass, name='check_guard_pass'),

    path('admin_profile', views.admin_profile, name='admin_profile'),
    path('student_profile', views.student_profile, name='student_profile'),
    path('guard_profile', views.guard_profile, name='guard_profile'),
    
    path('change_password', views.change_password, name='change_password'),
    path('changed', views.changed, name='changed'),

    path('uname_gatepass', views.uname_gatepass, name='uname_gatepass'),
    path('gatepass', views.gatepass, name='gatepass'),
    path('gatepass_issue', views.gatepass_issue, name='gatepass_issue'),
    path('forget_pass', views.forget_pass, name='forget_pass'),
    path('forgeted', views.forgeted, name='forgeted'),
    




    path('scan_for_outing', views.scan_for_outing, name='scan_for_outing'),

    path('check_qr', views.check_qr, name='check_qr'),



]
