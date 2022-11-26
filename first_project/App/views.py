from django.shortcuts import render

class User:
    def __init__(self, name):
        self.name = name

def index(request):
    user = User("Sam")
    data = {"user": user}
    return render(request, "index.html", context=data)



