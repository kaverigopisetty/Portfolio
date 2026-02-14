from django.urls import path
from app1 import views
urlpatterns=[
    path('',views.home),
    path('about/',views.about, name='about'),
    path('experience/',views.experience, name='experience'),
    path('education/',views.education, name='education'),
    path('contact/',views.contact, name='contact'),
    path('project/',views.about, name='project'),

]