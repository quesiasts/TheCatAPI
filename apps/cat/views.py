from prettyconf import config
from django.http import HttpResponse
import requests


# Create your views here.
def get_breeds(request):
    #pull data from third party rest api
    headers = {
        'x-api-key': config("API_KEY")
    }
    response = requests.get('https://api.thecatapi.com/v1/breeds', headers=headers)
    #convert reponse data into json
    breeds = response.json()

    return HttpResponse(breeds)

def get_image_urls(request):
    headers = {
        'x-api-key': config("API_KEY")
    }
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=3', headers=headers)
    breeds = response.json()

    return HttpResponse(breeds)