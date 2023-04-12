
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "January": "This is January",
    "February": "This is February",
    "March": "This is March",
    "April": "This is April",
    "May": "This is May",
    "June": "This is June",
    "July": "This is July",
    "August": "This is August",
    "September": "This is September",
    "October": "This is October",
    "November": "This is November",
    "December": None
}


def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", context={
            'text': text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("no month found")
        raise


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())

        if month > len(months):
            return HttpResponseNotFound("no months found sorry")

        redirect_month = months[month - 1]
        redirect_path = reverse("month_challange", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("not found")
        raise


def list_of_months(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", context={
        'months': months
    })
