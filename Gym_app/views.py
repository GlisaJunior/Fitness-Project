from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def homepage (request):
    return render(request, 'homepage.html')

def blog (request):
    return render(request, 'blog.html')

def workouts (request):
    return render(request, 'workouts.html')

def instructors (request):
    return render(request, 'instructors.html')

def timetable (request):
    return render(request, 'timetable.html')

def gym_and_more (request):
    return render(request, 'gym_and_more.html')

def webshop (request):
    return render(request, 'webshop.html')

def contact (request):
    return render(request, 'contact.html')



def sign_up (request):
    return render(request, 'sign_up.html')

def log_in (request):
    return render(request, 'log_in.html')



def member_account (request):
    return render(request, 'member_account.html')

def instructor_profile (request):
    return render(request, 'instructor_profile.html')



def admin_instructors (request):
    return render(request, 'admin_instructors.html')

def admin_workouts (request):
    return render(request, 'admin_workouts.html')

def admin_members (request):
    return render(request, 'admin_members.html')

def admin_mailbox (request):
    return render(request, 'admin_mailbox.html')
