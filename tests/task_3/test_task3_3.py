import pytest
import requests
from tests.task_3.helpers.urls import *


@pytest.mark.parametrize('resource', ['posts', 'comments', 'albums', 'photos', 'todos', 'users'])
def test_list_posts(resource):
    response = requests.get(url=JSON_PLACEHOLDER_BASE_URL + resource)
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.parametrize('post_id', range(1, 5))
def test_post_id(post_id):
    response = requests.get(url=JSON_PLACEHOLDER_BASE_URL + f'posts/{post_id}')
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()['id'] == post_id


@pytest.mark.parametrize('post_id', range(1, 5))
def test_get_comments_by_post_id(post_id):
    response = requests.get(url=JSON_PLACEHOLDER_BASE_URL + f'posts/{post_id}/comments')
    assert response.status_code == 200
    assert len(response.json()) > 0
    for comment in response.json():
        assert comment['postId'] == post_id


@pytest.mark.xfail(reason="В документации указано, что настоящих изменений на сервере не присходит, но удаление "
                          "иммитируется", strict=True)
@pytest.mark.parametrize('post_id', range(1, 5))
def test_delete_post(post_id):
    response = requests.get(url=JSON_PLACEHOLDER_BASE_URL + f'posts/{post_id}')
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()['id'] == post_id
    response_delete = requests.delete(url=JSON_PLACEHOLDER_BASE_URL + f'posts/{post_id}')
    assert response_delete.status_code == 200
    assert requests.get(url=JSON_PLACEHOLDER_BASE_URL + f'posts/{post_id}').json() == {}



@pytest.mark.xfail(reason="В документации указано, что настоящих изменений на сервере не присходит, но удаление "
                          "иммитируется", strict=True)
@pytest.mark.parametrize('post_id', range(1, 5))
def test_patching_source(post_id):
    response = requests.get(url=JSON_PLACEHOLDER_BASE_URL + f'posts/{post_id}')
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()['id'] == post_id
    data = {'title': 'Alisa'}
    patch_response = requests.patch(url=JSON_PLACEHOLDER_BASE_URL + f'posts/{post_id}', json=data)
    assert patch_response.status_code == 200
    after_patch_response = requests.get(url=JSON_PLACEHOLDER_BASE_URL + f'posts/{post_id}')
    assert after_patch_response.status_code == 200
    assert after_patch_response.json()['title'] == 'Alisa'
