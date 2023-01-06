from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from .forms import UserRegistrationForm,CourseeditForm,ExameditForm,MarkeditForm,Teachprofeditform,Stuprofeditform
from django.contrib.auth.models import User
from .models import UserType,Courses,Exam,Marks,Materials,Teachprofile,Stuprofile,Mycourses

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        newpass = make_password(password)
        newuser = User.objects.create(username=username,password=newpass,first_name=fname,last_name=lname,email=email)
        newuser.save()
        usertype = request.POST.get('usertype')
        newtype = UserType.objects.create(user_type=usertype)
        newtype.save()
        messages.success(request, "Registration successful")
        return redirect('index')
    return render(request, 'register.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.info(request, "Login Successful")
            return redirect('adminhome')
        else:
            messages.error(request, "Invlid username or password")
    return render(request, 'login.html')

def Teachlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.info(request, "Login Successful")
            return redirect('Teachhome')
        else:
            messages.error(request, "Invlid username or password")
    return render(request, 'login.html') 

def Stulogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.info(request, "Login Successful")
            return redirect('Stuhome')
        else:
            messages.error(request, "Invlid username or password")
    return render(request, 'login.html') 

def index(request):
    return render(request,'index.html')

def logout(request):
    auth_logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("index")   

def adminhome(request):
    return render(request, 'adminhome.html')

def Userslist(request):
    myusers = User.objects.all()
    context = {'myusers': myusers}
    return render(request, 'mngusrs.html', context)

def Useredit(request, id):
    user = User.objects.get(id=id)
    usereditForm = UserRegistrationForm(instance=user)
    if request.method == 'POST':
        usereditForm = UserRegistrationForm(request.POST, instance=user)
        if usereditForm.is_valid():
            usereditForm.save()
            messages.success(request, 'user updated successfully.')
            return redirect('Userslist')
    return render(request, 'edituser.html', {'user': user, 'usereditform': usereditForm})  

def deleteuser(request, id):
    deleteus = User.objects.get(id=id)
    deleteus.delete()
    messages.success(request, 'User deleted successfully.')
    return redirect('Userslist')

def Courselist(request):
    mycourses = Courses.objects.all()
    context = {'mycourses': mycourses}
    return render(request, 'mngcourses.html', context)

def Courseadd(request):
    if request.method == 'POST':
        newcourse = request.POST.get('coursename')
        price = request.POST.get('price')
        new = Courses.objects.create(course_name=newcourse, course_price=price)
        new.save()
        messages.success(request, "Course created successfully")
        return redirect('Courselist')  
    return render(request,'addcourses.html') 

def Courseedit(request, id):
    user = Courses.objects.get(id=id)
    courseeditForm = CourseeditForm(instance=user)
    if request.method == 'POST':
        courseeditForm = CourseeditForm(request.POST, instance=user)
        if courseeditForm.is_valid():
            courseeditForm.save()
            messages.success(request, 'Course updated successfully.')
            return redirect('Courselist')
    return render(request, 'editcourses.html', {'user': user, 'courseeditForm': courseeditForm})

def deletecourse(request, id):
    deletecour = Courses.objects.get(id=id)
    deletecour.delete()
    messages.success(request, 'Course deleted successfully.')
    return redirect('Courselist') 

def Examlist(request):
    myexams = Exam.objects.all()
    context = {'myexams': myexams}
    return render(request, 'mngexam.html', context) 

def Examadd(request):
    mycourses = Courses.objects.all()
    context = {'mycourses': mycourses}
    if request.method == 'POST':
        newexam = request.POST.get('examname')
        course = request.POST.get('courses')
        examtime = request.POST.get('time')
        new = Exam.objects.create(exam_name=newexam,course_id=course,exam_time=examtime)
        new.save()
        messages.success(request, "Course created successfully")
        return redirect('Examlist')
    return render(request,'addexam.html',context) 


def Examedit(request, id):
    user = Exam.objects.get(id=id)
    exameditForm = ExameditForm(instance=user)
    if request.method == 'POST':
        exameditForm = ExameditForm(request.POST, instance=user)
        if exameditForm.is_valid():
            exameditForm.save()
            messages.success(request, 'Exam updated successfully.')
            return redirect('Examlist')
    return render(request, 'editexam.html', {'user': user, 'exameditForm': exameditForm}) 

def deleteexam(request, id):
    deleteex = Exam.objects.get(id=id)
    deleteex.delete()
    messages.success(request, 'Exam deleted successfully.')
    return redirect('Examlist')

def Marklist(request):
    mymark = Marks.objects.all()
    context = {'mymark': mymark}
    return render(request, 'mngmarks.html', context) 

def Markedit(request, id):
    user = Marks.objects.get(id=id)
    markeditForm = MarkeditForm(instance=user)
    if request.method == 'POST':
        markeditForm = MarkeditForm(request.POST, instance=user)
        if markeditForm.is_valid():
            markeditForm.save()
            messages.success(request, 'Mark updated successfully.')
            return redirect('Marklist')
    return render(request, 'editmark.html', {'user': user, 'markeditform': markeditForm}) 

def deletemark(request, id):
    deletemar = Marks.objects.get(id=id)
    deletemar.delete()
    messages.success(request, 'Marks deleted successfully.')
    return redirect('Marklist')

def Materialslist(request):
    material = Materials.objects.all()
    context = {'material': material}
    return render(request, 'mngmaterials.html', context) 

def deletematerial(request, id):
    deletemat = Materials.objects.get(id=id)
    deletemat.delete()
    messages.success(request, 'Material deleted successfully.')
    return redirect('Materialslist')

def Teachhome(request):
    return render(request,'teachhome.html')

def viewteachpro(request):
    profile = Teachprofile.objects.filter(owner=request.user)
    context = {'profile': profile}
    return render(request, 'teachprofile.html', context)

def Teachprofedit(request, id):
    user = Teachprofile.objects.get(id=id)
    teachprofForm = Teachprofeditform(instance=user)
    if request.method == 'POST':
        teachprofForm = Teachprofeditform(request.POST, instance=user)
        if teachprofForm.is_valid():
            teachprofForm.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('viewstupro')
    return render(request, 'Teachprofedit.html', {'user': user, 'teachprofForm': teachprofForm})

def Teachlistmarks(request):
    marks = Marks.objects.all()
    context = {'marks': marks}
    return render(request, 'teachlistmarks.html', context)

def Markadd(request):
    if request.method == 'POST':
        exam = request.POST.get('exam')
        course = request.POST.get('course')
        new = Marks.objects.create(exam_id=exam,)
        messages.success(request, "Marks Added successfully")
        return redirect('Teachlistmarks')
    return render(request,'uploadmarks.html',{'newmarkform': newmarkform})

def Teachlistmaterials(request):
    material = Materials.objects.filter(course=request.Teachprofile.course)
    context = {'material',material}
    return render(request,'teachlistmaterials.html',context)

def Materialadd(request):
    course = Courses.objects.all()
    context = {'courses': course}
    if request.method == 'POST' and request.FILES['material']:
        newmaterial = request.FILES('material')
        course = request.POST.get('course')
        new = Materials.objects.create(material=newmaterial, course_id=course)
        new.save()
        messages.success(request, "Material Added successfully")
        return redirect('Materialadd')
    return render(request,'uploadmaterials.html',context)

def Stuhome(request):
    course = Courses.objects.all()
    context = {'course':course}
    return render(request,'stuhome.html',context)

def viewstupro(request):
    profile = Stuprofile.objects.filter(owner=request.user)
    context = {'profile': profile}
    return render(request, 'stuprofile.html', context)

def Stuprofedit(request, id):
    user = Stuprofile.objects.get(id=id)
    stuprofForm = Stuprofeditform(instance=user)
    if request.method == 'POST':
        stuprofForm = Stuprofeditform(request.POST, instance=user)
        if stuprofForm.is_valid():
            stuprofForm.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('viewstupro')
    return render(request, 'studproedit.html', {'user': user, 'stuprofForm': stuprofForm})

def Mycourseslist(request):
    Mycourse = Mycourses.objects.filter(owner=request.user)
    context = {'Mycourse': Mycourse}
    return render(request, 'mycourses.html', context)

def viewprogress(request):
    marks = Marks.objects.filter(owner=request.user)
    context = {'marks': marks}
    return render(request, 'progress report.html', context)

def Stuproadd(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        place = request.POST.get('place')
        city = request.POST.get('city')
        state = request.POST.get('state')
        new = Stuprofile.objects.create(name=name,dOB=dob,address=address,place=place,city=city,state=state)
        new.owner=request.user
        new.save()
        messages.success(request, "Profile submitted successfully")
        return redirect('viewstupro')
    return render(request,'studproadd.html')
    
def Teachproadd(request):
    cours = Courses.objects.all()
    context = {'cours': cours}
    if request.method == 'POST':
        name = request.POST.get('fullname')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        place = request.POST.get('place')
        city = request.POST.get('city')
        state = request.POST.get('state')
        course = request.POST.get('course')
        new = Teachprofile.objects.create(name=name,dob=dob,address=address,place=place,city=city,state=state,course_id=course)
        new.owner=request.user
        new.save()
        messages.success(request, "Profile submitted successfully")
        return redirect('index')
    return render(request,'teachproadd.html',context)
    
def viewmaterial(request):
    mats = Materials.objects.filter(course=request.Courses)
    context = {'mats': mats}
    return render(request, 'viewmaterial.html', context)

def payment(request):
    cours = Courses.objects.all()
    context = {'cours': cours}
    if request.method == 'POST':
        course = request.POST.get('course')
        new = Mycourses.objects.create(course_id=course)
        new.owner = request.user
        new.save()
        return redirect('Mycourseslist')
    return render(request,'payment.html',context)
