import requests
import json
from prettyconf import config
from django.shortcuts import HttpResponse

# Create your views here.
def get_breeds(request):
    #pull data from third party rest api
    headers = {
        'x-api-key': config("API_KEY")
    }
    response = requests.get('https://api.thecatapi.com/v1/breeds', headers=headers)
    #convert reponse data into json
    breeds = response.json()
    for i in breeds:
        data = json.dumps(i)
        return HttpResponse(data)

def get_image_urls(request):
    headers = {
        'x-api-key': config("API_KEY")
    }
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=3', headers=headers)
    breeds = response.json()

    for i in breeds:
        data = json.dumps(i)
        return HttpResponse(data)
