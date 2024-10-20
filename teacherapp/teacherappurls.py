from django.urls import path
from . import views

# teacher app urls
urlpatterns = [
    path('teacherapp/',views.teacherhome,name='teacherhome'),
    path('teacherprofile/',views.teacherprofile,name='teacherprofile'),
    path('uploadpic/',views.uploadpic,name='uploadpic'),
    path('tchangepass/',views.tchangepass,name='tchangepass'),
    path('teacherlogout/',views.teacherlogout,name='teacherlogout'),
    path('addattend/',views.addattend,name='addattend'),
    path('viewattend/',views.viewattend,name='viewattend'),
]