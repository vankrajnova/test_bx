import pytest
from fixture.application import Application

fixture = None


@pytest.fixture(scope="session", autouse=True)
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default = "firefox")
    parser.addoption("--baseUrl", action="store", default="http://bx.marya.ru/")



