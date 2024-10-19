from django.shortcuts import render
from .models import *
# Create your views here.
def about(request):
    context = {
        "title":""
    }
    return render(request,'about.html',context=context)

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        number = request.POST.get('number')
        text = request.POST.get('text')
        print(text)
        
    infoObj = Info.objects.get(id=1)
    services = Service.objects.all()
    doctores = Doctor.objects.all()

    context = {
        "doctores":doctores,
        "services":services,
        "info":infoObj,
        "title":"Clinic - website"
    }
    return render(request,'index.html',context=context)

def feature(request):
    context = {
        "title":""
    }
    return render(request,'feature.html',context=context)

def appointment(request):
    context = {
        "title":"Someone Text"
    }
    return render(request,'appointment.html',context=context)

def contact(request):
    context = {
        "title":"Someone Text"
    }
    return render(request,'contact.html',context=context)

def service(request):
    context = {
        "title":"Someone Text"
    }
    return render(request,'service.html',context=context)

def team(request):
    context = {
        "title":"Someone Text"
    }
    return render(request,'team.html',context=context)

def testimonial(request):
    context = {
        "title":"Someone Text"
    }
    return render(request,'testimonial.html',context=context)


def page_404(request):
    return render(request,'404.html',{"title":"404 Not Founs"})