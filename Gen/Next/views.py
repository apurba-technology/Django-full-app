from django.shortcuts import render, redirect
from django.http import HttpResponse
from Next.functions.functions import handle_uploaded_file  
from Next.forms import *
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == 'GET':
        Banners = Banner.objects.all()  
        return render(request, 'index.html',{'banner_images' : Banners}) 
    #return render(request,'index.html')


def log(request):
    return render(request,'user_log_in1.html')

def contact(request):
    if request.method == 'GET':
        Banners = Banner.objects.all()  
        return render(request, 'contact.html',{'banner_images' : Banners})
    #return render(request, 'contact.html')


def about(request):
    if request.method == 'GET':
        Banners = Banner.objects.all()  
        return render(request, 'about.html',{'banner_images' : Banners})
    #return render(request,'about.html')

def admin(request):
    return render(request,'admin.html')


def banner_upload(request): 
  
    if request.method == 'POST': 
        form = BannerForm(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return redirect('display_images') 
            #messages.success(request,'apurba')
            #return render(request, 'banner_up.html', {'form' : form})
    else: 
        form = BannerForm() 
    return render(request, 'banner_up.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('<center><h1>successfully uploaded <br><a href="admin">back</a></h1></center>') 

def display_images(request): 
  
    if request.method == 'GET':
        Banners = Banner.objects.all()  
        return render(request, 'di.html',{'banner_images' : Banners}) 

def delete(request, id):
    Banners = Banner.objects.get(id=id)
    Banners.delete()
    return redirect("display_images")



def admin_regestion(request):
	error=True
	if request.method=='POST':
		b=admin_regestion_meForm(request.POST)
		bb=admin_regestion_me()
		bb.name=request.POST['name']
		bb.e_mail=request.POST['e_mail']
		bb.password=request.POST['password']
		bb.password1=request.POST['password1']
		if bb.password == bb.password1:
			error = False
			bb.password=request.POST['password']
			bb.save()
			return HttpResponse("Regestion complet")
		else:
			b=admin_regestion_meForm()
			return render(request,"admin_reg.html",{'form':b})				
	else:
		b=admin_regestion_meForm()
		return render(request,"admin_reg.html",{'form':b})


def log_in(request):
	if request.method=='POST':
		e_mail=request.POST['e_mail']
		password=request.POST['password']
		row=admin_regestion_me.objects.raw("select id,e_mail,password from Admin_Regestion where e_mail='"+str(e_mail)+"' and password='"+str(password)+"'")
		#return HttpResponse(row)
		if(row):
			return redirect("admin")
		else:
			return render(request, "admin_login.html")
            #return HttpResponse("Not Ok")


	else:
		return render(request,"admin_login.html")
		#return HttpResponse("Password is Worng")


