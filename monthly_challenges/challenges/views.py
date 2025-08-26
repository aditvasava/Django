from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# reverse used to handle dynamic urls 
from django.urls import reverse

# render_to_string used to convert html file to string
from django.template.loader import render_to_string

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
    "december": None
}

def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</li>"

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

    return render(request, "challenges/index.html", {"months": months})


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
        # response_data = f"<h1>{challenge_text}</h1>"

        # edit settings.py file in the main folder of project to allow the functionality of sending html files
        # why did we create a challenges sub-folder ?
        # -> It might be possible that there could be other apps in the project and could have a similar file name
        # -> such as "challenge.html", so to keep things linear, create sub-folders inside templates folder as the same name as the app

        # render_to_string() is the more specific method of converting files to string,
        # there is a more generalized way, which is render() method, this is automatically imported by default at the top of file
        
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)

        # the first parameter - "request" in render() is mandatory to write
        challenge_text = monthly_challenges[month]
        # capitalized_month = month.capitalize()
        return render(request, "challenges/challenge.html", {"text": challenge_text, "title": month}) # writing this is same as what the above 2 code line does.
    except:
        return HttpResponseNotFound("<h2>Month does not exist</h2>")