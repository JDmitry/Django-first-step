from django.http import HttpResponse

def set(request):
    name = request.GET.get("name", "No")
    res = HttpResponse(f"Name: {name}")
    res.set_cookie("user", name)
    return res
 
def get(request):
    # user = request.COOKIES["user"]
    user = request.GET.get_sign_cookie("user")
    return HttpResponse(f"Hi, {user}")
