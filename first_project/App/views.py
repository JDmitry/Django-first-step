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

def user(request, name="No name", age=0):
    return HttpResponse(f"""
                            <p>Name: {name}</p>
                            <p>Age: {age}</p>
                         """)