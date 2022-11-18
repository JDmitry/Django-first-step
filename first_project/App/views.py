from django.http import HttpResponse
  
def index(request):
    return HttpResponse("<h1>Index</h1>")

def about(request, name, age):
    return HttpResponse(f"""
                            <h1>
                                name: {name}, 
                                age: {age} 
                            </h1>
                        """)

def contact(reqest):
    return HttpResponse("<h1>Contact</h1>")