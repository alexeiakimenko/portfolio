from django.shortcuts import render
from .models import Skills


# Create your views here.

def index(request):
    project = Skills.objects.all()
    return render(request, 'skills/attraction.html', {'projects': project})