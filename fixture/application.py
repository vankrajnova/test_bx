from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper

class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://bx.marya.ru/")


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
            if not (len(wd.find_element_by_xpath(".//*[@id='auth_form']/div/form/div/div[1]/p/font")) == 0):
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