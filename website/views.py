from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("""<h2>Hey I am a django Server</h2>
                        <p>hemel</p>
                        <hr/>
                        """)

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("This is contact page")

def hemel(request):
    return HttpResponse("hemel")