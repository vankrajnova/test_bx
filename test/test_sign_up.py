# -*- coding: utf-8 -*-
from model.user import User



def test_login(app):
    success = True
    app.session.login(User(user_login="bxuser", user_password="bxuser"))
    success = app.check_success(success)
    app.session.logout(success)


def test_empty(app):
    success = True
    app.session.login(User(user_login="", user_password=""))
    success = app.check_empty(success)
    app.session.close_auth_form(success)


def test_empty_login(app):
    success = True
    app.session.login(User(user_login="", user_password="bxuser"))
    success = app.check_empty(success)
    app.session.close_auth_form(success)


def test_empty_password(app):
    success = True
    app.session.login(User(user_login="bxuser", user_password=""))
    success = app.check_empty(success)
    app.session.close_auth_form(success)


def test_error_login(app):
    success = True
    app.session.login(User(user_login="xzczzc", user_password="bxuser"))
    success = app.check_empty(success)
    app.session.close_auth_form(success)


def test_error_password(app):
    success = True
    app.session.login(User(user_login="bxuser", user_password="dfsdfs"))
    success = app.check_empty(success)
    app.session.close_auth_form(success)




