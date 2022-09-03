import datetime
from tempfile import tempdir
from venv import create
from django.shortcuts import redirect, render

from AdhyanApp.views import review
from .models import *
from AdhyanApp import models as m
from django.conf import settings
from django.core.mail import send_mail

import random as r
# Create your views here.


def pdfviewer(request,pk):
    index=Add_Index.objects.get(id=pk)
    uid=Register.objects.get(email=request.session['adminemail'])
    return render(request,'pdf-viewer.html',{'uid':uid,'index':index})

def showadmin(request,pk):
    uid=Register.objects.get(email=request.session['adminemail'])
    user=Register.objects.get(id=pk)
    course=All_Course.objects.filter(uid=user).count
    enq_co=m.Enquiry.objects.all().count
    review=Review.objects.filter(course__uid=user).count
    purchase=Booking.objects.filter(course__uid=user,pay_verify=True).count
    return render(request,'showadmin.html',{'uid':uid,'u':user,'tcourse':course,'tenq':enq_co,'treview':review,'tpurchase':purchase})

def aindex(request):
    uid=Register.objects.get(email=request.session['adminemail'])
    enq=m.Enquiry.objects.all()[::-1][0:5]
    review=Review.objects.all()[::-1][0:5]
    treview=Review.objects.all().count
    admin=Register.objects.all()
    enq_co=m.Enquiry.objects.all().count
    course=All_Course.objects.all().count
    student=User.objects.all().count
    pay=Booking.objects.filter(pay_verify=True).count
    allstudent=User.objects.all()[::-1][0:4]
    allcourse=All_Course.objects.all()
    adminco=All_Course.objects.filter(uid=uid).count
    purchase=Booking.objects.filter(course__uid=uid,pay_verify=True).count
    return render(request,'aindex.html',{'adminco':adminco,'purchase':purchase,'uid':uid,'enq':enq,'enq_co':enq_co,'course':course,'student':student,'admin':admin,'allstudent':allstudent,'allcourse':allcourse,'pay':pay,'review':review,'treview':treview})

    # return render(request,'aindex.html',{'uid':uid,'enq':enq})
def signin(request):
    try:
        uid=Register.objects.get(email=request.session['adminemail'])
        return redirect('aindex')
    except:
        # global nowtime
        if request.method=='POST':
            try:
                uid=Register.objects.get(email=request.POST['email'])
                if uid.password==request.POST['password']:
                    request.session['adminemail']=uid.email
                    return redirect('aindex')
                return render(request,'signin.html',{'msg':'Password is incorrect'})
            except:
                return render(request,'signup.html',{'msg':'Email is not registered'})
        return render(request,'signin.html')
def signup(request):
    if request.method=='POST':
        try:
            Register.objects.get(email=request.POST['email'])
            return render(request,'signup.html',{'msg':'Email is alrady register.'})
        except:
            if request.POST['password']==request.POST['cpassword']:
                global temp
                temp={
                    'name':request.POST['name'],
                    'mobile':request.POST['mobile'],
                    'gender':request.POST['gender'],
                    'email':request.POST['email'],
                    'address':request.POST['address'],
                    'password':request.POST['password'],
                }
                otp = r.randrange(100000,999999)
                subject = 'welcome to Adhyan.'
                message = f'Your otp is {otp} .Please Enter valid Otp'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'aotp.html',{'otp':otp})
            return render(request,'signup.html',{'msg':'Both passwords are not matched'})
    return render(request,'signup.html')
def aotp(request):
    if request.method=='POST':
        if request.POST['uotp'] == request.POST['otp']:
            global temp
            Register.objects.create(
                name=temp['name'],
                mobile=temp['mobile'],
                gender=temp['gender'],
                email=temp['email'],
                address=temp['address'],
                password=temp['password'],
            )
            msg='Account is Created'
            return render(request,'signin.html',{'msg': msg})
        return render(request,'aotp.html',{'otp':request.POST['otp'],'msg':'incorrect OTP'})
def alogout(request):
    del request.session['adminemail']
    return redirect('signin')

def aforgot(request):
    admin=Register.objects.all()
    if request.method=='POST':
        uid=Register.objects.get(email=request.POST['email'])
        if uid.email==request.POST['email']:
            s1="abcdefghijklmnopqrstuvwxyz"
            s2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            s3="0123456789"
            s4=".@"
            s=s1+s2+s3+s4
            fpass = "".join(r.sample(s,8))
            subject = 'Forgot Password For Adhyan Id'
            message = f'Your new Password is {fpass} .Please Enter This Password for signin'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'fpass.html',{'fpass':fpass,'Email':uid.email,'msg':'See in Your Email id Your Password is Sent','admin':admin})
        return render(request,'forgot-password.html',{'msg':'Email Is not Register','admin':admin})
    return render(request,'forgot-password.html',{'admin':admin})


def passwordrecovery(request):
    uid=Register.objects.get(email=request.session['adminemail'])
    if request.method=='POST':
        if uid.password == request.POST['opassword']:
            if request.POST['npassword'] == request.POST['cpassword']:
                uid.password = request.POST['npassword']
                uid.save()
                return redirect('aindex')
            return render(request,'password-recovery.html',{'msg':'Both Password Are not Matched '})
        return render(request,'password-recovery.html',{'msg':'Old Password is not Matched '})
    return render(request,'password-recovery.html')

def fpass(request):
    try:
        uid=Register.objects.get(email=request.session['adminemail'])
        return redirect('aindex')
    except:
        if request.method=='POST':
            try:
                uid=Register.objects.get(email=request.POST['email'])
                if request.POST['password']==request.POST['fpass']:
                    uid.password=request.POST['fpass']
                    uid.save()
                    request.session['adminemail']=uid.email
                    return redirect('aindex')
                return render(request,'fpass.html',{'msg':'Password is incorrect'})
            except:
                return render(request,'signup.html',{'msg':'Email is not registered'})
        return render(request,'fpass.html')
def myprofile(request):
    uid=Register.objects.get(email=request.session['adminemail'])
    if request.method=='POST':
        uid.name=request.POST['name']
        uid.mobile=request.POST['mobile']
        uid.address=request.POST['address']
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        uid.save()
        return render(request,'my-profile.html',{'uid':uid,'msg':'Profile is Updated','nowtime':datetime.datetime.now()})
    return render(request,'my-profile.html',{'uid':uid})


def addcourse(request):
    co=Department.objects.all()
    uid=Register.objects.get(email=request.session['adminemail'])
    if request.method=='POST':
        try:
            course=All_Course.objects.get(coname=request.POST['coname'])
            msg = f'Course is already in list and status is {course.verify}'
            return render(request,'add-course.html',{'uid':uid,'msg':msg})
        except:  
            dept=Department.objects.get(name=request.POST['codepartment'])
            All_Course.objects.create(
                uid = uid,
                coname=request.POST['coname'],
                coduration=request.POST['coduration'],
                coprice=request.POST['coprice'],
                codepartment=dept,
                copic=request.FILES['copic'],
                codiscription=request.POST['codiscription'],
                coyear=request.POST['coyear'],
            )
            msg = 'Course is added'
            return render(request,'add-course.html',{'uid':uid,'msg':msg,'co':co})
    return render(request,'add-course.html',{'uid':uid,'co':co})

def editcourse(request,pk):
    dept = Department.objects.all()
    uid=Register.objects.get(email=request.session['adminemail'])
    co=All_Course.objects.get(id=pk)
    if request.method=='POST':
        depts=Department.objects.get(name=request.POST['codepartment'])
        co.coname=request.POST['coname']
        co.coduration=request.POST['coduration']
        co.coprice=request.POST['coprice']
        co.codepartment=depts
        co.codiscription=request.POST['codiscription']
        co.coyear=request.POST['coyear']
        if 'copic' in request.FILES:
            co.copic=request.FILES['copic']
        co.save()
        msg='Course is Edited'
        return render(request,'edit-course.html',{'dept':dept,'uid':uid,'co':co,'msg':msg})
    return render(request,'edit-course.html',{'dept':dept,'uid':uid,'co':co})


def editdepartment(request,pk):
    dept = Department.objects.get(id=pk)
    uid=Register.objects.get(email=request.session['adminemail'])
    if request.method=='POST':
        dept.name=request.POST['name']
        dept.headdepartment=request.POST['headdepartment']
        dept.email=request.POST['email']
        dept.mobile=request.POST['phone']
        dept.no_of_student=request.POST['noofstudent']
        if 'date' in request.POST:
            dept.dep_date=request.POST['date']
        dept.save()
    return render(request,'edit-department.html',{'uid':uid,'dept':dept})

def editindex(request,pk):
    index = Add_Index.objects.get(id=pk)
    uid=Register.objects.get(email=request.session['adminemail'])
    course=All_Course.objects.all()
    if request.method=='POST':
        index.topic=request.POST['topic']
        if 'material' in request.FILES:
            course.material=request.FILES['material']
    msg='Index Is Edited'
    return render(request,'edit-index.html',{'uid':uid,'index':index,'msg':msg})

def deletedepartment(request,pk):
    dept = Department.objects.get(id=pk)
    dept.delete()
    return redirect(department)

def courseinfo(request,pk):
    uid=Register.objects.get(email=request.session['adminemail'])
    co=All_Course.objects.get(id=pk)
    index=Add_Index.objects.filter(course=co)
    return render(request,'course-info.html',{'co':co,'uid':uid,'index':index})
def adddepartment(request):
    uid=Register.objects.get(email=request.session['adminemail'])
    if request.method=='POST':
        try:
            dept=Department.objects.get(name=request.POST['name'])
            msg = f'Department is already in list and status is {dept.verify}'
            return render(request,'add-department.html',{'uid':uid,'msg':msg})
        except:
            Department.objects.create(
                uid=uid,
                name=request.POST['name'],
                headdepartment=request.POST['headofdepartment'],
                email=request.POST['email'],
                mobile=request.POST['phone'],
                no_of_student=request.POST['noofstudent'],
                dep_date=request.POST['date']
            )
            msg = 'Department is added'
            return render(request,'add-department.html',{'uid':uid,'msg':msg})
    return render(request,'add-department.html',{'uid':uid})
def department(request):
    uid=Register.objects.get(email=request.session['adminemail'])
    depts = Department.objects.filter(varify=False)[::-1]
    return render(request,'department.html',{'uid':uid,'depts':depts})

def allcourses(request):
    uid=Register.objects.get(email=request.session['adminemail'])
    courses = All_Course.objects.filter(covarify=False,coreject=False)[::-1]
    tcourses = All_Course.objects.filter(covarify=False,coreject=False).count
    # app_course = All_Course.objects.filter(covarify = True)
    return render(request,'allcourses.html',{'uid':uid,'courses':courses,'tcourses':tcourses})

def libraryassets(request):
    uid=Register.objects.get(email=request.session['adminemail'])
    courses = All_Course.objects.filter(covarify=False,coreject=False)[::-1]
    return render(request,'library-assets.html',{'uid':uid,'course':courses})
def addstudent(request):
    uid=Register.objects.get(email=request.session['adminemail'])
    return render(request,'add-student.html',{'uid':uid})
def allstudents(request):
    uid=Register.objects.get(email=request.session['adminemail'])
    user=m.User.objects.all()
    tstudent=m.User.objects.all().count
    return render(request,'all-students.html',{'uid':uid,'user':user,'tstudent':tstudent})
def student_delete(request,pk):
    user=m.User.objects.get(id=pk)
    # request.session['email'] = user.email
    # del request.session['email']
    user.delete()
    return redirect('allstudents')
def Enquiry(request):
    uid=Register.objects.get(email=request.session['adminemail'])
    enq=m.Enquiry.objects.all()
    return render(request,'Enquiry.html',{'uid':uid,'enq':enq})
def showreview(request):
    uid=Register.objects.get(email=request.session['adminemail'])
    review=Review.objects.all()
    return render(request,'showreview.html',{'uid':uid,'review':review})
def studentprofile(request,pk):
    uid=Register.objects.get(email=request.session['adminemail'])
    user =m.User.objects.get(id=pk)
    book=Booking.objects.filter(student=user,pay_verify=True)
    return render(request,'student-profile.html',{'uid':uid,'user':user,'book':book})
def addindex(request,pk):
    co=Department.objects.all()
    uid=Register.objects.get(email=request.session['adminemail'])
    course=All_Course.objects.get(id=pk)
    if request.method=='POST':
        post = list(dict(request.POST).keys())
        post.pop(0)
        # print(post)
        file = list(dict(request.FILES).keys())
        d = dict(zip(post,file))
        try:
            add=Add_Index.objects.get(topic=request.POST['title_name'])
            msg = 'Index is already in list please verify'
            return render(request,'addindex.html',{'uid':uid,'msg':msg})
        except:
            for p,f in d.items():
                Add_Index.objects.create(
                    uid=uid,
                    course=course,
                    topic=request.POST[p],
                    material = request.FILES[f]
                )
            msg = 'Index is added'
            return render(request,'addindex.html',{'uid':uid,'msg':msg})
    return render(request,'addindex.html',{'uid':uid,'course':course,'co':co})
def allindex(request):
    uid=Register.objects.get(email=request.session['adminemail'])
    index=Add_Index.objects.all()
    return render(request,'all-index.html',{'uid':uid,'index':index})

def coursepayment(request):
    uid=Register.objects.get(email=request.session['adminemail'])
    book=Booking.objects.filter(pay_verify=True)
    return render(request,'course-payment.html',{'uid':uid,'book':book})

def deleteindex(request,pk):
    index=Add_Index.objects.get(id=pk)
    index.delete()
    return redirect('allindex')
def deletepayment(request,pk):
    book=Booking.objects.get(id=pk)
    book.delete()
    return redirect('coursepayment')
def p404(request):
    return render(request,'404.html')
def p500(request):
    return render(request,'500.html')
def accordion(request):
    return render(request,'accordion.html')
def addlibraryassets(request):
    return render(request,'add-library-assets.html')
def addprofessor(request):
    return render(request,'add-professor.html')
def advanceformelement(request):
    return render(request,'advance-form-element.html')
def alerts(request):
    return render(request,'alerts.html')
def allprofessors(request):
    return render(request,'all-professors.html')

def analytics(request):
    return render(request,'analytics.html')
def areacharts(request):
    return render(request,'area-charts.html')

def barcharts(request):
    return render(request,'bar-charts.html')
def basicformelement(request):
    return render(request,'basic-form-element.html')
def buttons(request):
    return render(request,'buttons.html')
def c3(request):
    return render(request,'c3.html')
def codeeditor(request):
    return render(request,'code-editor.html')
def datamaps(request):
    return render(request,'data-maps.html')
def datatable(request):
    return render(request,'data-table.html')

def duallistbox(request):
    return render(request,'dual-list-box.html')
def editlibraryassets(request):
    return render(request,'edit-library-assets.html')
def editprofessor(request):
    return render(request,'edit-professor.html')
def editstudent(request):
    return render(request,'edit-student.html')
def events(request):
    return render(request,'events.html')


def googlemap(request):
    return render(request,'google-map.html')
def imagescropper(request):
    return render(request,'images-cropper.html')

def linecharts(request):
    return render(request,'line-charts.html')
def lock(request):
    return render(request,'lock.html')
def mailbox(request):
    return render(request,'mailbox.html')
def mailboxcompose(request):
    return render(request,'mailbox-compose.html')
def mailboxview(request):
    return render(request,'mailbox-view.html')
def modals(request):
    return render(request,'modals.html')
def multiupload(request):
    return render(request,'multi-upload.html')
def notifications(request):
    return render(request,'notifications.html')
def passwordmeter(request):
    return render(request,'password-meter.html')
def preloader(request):
    return render(request,'preloader.html')
def professorprofile(request):
    return render(request,'professor-profile.html')
def roundedchart(request):
    return render(request,'rounded-chart.html')
def sparkline(request):
    return render(request,'sparkline.html')
def statictable(request):
    return render(request,'static-table.html')
def tabs(request):
    return render(request,'tabs.html')
def tinymc(request):
    return render(request,'tinymc.html')
def treeview(request):
    return render(request,'tree-view.html')
def widgets(request):
    return render(request,'widgets.html')
def xeditable(request):
    return render(request,'x-editable.html')
def peity(request):
    return render(request,'peity.html')

# Java programming language was originally developed by Sun Microsystems which was initiated by James Gosling and released in 1995 as core component of Sun Microsystems' Java platform (Java 1.0 [J2SE]).
