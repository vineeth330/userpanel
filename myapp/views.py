from django.shortcuts import render, redirect
from myapp.models import studentdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.


def displayindex(req):
    return render(req, "index.html")


def displaystudent(req):
    return render(req, "studentpage.html")


def studentdata(req):
    if req.method == "POST":
        na = req.POST.get('name')
        ag = req.POST.get('age')
        mo = req.POST.get('mobile')
        em = req.POST.get('email')
        cs = req.POST.get('course')
        ad = req.POST.get('address')
        im = req.FILES['image']
        obj = studentdb(Name=na, Age=ag, Mobile=mo, Email=em, Course=cs, Address=ad, Image=im)
        obj.save()
        return redirect(displaystudent)


def studentdetails(req):
    data = studentdb.objects.all()
    return render(req, "Displaystudent.html", {'data': data})


def studentedit(req, dataid):
    data = studentdb.objects.get(id=dataid)
    return render(req, "Editstudent.html", {'data': data})


def studentupdate(req, dataid):
    if req.method == "POST":
        na = req.POST.get('name')
        ag = req.POST.get('age')
        mo = req.POST.get('mobile')
        em = req.POST.get('email')
        cs = req.POST.get('course')
        ad = req.POST.get('address')
        try:
            im = req.FILES['image']
            fs = FileSystemStorage()



            file = fs.save(im.name, im)
        except MultiValueDictKeyError:
            file = studentdb.objects.get(id=dataid).Image
        studentdb.objects.filter(id=dataid).update(Name=na, Age=ag, Mobile=mo, Email=em, Course=cs, Address=ad, Image=file)
        return redirect(studentdetails)