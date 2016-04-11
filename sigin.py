# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class sigin(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://bx.marya.ru/")


    def open_auth_form(self):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_css_selector("span.pseudolink.link-white").click()


    def login(self, user_login, user_password):
        wd = self.wd
        self.open_auth_form()
        wd.find_element_by_id("user_login").click()
        wd.find_element_by_id("user_login").clear()
        wd.find_element_by_id("user_login").send_keys(user_login)
        wd.find_element_by_name("USER_PASSWORD").click()
        wd.find_element_by_name("USER_PASSWORD").clear()
        wd.find_element_by_name("USER_PASSWORD").send_keys(user_password)
        wd.find_element_by_name("Login").click()


    def check_empty (self, success):
        wd = self.wd
        if (len(wd.find_elements_by_xpath(".//*[@id='auth_form']/div/form/div/div[1]/p/font")) != 0):
            success = True
            print(True)
        else:
            if not(len(wd.find_element_by_xpath(".//*[@id='auth_form']/div/form/div/div[1]/p/font")) == 0):
                success = False
                print(False)
        return success


    def check_success(self, success):
        wd = self.wd
        if (len(wd.find_elements_by_xpath(".//*[@id='top']/div/div[2]/div/form/div/a/span")) != 0):
            success = True
            print(True)
        else:
            if (len(wd.find_elements_by_xpath(".//*[@id='top']/div/div[2]/div/form/div/a/span")) == 0):
                success = False
                print(False)
        return success


    def close_auth_form(self, success):
        wd = self.wd
        wd.find_element_by_css_selector("div.mfp-close.cn-modal-close").click()



    def open_personal_account(self):
        wd = self.wd
        wd.find_element_by_xpath(".//*[@id='top']/div/div[2]/div/form/div/a/span").click()


    def logout(self, success):
        wd = self.wd
        self.open_personal_account()
        wd.find_element_by_xpath("//div[@class='profile_menu']//a[.='Выйти']").click()





    def test_login(self):
        success = True
        self.login(user_login="bxuser", user_password="bxuser")
        success = self.check_success(success)
        self.logout(success)



    def test__login_empty(self):
        success = True
        self.login(user_login="", user_password="")
        success = self.check_empty(success)
        self.close_auth_form(success)



    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()