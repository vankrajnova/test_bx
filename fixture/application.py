from selenium import webdriver
from fixture.session import SessionHelper
from fixture.register import RegisterHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.register = RegisterHelper(self)
        self.base_url = base_url



    def is_valid(self): # блок исключений
        try:
            self.wd.current_url
            return True
        except:
            return False


    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)


    def open_auth_form(self):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_css_selector("span.pseudolink.link-white").click()


    def check_empty(self, success):
        wd = self.wd
        if (len(wd.find_elements_by_xpath(".//*[@id='auth_form']/div/form/div/div[1]/p/font")) != 0):
            success = True
            print(True)
        else:
            if (len(wd.find_element_by_xpath(".//*[@id='auth_form']/div/form/div/div[1]/p/font")) == 0):
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


    def open_personal_account(self):
        wd = self.wd
        wd.find_element_by_xpath(".//*[@id='top']/div/div[2]/div/form/div/a/span").click()


    def destroy(self):
        self.wd.quit()