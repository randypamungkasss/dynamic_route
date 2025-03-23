from django.shortcuts import render
from .models import Todo

# Create your views here.
def index_view(request):
    todos = Todo.objects.all()
    return render(request, "index.html", {'todos': todos})