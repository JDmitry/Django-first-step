from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
  
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h1>Name: {name}, age: {age}</h1>")
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})