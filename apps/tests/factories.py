import factory

from ..cat.models import Cat, CatBreed


class CatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cat

    url = "https://cdn2.thecatapi.com/images/0XYvRd7oD.jpg"
    breed = "abys"
    object = "black hat"
    image = "0XYvRd7oD.jpg"


class CatBreedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CatBreed

    name = "Abyssinian"
    origin = "Egypt"
    temperament = "Active, Energetic, Independent, Intelligent, Gentle"
