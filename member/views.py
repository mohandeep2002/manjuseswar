from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


from member.models import Member

# Create your views here.
def login(request):
    #return HttpResponse("Hello")
    if request.method == "POST":
        emailid = request.POST.get('emailid')
        password = request.POST.get('password')
        member = Member.get_member_by_email(emailid)
        flag = Member.objects.filter(Q(emailid=emailid) & Q(password=password))
        print(flag)
        print(member)
        return HttpResponse("success")
    else:
        return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        print(111)
        emailid = request.POST.get('email')
        fullname = request.POST.get('firstname')
        
        password = request.POST.get('password')
        print(fullname, emailid, password)
        member = Member(fullname=fullname,
                        emailid=emailid,
                        password=password)
        member.register()   
        return HttpResponse("registered")
        
    return render(request, "signup.html")

