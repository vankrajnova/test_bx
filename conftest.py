import pytest
from fixture.application import Application

fixture = None


@pytest.fixture(scope="session", autouse=True)
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

