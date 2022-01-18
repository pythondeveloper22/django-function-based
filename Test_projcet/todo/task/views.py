from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    return HttpResponse("HI")
def studentinfo(request):
    #example4
    # stu=Student.objects.all()
    stu = Student.objects.get(pk=2)
    print(stu)
    return render(request,"task/studentinfo.html",{'student':stu})

