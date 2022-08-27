import requests
import json
from prettyconf import config
from django.shortcuts import HttpResponse
from cat.models import Cat, CatBreed

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

    for i in breeds:
        cats_data = Cat(
            breed = i['strBreed'],
            url = i['strUrl'],
            object = i['strObject'],
        )
        cats_data.save(config("DATABASE"))
        all_breeds = Cat.objects.all().filter("id")

    return HttpResponse(all_breeds)

# def get_breeds(request):
#     all_breeds = {}
#     if 'breed' in request.GET:
#         breed = request.GET['breed']
#         url = 'https://api.thecatapi.com/v1/breeds' % breed
#         headers = {
#         'x-api-key': config("API_KEY")
#         }
#         response = requests.get(url, headers=headers)
#         data = response.json()
#         cats = data['cats']

#         for i in cats:
#             cats_data = Cat(
#                 breed = i['strBreed'],
#                 url = i['strUrl'],
#                 object = i['strObject'],
#             )
#             cats_data.save()
#             all_breeds = Cat.objects.all().order_by('id')

#     return HttpResponse(request, {'all_breeds': all_breeds})


# def breed_detail(request, id):
#     breed = CatBreed.objects.get(id=id)
#     headers = {
#         'x-api-key': config("API_KEY")
#     }
#     response = requests.get('https://api.thecatapi.com/v1/images/search?limit=3', headers=headers)
#     breeds = response.json()
#     return HttpResponse(request, {'breeds': breed})
