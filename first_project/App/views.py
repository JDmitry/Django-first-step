from django.shortcuts import render
  
def index(request):
    return render(request, "index.html", context={"name": "Earth"})
 
def contact(request):
    return render(request, "contact.html")