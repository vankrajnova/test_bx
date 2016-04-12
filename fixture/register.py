class RegisterHelper:

    def __init__(self, app):
        self.app = app


    def open_register_form(self):
        wd = self.app.wd
        self.app.open_auth_form()
        wd.find_element_by_link_text("Зарегистрироваться").click()


    def create_register_form(self, info):
        wd = self.app.wd
        self.open_register_form()
        wd.find_element_by_name("REGISTER[NAME]").click()
        wd.find_element_by_name("REGISTER[NAME]").clear()
        wd.find_element_by_name("REGISTER[NAME]").send_keys(info.name)
        wd.find_element_by_name("REGISTER[LAST_NAME]").click()
        wd.find_element_by_name("REGISTER[LAST_NAME]").clear()
        wd.find_element_by_name("REGISTER[LAST_NAME]").send_keys(info.last_name)
        wd.find_element_by_name("REGISTER[LOGIN]").click()
        wd.find_element_by_name("REGISTER[LOGIN]").clear()
        wd.find_element_by_name("REGISTER[LOGIN]").send_keys(info.login)
        wd.find_element_by_name("REGISTER[PASSWORD]").click()
        wd.find_element_by_name("REGISTER[PASSWORD]").clear()
        wd.find_element_by_name("REGISTER[PASSWORD]").send_keys(info.password)
        wd.find_element_by_name("REGISTER[CONFIRM_PASSWORD]").click()
        wd.find_element_by_name("REGISTER[CONFIRM_PASSWORD]").clear()
        wd.find_element_by_name("REGISTER[CONFIRM_PASSWORD]").send_keys(info.confirm_password)
        wd.find_element_by_name("REGISTER[EMAIL]").click()
        wd.find_element_by_name("REGISTER[EMAIL]").clear()
        wd.find_element_by_name("REGISTER[EMAIL]").send_keys(info.email)
        wd.find_element_by_name("REGISTER[PERSONAL_PHONE]").click()
        wd.find_element_by_name("REGISTER[PERSONAL_PHONE]").clear()
        wd.find_element_by_name("REGISTER[PERSONAL_PHONE]").send_keys(info.phone)
        wd.find_element_by_css_selector("div.jq-selectbox__select-text").click()
        wd.find_element_by_xpath("//div[@class='all-wrap']//li[.='Новокуйбышевск']").click()
        wd.find_element_by_xpath(
            "//div[@class='all-wrap']/div[3]/div/div[2]/form[1]/div[9]/div[2]/div/div[1]/div[1]").click()
        wd.find_element_by_xpath(
            "//div[@class='all-wrap']/div[3]/div/div[2]/form[1]/div[9]/div[2]/div/div[2]/ul/li").click()
        wd.find_element_by_name("next_step").click()



    def check_register_empty(self, success):
        wd = self.app.wd
        if (len(wd.find_elements_by_xpath("//div[@class='all-wrap']//button[.='Назад']")) == 0):
            success = True
            print(True)
        else:
            if (len(wd.find_element_by_xpath("//div[@class='all-wrap']//button[.='Назад']")) != 0):
                success = False
                print(False)
        return success


    def check_register(self, success):
        wd = self.app.wd
        if (len(wd.find_elements_by_xpath("//div[@class='all-wrap']//button[.='Назад']")) != 0):
            success = True
            print(True)
        else:
            if (len(wd.find_element_by_xpath("//div[@class='all-wrap']//button[.='Назад']")) == 0):
                success = False
                print(False)
        return success


    def return_to_register_form(self, success):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='all-wrap']//button[.='Назад']").click()


    def verification_phone(self, success):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='all-wrap']//button[.='Отправить']").click()
