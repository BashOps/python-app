from django.shortcuts import render
from django.http import HttpResponse
from .models import Department
# Create your views here.
def home(request):
    number = {
        "num": 0
    }
    return render(request, "index.html", number)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def booking(request):
    return render(request, "booking.html")

def vision(request):
    return render(request, "vision.html")

def department(request):
    dict_dept = {
    'dept': Department.objects.all()
    }
    return render(request, "department.html", dict_dept)

# Create your views here.
