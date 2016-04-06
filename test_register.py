# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from personality import Personality
from information import Information

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_register(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    



    def open_home_page(self, wd):
        wd.get("http://bx.marya.ru/")

    def open_auth_form(self, wd):
        wd.find_element_by_css_selector("span.pseudolink.link-white").click()

    def login(self, wd, personality):
        wd.find_element_by_id("user_login").click()
        wd.find_element_by_id("user_login").clear()
        wd.find_element_by_id("user_login").send_keys(personality.user_login)
        wd.find_element_by_name("USER_PASSWORD").click()
        wd.find_element_by_name("USER_PASSWORD").clear()
        wd.find_element_by_name("USER_PASSWORD").send_keys(personality.user_password)
        wd.find_element_by_name("Login").click()

    def open_personal_account(self, wd):
        wd.find_element_by_xpath("//div[@id='top']/div/div[2]/div/form/div/a/span").click()

    def logout(self, wd):
        wd.find_element_by_xpath("//div[@class='profile_menu']//a[.='Выйти']").click()


    def return_to_auth_form(self, wd):
        wd.find_element_by_css_selector("span.pseudolink.link-white").click()

    def open_registration_form(self, wd):
        wd.find_element_by_link_text("Зарегистрироваться").click()

    def create_registration_form(self, wd, information):
        wd.find_element_by_name("REGISTER[NAME]").click()
        wd.find_element_by_name("REGISTER[NAME]").clear()
        wd.find_element_by_name("REGISTER[NAME]").send_keys(information.name)
        wd.find_element_by_name("REGISTER[LAST_NAME]").click()
        wd.find_element_by_name("REGISTER[LAST_NAME]").clear()
        wd.find_element_by_name("REGISTER[LAST_NAME]").send_keys(information.last_name)
        wd.find_element_by_name("REGISTER[LOGIN]").click()
        wd.find_element_by_name("REGISTER[LOGIN]").clear()
        wd.find_element_by_name("REGISTER[LOGIN]").send_keys(information.username)
        wd.find_element_by_name("REGISTER[PASSWORD]").click()
        wd.find_element_by_name("REGISTER[PASSWORD]").clear()
        wd.find_element_by_name("REGISTER[PASSWORD]").send_keys(information.password)
        wd.find_element_by_name("REGISTER[CONFIRM_PASSWORD]").click()
        wd.find_element_by_name("REGISTER[CONFIRM_PASSWORD]").clear()
        wd.find_element_by_name("REGISTER[CONFIRM_PASSWORD]").send_keys(information.confirm_password)
        wd.find_element_by_name("REGISTER[EMAIL]").click()
        wd.find_element_by_name("REGISTER[EMAIL]").clear()
        wd.find_element_by_name("REGISTER[EMAIL]").send_keys(information.email)
        if not wd.find_element_by_xpath("//select[@class='select-phone-code']//option[1]").is_selected():
            wd.find_element_by_xpath("//select[@class='select-phone-code']//option[1]").click()
        wd.find_element_by_name("REGISTER[PERSONAL_PHONE]").click()
        wd.find_element_by_name("REGISTER[PERSONAL_PHONE]").clear()
        wd.find_element_by_name("REGISTER[PERSONAL_PHONE]").send_keys(information.phone)
        wd.find_element_by_css_selector("div.jq-selectbox__trigger-arrow").click()
        wd.find_element_by_xpath("//div[@class='all-wrap']//li[.='Краснодар']").click()
        wd.find_element_by_xpath(
            "//div[@class='all-wrap']/div[3]/div/div[2]/form[1]/div[9]/div[2]/div/div[1]/div[2]").click()
        wd.find_element_by_xpath(
            "//div[@class='all-wrap']/div[3]/div/div[2]/form[1]/div[9]/div[2]/div/div[2]/ul/li[1]").click()

    def next_step(self, wd):
        wd.find_element_by_name("next_step").click()

    def test_register(self):
        wd = self.wd

        self.open_home_page(wd)
        self.open_auth_form(wd)
        self.login(wd, Personality(user_login="bxuser", user_password="bxuser"))
        self.open_personal_account(wd)
        self.logout(wd)
        self.return_to_auth_form(wd)
        self.open_registration_form(wd)
        self.create_registration_form(wd, Information(name="Тест", last_name="Тестовая", username="testlogin", password="123456",
                                                      confirm_password="123456", email="test@marya.ru", phone="937 260-97-57"))
        self.next_step(wd)





    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
