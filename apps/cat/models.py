from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/photos')

class Cat(models.Model):
    url = models.URLField(max_length=200, help_text="armazena o endereço da foto")
    breed = models.CharField(max_length=100, null=False, help_text="armazena a raça")
    object = models.CharField(max_length=100, blank=True, help_text="armazena o tipo do objeto presente na foto")
    image = models.ImageField(storage=fs)

    def __str__(self):
        return self.breed

class CatBreed(models.Model):
    name = models.CharField(max_length=100, help_text="representa o nome da raça")
    origin = models.CharField(max_length=100, help_text="origem da raça")
    temperament = models.CharField(max_length=200, help_text="temperamentos da raça")

    def __str__(self):
        return self.name