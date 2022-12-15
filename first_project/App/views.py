from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
  
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        comment = request.POST.get("comment")
        num = request.POST.get("num")
        return HttpResponse(f"<h1>Name: {name}    -   Num:  {num}  - Comment: {comment}</h1>")
    else:
        userform = UserForm(field_order = ["name", "comment", "num"])
        return render(request, "index.html", {"form": userform})