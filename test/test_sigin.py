# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.user import User


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_login(app):
    success = True
    app.session.login(User(user_login="bxuser", user_password="bxuser"))
    success = app.check_success(success)
    app.session.logout(success)


def test__empty(app):
    success = True
    app.session.login(User(user_login="", user_password=""))
    success = app.check_empty(success)
    app.session.close_auth_form(success)

def test__empty_login(app):
    success = True
    app.session.login(User(user_login="", user_password="bxuser"))
    success = app.check_empty(success)
    app.session.close_auth_form(success)



