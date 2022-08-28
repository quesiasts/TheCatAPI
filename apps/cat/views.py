import json

import requests
from django.shortcuts import HttpResponse
from prettyconf import config


def get_breeds(request):
    headers = {"x-api-key": config("API_KEY")}
    response = requests.get("https://api.thecatapi.com/v1/breeds", headers=headers)
    breeds = response.json()
    for i in breeds:
        data = json.dumps(i)
        return HttpResponse(data)


def get_image_urls(request):
    headers = {"x-api-key": config("API_KEY")}
    response = requests.get(
        "https://api.thecatapi.com/v1/images/search?limit=3", headers=headers
    )
    breeds = response.json()

    for i in breeds:
        data = json.dumps(i)
        return HttpResponse(data)
