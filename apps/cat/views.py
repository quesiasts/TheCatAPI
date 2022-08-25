from django.shortcuts import render
import requests

def index(request):
    api = "https://api.thecatapi.com/v1/images/search?limit=10"
    req = requests.get(api)

    try:
        arr = req.json()
    except ValueError:
        print("The response didn't arrive in the expected format")

    dictionary = {}
    for index, value in enumerate(arr):
        dictionary[index] = value

    context = {
        "cats" : dictionary
    }

    return render(request, "index.html", context)