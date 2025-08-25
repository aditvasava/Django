from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# the request parameter in the below function is compulsory even though it is not being used in the function 
# def january(request):
    
#     # Returning an object of class HttpResponse (Here we are just returning a string, but we can also send http file as response)
#     return HttpResponse("Django is working")

# def february(request):
#     return HttpResponse("February Works!")

monthly_challenges = {
    "january": "Eat no meat for 30 days",
    "february": "Walk for 30 mins a day.",
    "march": "Learn Django for 10 mins a day.",
    "april": "Watch Squid Game",
    "may": "Visit Norway",
    "june": "Purchase umbrella",
    "july": "Learn Azure",
    "august": "practice c++",
    "september": "play watch dogs",
    "october": "play pubg",
    "november": "learn git",
    "december": "enjoy vacations"
}

# user can enter a number in the url, and below method will redirect the request to another url.
# basically, only the string part in the url is the one which shows some data.
def monthly_challenge_by_number(request, month):
    if month > 12 or month < 1:
        return HttpResponseNotFound("Invalid Month")
    
    months = list(monthly_challenges.keys())
    redirect_month = months[month-1]

    # the first parameter in the reverse function is coming from the urls.py file
    redirect_path = reverse("month-challenge", args = [redirect_month])    # challenges/february , challenges/january
    
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    return HttpResponseRedirect(redirect_path)


# We are creating view for every month, however we don't know what the user might enter in the url, so use dynamic path segments
# below function solves the problem of any route, we use the same function to handle any month entered in URL
# the second parameter name in the below function - "month" should be same as the one defined in the urls.py file.
def monthly_challenge(request, month):
    # challenge_text = None
    # if month == "january":
    #     challenge_text = "Eat no meat for 30 days"
    # elif month == "february":
    #     challenge_text = "Walk for 30 mins a day."
    # elif month == "march":
    #     challenge_text = "Learn Django for 10 mins a day."
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Month does not exist")