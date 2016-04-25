import json
import pytest
import os.path
from fixture.application import Application


fixture = None
target = None


@pytest.fixture(scope="session", autouse=True)
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default = "firefox")
    parser.addoption("--target", action="store", default="target.json")



