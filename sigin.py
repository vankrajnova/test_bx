# -*- coding: utf-8 -*-

from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login(app):
    success = True
    app.login(user_login="bxuser", user_password="bxuser")
    success = app.check_success(success)
    app.logout(success)


def test__login_empty(app):
    success = True
    app.login(user_login="", user_password="")
    success = app.check_empty(success)
    app.close_auth_form(success)



