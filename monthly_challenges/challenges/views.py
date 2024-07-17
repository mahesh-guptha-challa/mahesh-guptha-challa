from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "jan": "Hey it is Jan!...",
    "feb": "Hey it is Feb!...",
    "mar":"Hey it is Mar!...",
    "Apr":"Hey it is Apr!...",
    "may":"Hey it is May!...",
    "jun":"Hey it is Jun!...",
    "jul":"Hey it is Jul!...",
    "Aug":"Hey it is Aug!...",
    "sep": "Hey it is sep",
    "oct": "Hey it is oct",
    "nov": "hey it is nov",
    "dec": None
}

# Create your views here.
def challenges_by_number(request, month):
    
    if  month>len(monthly_challenges):
        return HttpResponseNotFound(f"Invalid month number.....")

    redirect_url = reverse("str-month", args = [list(monthly_challenges.keys())[month-1]])
    # not good practices to follow
    # redirect_url = f"/challenges/{list(monthly_challenges.keys())[month-1]}"
    # redirect_url = f"./{list(monthly_challenges.keys())[month-1]}"
    return HttpResponseRedirect(redirect_url)

def challenges_direct(request, month):

    try:
        # if needed we can send normal text.
        response = monthly_challenges[month]
        # we can send html text by following.
        html_response = f"<b>{response}</b>"
        return render(request, "challenges/challenges.html", {"text": response, "month_name": month})
        # return HttpResponse(html_response)
    except Exception as e:
        # error_response = render_to_string("404.html")
        # return HttpResponseNotFound(error_response)
        return Http404()
        # return HttpResponseNotFound(f"We are not supporting this {month} currently...")

def challenges_list(request):

    # returning the html response using the legacy method.
    # return HttpResponse(render_to_string("challenges/challenges.html"))
    # returning in the latest and short cu method.
    # return render(request, "challenges/challenges.html")
    redirect_url = reverse("str-month", args = [list(monthly_challenges.keys())[0]])
    months = list(monthly_challenges.keys())
    # text = f"""<a href="{redirect_url}">jan</a>"""
    # the following code is begging.
    # for each_month in monthly_challenges.keys():
    #     redirect_url = reverse("str-month", args = [each_month])
    #     text = f"""<li><a href="{redirect_url}">{each_month.capitalize()}</a></li>"""
    #     return_response+=text
    # return_response = f"<ul>{return_response}</ul>"

    return render(request, "challenges/index.html", {"months": months})


# to rn the server.
# python manage.py runserver