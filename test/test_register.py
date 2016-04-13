from model.info import Info

def test_register(app):
    success = True
    app.register.create_register_form(Info(name="Тест", last_name="Тестовая", login="login", password="123456", confirm_password="123456", email="a@ru", phone="777 777-77-77"))
    success = app.register.check_register(success)
    app.register.verification_phone(success)


def test_register_empty_form(app):
    success = True
    app.register.create_register_form(Info(name="Тест", last_name="Тестовая", login="", password="", confirm_password="",
                 email="", phone=""))
    success = app.register.check_register_empty(success)
    app.register.return_to_register_form(success)
    return success





