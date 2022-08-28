import logging

from rest_framework import serializers

from .models import Cat, CatBreed

logger = logging.getLogger(__name__)


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = "__all__"

    def is_wrong_data(self):
        request = self.context.get("request", None)
        if request and "x-api-key" not in request.headers:
            logger.warning("cats_serializer, event=not_using_api_key")

    def update(self, instance, validate_data):
        return Cat.objects.update_or_create(
            instance,
            **validate_data,
        )


class CatBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatBreed
        fields = "__all__"

    def is_wrong_data(self):
        request = self.context.get("request", None)
        if request and "x-api-key" not in request.headers:
            logger.warning("cats_breed_serializer, event=not_using_api_key")

    def update(self, instance, validate_data):
        return CatBreed.objects.update_or_create(
            instance,
            **validate_data,
        )
