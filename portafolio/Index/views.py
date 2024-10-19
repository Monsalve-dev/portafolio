from django.shortcuts import render
from .models import Project

# Create your views here.
def home2(request):
    Proyectos = Project.objects.all()
    return render(request, "Index/Home2.html", {"Aplicaciones": Proyectos})