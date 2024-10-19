from django.shortcuts import render, redirect
from .models import Adminis
# Create your views here.
def home2(request):
    Administ = Adminis.objects.all()
    return render(request, "proyecto1/app.html", {"Tareas": Administ})

def registarTarea(request):
    title=request.POST['txtTitle']
    descrip = request.POST['txtDescrip']
    
    tarea= Adminis.objects.create(Title=title, Descrip=descrip)
    return redirect('/app1/home')   
def actualizarTarea(request, Title):
    tarea=Adminis.objects.get(Title=Title)
    
    return render(request, "proyecto1/ActualizarTarea.html", {"Tareas": tarea})


def ActualizarTarea(request):
    title=request.POST['txtTitle']
    descrip = request.POST['txtDescrip']
    
    tarea=Adminis.objects.get(Title=title)
    
    tarea.Title=title
    tarea.Descrip=descrip
    tarea.save()
    return redirect('/app1/home')   
def leerTarea(request, Title):
    tarea=Adminis.objects.get(Title=Title)
    
    return render(request, "proyecto1/Leer.html", {"Tareas": tarea})

def LeerTarea(request):
    title=request.POST['txtTitle']
    descrip = request.POST['txtDescrip']
    
    return redirect('/app1/home')
    
def eliminarTarea(request, Title):
    tarea=Adminis.objects.get(Title=Title)
    tarea.delete()
    return redirect('/app1/home')
