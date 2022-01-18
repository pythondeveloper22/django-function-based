from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# this function will create data and show data in same html page
def add_show(request):
    # stud = User.objects.all()
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        print("this comes when request is post")
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            # it will store the data into database table
            reg = User(name=nm, email=email, password=password)
            fm.save(reg)
            fm = StudentRegistration()


    else:
        fm = StudentRegistration()
        print("this comes when request is get request")
    stud = User.objects.all()
    return render(request, 'crud/addandshow.html', {'form': fm, 'student': stud})

#update data
def update_data(request, id):
    if request.method == 'POST':
        d = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=d)
        if fm.is_valid():
            fm.save()
    else:
        d = User.objects.get(pk=id)
        fm = StudentRegistration(instance=d)

    return render(request, 'crud/updatestudent.html',{'form' : fm})
# this function will delete data
def delete_data(request, id):
    if request.method == 'POST':
        d=User.objects.get(pk=id)
        d.delete()
        return HttpResponseRedirect('/')
