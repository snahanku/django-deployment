from django.shortcuts import render , HttpResponseRedirect
from Crudapp.forms import StudentRegistration
from Crudapp.models import User

# Create your views here.
def show_base(request):
    return render(request , "base.html")

def add_show(request):
    if request.method=="POST" :
        database_data= User()
        fm= StudentRegistration(request.POST)
        if fm.is_valid():
            database_data= User()
            database_data.name=fm.cleaned_data['name']
            database_data.email= fm.cleaned_data['email']
            database_data.password= fm.cleaned_data['password']
            database_data.save()
            fm=StudentRegistration() #to made the form again blank we can render  (here) fm=StudendtRegistration() that is blank 
    else:
        fm=StudentRegistration()
    stu= User.objects.all()
    return render(request, "addandshow.html" ,   {'form' :fm , "stu": stu})

def delete_data(request , id):
    if request.method=="POST":
        pi = User.objects.get( pk=id)
        pi.delete()
    return  HttpResponseRedirect('/')
        
        
def update_data(request, id ):
    if  request.method=="POST":
        pi= User.objects.get(pk=id)
        fm= StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi= User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request , "Updatestudent.html"  ,  {"form":fm} )
