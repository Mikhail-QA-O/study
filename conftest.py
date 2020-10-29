import requests
import pytest


def pytest_addoption(parser):
    parser.addoption(
        '--url',
        action='store',
        default='http://jsonplaceholder.typicode.com/todos/',
        help='Request base url'

    )


@pytest.fixture(scope='function')
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='function')
def session():
    return requests.Session()
