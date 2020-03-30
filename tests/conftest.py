pytest_plugins = 'pytester'
import pytest

@pytest.fixture(scope='session')
def django_db_setup():
    print("django test")