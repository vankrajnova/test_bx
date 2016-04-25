from model.info import Info

def test_register(app):
    app.register.create_register_form(Info(name="Тест", last_name="Тестовая", login="login", password="123456", confirm_password="123456", email="a@ru", phone="777 777-77-77"))


def test_register_empty_form(app):
    app.register.create_register_form(Info(name="Тест", last_name="Тестовая", login="", password="", confirm_password="",
                 email="", phone="777 777-77-77"))






