from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages



# Create your views here.

def index(request):
    context ={
        "variable1" : "this is  my vairable1",
        "variable2" : "this is  my vairable2"

    }
    return render(request,"index.html" , context)




def about(request):
    return render(request,"about.html")



def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        #date=request.POST.get('date')
        if len(name)<2  or len(email)<2 or len(phone)<10  or len(desc)<4:
            messages.error(request, ' Plese fill form corretly ')
        else:
            contact = Contact(name=name,  email=email, phone=phone,  desc=desc,  date=datetime.today())
            contact.save()
            messages.success(request, ' Your message has been Sent!')

    return render(request,"contact.html")


    


def services(request):
    return render(request,"services.html")
    