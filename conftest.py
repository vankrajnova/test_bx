import json
import pytest
from fixture.application import Application


fixture = None
target = None


@pytest.fixture(scope="session", autouse=True)
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        with open(request.config.getoption("--target")) as config_file:
            target = json.load(config_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default = "firefox")
    parser.addoption("--target", action="store", default="target.json")



