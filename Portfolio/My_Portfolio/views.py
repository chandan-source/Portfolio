from django.shortcuts import render
from django.shortcuts import redirect
from.models import *

# Create your views here.
def home(request):

    return render(request,'base.html')
def aboutus(request):
    return render(request,'about.html')
def my_work(request,type):
    c1='';
    c2='';
    c3='';
    if type=='all':
        c1='active'
    elif type=='commercial':
        c2='active'
    elif type=='personal':
        c3='active'
    wdata=Work.objects.all()
    d={"wdata":wdata,"type":type,"class1":c1,"class2":c2,"class3":c3}
    return render(request,'work.html',d)
def blog(request):
    blogdata=Blog.objects.all()
    d={"blogdata":blogdata}
    return render(request,'blog.html',d)
def contact(request):
    if request.method=='POST':
        dic=request.POST
        name=dic['name']
        email=dic['email']
        mobile=dic['tel']
        mssg=dic['message']
        message_detail.objects.create(name=name,email=email,contact_no=mobile,message=mssg)
        return redirect('home')



    return render(request,'contact.html')
def work_detail(request,wid):
    wd=Work.objects.get(id=wid)
    d={"wd":wd}
    return render(request,'work_detail.html',d)
def blog_detail(request,bid):
    bd=Blog.objects.get(id=bid)
    d={"bd":bd}
    return render(request,'blog_detail.html',d)
