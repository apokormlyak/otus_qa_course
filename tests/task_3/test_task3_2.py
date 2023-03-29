import pytest
import jsonschema
import requests
from tests.task_3.helpers.urls import *
from tests.task_3.helpers.schema_validation import *


def test_list_breweries():
    response = requests.get(url=BREWERY_BASE_URL)
    assert response.status_code == 200
    jsonschema.validate(instance=response.json(), schema=Brewery.schema)


@pytest.mark.parametrize('query_parameter, value', [('by_city', 'san_diego'), ('by_city', 'austin')])
def test_filter_by_city(query_parameter, value):
    response = requests.get(url=BREWERY_BASE_URL + f'?{query_parameter}={value}')
    assert response.status_code == 200
    for brewery in response.json():
        assert value.replace('_', ' ') in brewery['city'].lower()


@pytest.mark.parametrize('query_parameter, value', [('by_name', 'cooper'), ('by_name', 'heineken')])
def test_filter_by_name(query_parameter, value):
    response = requests.get(url=BREWERY_BASE_URL + f'?{query_parameter}={value}')
    assert response.status_code == 200
    for brewery in response.json():
        assert value in brewery['name'].lower()


@pytest.mark.parametrize('query_parameter, value', [('by_state', 'new_york'), ('by_state', 'california')])
def test_filter_by_name(query_parameter, value):
    response = requests.get(url=BREWERY_BASE_URL + f'?{query_parameter}={value}')
    assert response.status_code == 200
    for brewery in response.json():
        assert value.replace('_', ' ') in brewery['state'].lower()


def test_random_brewery():
    response = requests.get(url=BREWERY_BASE_URL + BREWERY_RANDOM)
    assert response.status_code == 200
    assert len(response.json()) == 1
    jsonschema.validate(instance=response.json(), schema=Brewery.schema)


@pytest.mark.parametrize('number, length', [(3, 3), (50, 50), (100, 50)])
def test_random_brewery_size(number, length):
    response = requests.get(url=BREWERY_BASE_URL + BREWERY_RANDOM + f'?size={number}')
    assert response.status_code == 200
    assert len(response.json()) == length


@pytest.mark.xfail(reason="По запросу приходят лишние пивоварни", strict=True)
@pytest.mark.parametrize('search_by', ['cat', 'dog', 'bird'])
def test_random_brewery_size(search_by):
    response = requests.get(url=BREWERY_BASE_URL + BREWERY_SEARCH + f'{search_by}')
    assert response.status_code == 200
    for brewery in response.json():
        assert search_by in brewery['name'].lower()
