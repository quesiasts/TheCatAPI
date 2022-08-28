import pytest
from factories import CatBreedFactory, CatFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def test_validate_cat_name():
    cat_name = CatFactory(breed="angorá")
    assert cat_name.breed == "abys"


@pytest.fixture
def test_validate_cat_breed_name():
    cat_name = CatBreedFactory(name="amora")
    assert cat_name.name == "moby dick"
