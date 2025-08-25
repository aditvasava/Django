from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# the request parameter in the below function is compulsory even though it is not being used in the function 
def index(request):
    
    # Returning an object of class httpresponse (Here we are just returning a string, but we can also send http file as response)
    return HttpResponse("Django is working")

def feb(request):

    return HttpResponse("February Works!")