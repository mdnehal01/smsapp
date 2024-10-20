from django.shortcuts import render, redirect
from . models import Enquiry, AdminLogin
import datetime
from django.core.exceptions import ObjectDoesNotExist
from adminapp.models import Teacher,Student

# Create your views here.
def index(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

def contact(req):
    if req.method=="POST":
        name=req.POST['name']
        gender=req.POST['gender']
        address=req.POST['address']
        contactno=req.POST['contactno']
        emailaddress=req.POST['emailaddress']
        enquirytext=req.POST['enquirytext']
        enquirydate=datetime.datetime.today()
        enq=Enquiry(name=name,gender=gender,address=address,contactno=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
        enq.save()
        msg="Your enquiry is submitted successfully"
        return render(req,'contact.html',{'msg':msg})
    return render(req, 'contact.html')

def login(req):
    return render(req,'login.html')

def logcode(req):
    if req.method=="POST":
        usertype=req.POST['usertype']
        userid=req.POST['userid']
        password=req.POST['password']
        if usertype=="admin":
            try:
                user=AdminLogin.objects.get(userid=userid,password=password)
                if user is not None:
                    req.session['adminid']=userid
                    return redirect('adminapp:adminhome')
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'Invalid User'})
        elif usertype=="teacher":
            try:
                teacher=Teacher.objects.get(emailaddress=userid,password=password)
                if teacher is not None:
                    req.session['teacherid']=userid
                    return redirect('teacherapp:teacherhome')
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'Invalid User'})
        elif usertype=="student":
            try:
                student=Student.objects.get(emailaddress=userid,password=password)
                if student is not None:
                    req.session['studentid']=userid
                    return redirect('studentapp:studenthome')
            except ObjectDoesNotExist:
                return render(req,'login.html',{'msg':'Invalid User'})

        
        
