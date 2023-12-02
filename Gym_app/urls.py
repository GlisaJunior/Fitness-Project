from django.urls import path
from . import views

urlpatterns = [
    path('homepage', views.homepage, name='homepage'),
    path('blog', views.blog, name='blog'),
    path('workouts', views.workouts, name='workouts'),
    path('instructors', views.instructors, name='instructors'),
    path('timetable', views.timetable, name='timetable'),
    path('gym_and_more', views.gym_and_more, name='gym_and_more'),
    path('webshop', views.webshop, name='webshop'),
    path('contact', views.contact, name='contact'),

    path('sign_up', views.sign_up, name='sign_up'),
    path('log_in', views.log_in, name='log_in'),

    path('member_account', views.member_account, name='member_account'),
    path('instructor_profile', views.instructor_profile, name='instructor_profile'),

    path('admin_instructors', views.admin_instructors, name='admin_instructors'),
    path('admin_workouts', views.admin_workouts, name='admin_workouts'),
    path('admin_members', views.admin_members, name='admin_members'),
    path('admin_mailbox', views.admin_mailbox, name='admin_mailbox'),
]