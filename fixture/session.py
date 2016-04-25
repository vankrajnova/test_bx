

class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, user):
        wd = self.app.wd
        self.app.open_auth_form()
        wd.find_element_by_id("user_login").click()
        wd.find_element_by_id("user_login").clear()
        wd.find_element_by_id("user_login").send_keys(user.user_login)
        wd.find_element_by_name("USER_PASSWORD").click()
        wd.find_element_by_name("USER_PASSWORD").clear()
        wd.find_element_by_name("USER_PASSWORD").send_keys(user.user_password)
        wd.find_element_by_name("Login").click()



    def close_auth_form(self, success):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.mfp-close.cn-modal-close").click()


    def logout(self, success):
        wd = self.app.wd
        self.app.open_personal_account()
        wd.find_element_by_xpath("//div[@class='profile_menu']//a[.='Выйти']").click()





