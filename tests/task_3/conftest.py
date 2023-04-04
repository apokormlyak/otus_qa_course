import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        '--url',
        default='https://ya.ru',
        help='Test url'
    )
    parser.addoption(
        '--status_code',
        default='200',
        help='Status code'
    )
    parser.addoption(
        '--method',
        default='get',
        choices=['get', 'post', 'put', 'delete']
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture
def status_code(request):
    return request.config.getoption('--status_code')


@pytest.fixture
def method(request):
    return getattr(requests, request.config.getoption('--method'))


