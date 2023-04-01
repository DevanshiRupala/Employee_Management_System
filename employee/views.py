from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')

def adlogin(request):
    error=""
    if request.method == 'POST':
        u = request.POST['user']
        p = request.POST['pass']
        if u == 'admin@321':
            if p == 'dreamers@123':
                error = "no"
            else:
                error = "yes"
        else:
            error = "yes"
    return render(request, 'adlogin.html', locals())

def emplogin(request):
    error=""
    if request.method == 'POST':
       u = request.POST.get('username')
       p = request.POST.get('password')
       user = authenticate(username=u, password=p)
       if user:
          login(request, user)
          error="no"
       else:
            error="yes"
    return render(request, 'emplogin.html', locals())

def option(request):
    return render(request, 'option.html')

def Logout(request):
    logout(request)
    return render(request, 'index.html')

def registration(request):
    error = ""
    if request.method == 'POST':
        id = request.POST['id']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phno = request.POST['phno']
        dept = request.POST['dept']
        des = request.POST['des']
        jdate = request.POST['date']
        pwd = request.POST['pwd']

        try:
          user = User.objects.create(first_name=fname, last_name=lname, password=pwd, username=fname)
          emp_details.objects.create(user=user, email=email, emp_id=id, contact=phno, empdept=dept, designation=des, joindate=jdate)
          error = "no"
        except:
           error = "yes"

    return render(request, 'registration.html', locals())

def upload_payroll(request):
    error = ""
    if request.method == 'POST':
        id = request.POST['id']
        reg = request.POST['reg']
        ot = request.POST['ot']
        bonus = request.POST['bonus']
        total = request.POST['total']

        try:
            payroll.objects.create(emp_id=id, reg_salary=reg, overtime=ot, bonus=bonus, total=total)
            error="no"
        except:
            error="yes"
    return render(request, 'upload_payroll.html', locals())

def grant_leave(request):

    if request.method == 'POST':
        id = request.POST['id']
        res = request.POST['response']
        leave_res.objects.create(emp_id=id, response=res)
        l=leave.objects.get(emp_id=id)
        l.delete()

    leav = leave.objects.all().values()
    context = {
        "data": leav,
    }
    return render(request, 'grant_leave.html', context)

def view_payroll(request):
    emp=""
    pay=""
    user = request.user
    emp = emp_details.objects.get(user=user)
    pay = payroll.objects.get(emp_id=emp.emp_id)
    return render(request, 'view_payroll.html', locals())

def leaves(request):
    error =""
    r=""
    if request.method == 'POST':
        id = request.POST['id']
        fname = request.POST['fname']
        lname = request.POST['lname']
        reason = request.POST['reason']
        des = request.POST['des']
        dept = request.POST['dept']
        date1 = request.POST['date1']
        date2 = request.POST['date2']

        try:
            leave.objects.create(emp_id=id, reason=reason, stdate=date1, enddate=date2, fname=fname, lname=lname, des=des, dept=dept,)
            error="no"
        except:
            error="no"

    try:
       user = request.user
       emp = emp_details.objects.get(user=user)
       l = leave_res.objects.get(emp_id=emp.emp_id)
       if l.response == "leave granted":
            r="yes"
            l.delete()
       if l.response == "leave not granted":
            r="no"
            l.delete()
    except:
        r=""
    return render(request, 'leave.html', locals())

def profile(request):
    employee=""
    user = request.user
    employee = emp_details.objects.get(user=user)

    return render(request, 'profile.html', locals())