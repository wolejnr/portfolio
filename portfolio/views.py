from django.shortcuts import render
from .models import Project
import requests
import json

# Create your views here.
def home(request):
    projects = Project.objects.all()
    data = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
    data = json.loads(data.text)
    data = data["moves"][0]["move"]["name"]
    return render(request, 'portfolio/index.html', {'projects': projects, 'data': data})