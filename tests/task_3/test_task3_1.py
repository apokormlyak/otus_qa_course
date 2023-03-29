import pytest
import jsonschema
import requests
import json
from tests.task_3.utils import breeds_list, sub_breeds_list
from tests.task_3.helpers.urls import *
from tests.task_3.helpers.schema_validation import *
from pathlib import Path


def test_all_breeds():
    response = requests.get(url=DOG_API_BASE_URL+LIST_ALL_BREEDS)
    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=ListAllBreeds.schema)
    breeds = iter(response.json()['message'])
    by_alphabet = set(map(lambda x: next(breeds) < next(breeds), breeds))
    assert len(by_alphabet) == 1
    assert by_alphabet == {True}

    with open('breeds_list.json', 'w') as f:
        json.dump(response.json(), f, indent=4)


def test_random_image():
    response = requests.get(url=DOG_API_BASE_URL + RANDOM_IMAGE)
    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=RandomImage.schema)


@pytest.mark.parametrize('path_parameter, images_count', [(3, 3), (50, 50), (100, 50)])
def test_random_image_list(path_parameter, images_count):
    response = requests.get(url=DOG_API_BASE_URL + RANDOM_IMAGE + f'/{path_parameter}')
    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=RandomImageList.schema)
    assert len(response.json()['message']) == images_count
    for dog in response.json()['message']:
        assert Path(dog).suffix == '.jpg'


@pytest.mark.parametrize('breed', breeds_list)
def test_image_by_breed(breed):
    response = requests.get(url=BREED_API_BASE_URL + f'{breed}/images')
    response_random = requests.get(url=BREED_API_BASE_URL + f'{breed}/images/random')
    assert response.status_code == 200
    assert response_random.status_code == 200


@pytest.mark.parametrize('breed, sub_breed', sub_breeds_list)
def test_image_by_sub_breed(breed, sub_breed):
    response = requests.get(url=BREED_API_BASE_URL + f'{breed}/{sub_breed[0]}/images')
    response_random = requests.get(url=BREED_API_BASE_URL + f'{breed}/{sub_breed[0]}/images/random')
    assert response.status_code == 200
    assert response_random.status_code == 200



