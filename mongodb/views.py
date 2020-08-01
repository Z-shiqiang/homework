from django.shortcuts import render, redirect

# Create your views here.
from mongodb.models import User


def index(request):
    user = User.objects.all()
    return render(request, 'index.html', {'user': user})

def createuser(request):
    if request.POST:
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        grade = request.POST.get('grade')
        User.objects.create(name=name, age=age, grade=grade)
        return redirect('/')

def deleteuser(request, name):
    User.objects.filter(name=name).first().delete()
    return redirect('/')

def updateuser(request, id):
    if request.POST:
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        grade = request.POST.get('grade')
        User.objects.filter(id=id).update(name=name, age=age, grade=grade)
        return redirect('/')

    user = User.objects.filter(id=id)
    return render(request, 'updateuser.html', {'user': user})
