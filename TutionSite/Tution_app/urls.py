
from .views import home, about, tutor, student, contact

from django.urls import path,include

app_name = 'Tution_app'

urlpatterns = [

    path('',home,name="home"),
    path('about',about,name="about"),
    path('tutor',tutor,name="tutor"),
    path('student',student,name="student"),
    path('contact',contact,name="contact"),



]
