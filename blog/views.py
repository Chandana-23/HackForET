from django.shortcuts import redirect, render


from blog.models import Blog, Student, Teacher

# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request,'base.html',{'blogs':blogs})

def register(request):
    return render(request,'register.html')
    
def add(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']
        branch = request.POST['branch']
        role = request.POST['role']
        contact = request.POST['contact']
        if pwd==cpwd:
            if role=='student':
                s = Student(name=name,email=email,pwd=pwd,branch=branch,contact=contact)
                s.save()

            elif role=='teacher':
                t = Teacher(name=name,email=email,pwd=pwd,branch=branch,contact=contact)
                t.save()

        return redirect('login')
    else:
        return redirect('register')

def login(request):
    return render(request,'login.html')
    
def logged(request):
    if request.method=='POST':
        email = request.POST['email']
        pwd = request.POST['pwd']
        role = request.POST['role']
        if role=='student':
            try:
                c_email = Student.objects.get(email=email)
            except:
                return redirect("login")
            if c_email.pwd==pwd:
                setattr(c_email,"auth",True)
                return render(request,"base.html",{'auth':c_email.auth,'email':email,'role':c_email.role})
            else:
                return redirect("login")
        else:
            try:
                c_email = Teacher.objects.get(email=email)
            except:
                return redirect("login")
            if c_email.pwd==pwd:
                setattr(c_email,"auth",True)
                return render(request,"base.html",{'auth':c_email.auth,'email':email,'role':c_email.role})
            else:
                return redirect("login")
    else:
        return redirect('login')

def logout(request):
    return redirect("/")

def write(request):
    return render(request,'write.html')

def addblog(request):
    print("Blog saved")
    if request.method=='POST':
        content = request.POST['blog']
        img = request.POST['img']
        email = request.POST['email']
        role = request.POST['role']
        d = Blog(email=email,role=role,content=content,img=img)
        d.save()
        print("Blog saved")
        blogs = Blog.objects.all()
        return redirect("/",{'blogs':blogs})
    else:
        # return redirect("write/"+email+"/"+role)
        blogs = Blog.objects.all()
        return redirect("/",{'blogs':blogs})