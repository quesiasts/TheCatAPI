import pytest
from rest_framework.status import is_success

pytestmark = pytest.mark.django_db


def test_api_list(client, cat):
    response = client.get("cat:list")
    assert is_success(response.status_code)
