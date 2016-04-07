# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_sig_in(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://bx.marya.ru/")

    def open_auth_form(self):
        wd = self.wd
        wd.find_element_by_css_selector("span.pseudolink.link-white").click()

    def login(self, user_password, user_login):
        wd = self.wd
        wd.find_element_by_id("user_login").click()
        wd.find_element_by_id("user_login").clear()
        wd.find_element_by_id("user_login").send_keys(user_login)
        wd.find_element_by_name("USER_PASSWORD").click()
        wd.find_element_by_name("USER_PASSWORD").clear()
        wd.find_element_by_name("USER_PASSWORD").send_keys(user_password)
        wd.find_element_by_name("Login").click()


    def close_auth_form(self, success):
        wd = self.wd
        wd.find_element_by_css_selector("div.mfp-close.cn-modal-close").click()
        self.assertTrue(success)


    def open_personal_account(self):
        wd = self.wd
        wd.find_element_by_xpath(".//*[@id='top']/div/div[2]/div/form/div/a/span").click()


    def logout(self, success):
        wd = self.wd
        wd.find_element_by_xpath("//div[@class='profile_menu']//a[.='Выйти']").click()
        self.assertTrue(success)


    def test_login_empty_login(self):
        success = True
        wd = self.wd
        self.open_home_page()
        self.open_auth_form()
        self.login(user_login="", user_password="bxuser")
        if not (len(wd.find_elements_by_css_selector("font.errortext")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.close_auth_form(success)


    def test_login_empty_password(self):
        success = True
        wd = self.wd
        self.open_home_page()
        self.open_auth_form()
        self.login(user_login="bxuser", user_password="")
        if not (len(wd.find_elements_by_css_selector("font.errortext")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.close_auth_form(success)


    def test_login_empty(self):
       success = True
       wd = self.wd
       self.open_home_page()
       self.open_auth_form()
       self.login(user_login="", user_password="")
       if not (len(wd.find_elements_by_css_selector("font.errortext")) != 0):
           success = False
           print("verifyElementPresent failed")
       self.close_auth_form(success)


    def test_login(self):
        success = True
        wd = self.wd
        self.open_home_page()
        self.open_auth_form()
        self.login(user_login="bxuser", user_password="bxuser")
        if not (len(wd.find_elements_by_xpath(".//*[@id='top']/div/div[2]/div/form/div/a/span")) != 0):
            success = False
            print("verifyElementPresent failed")
        self.open_personal_account()
        self.logout(success)



    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
