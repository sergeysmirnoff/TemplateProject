from selenium.webdriver.common.by import By


# this is a mapper for page: https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com
class Basic_login:

    def __init__(self, sd):
        self.sd = sd

    def ze_snippet_script(self):
        return self.sd.get_element("//*[@id='ze-snippet']", "xpath")

    def navigation_nav(self):
        return self.sd.get_element("//*[@id='navigation']", "xpath")

    def email_text(self):
        return self.sd.get_element("//*[@id='modalusername']", "xpath")

    def current_password_password(self):
        return self.sd.get_element("//*[@id='current-password']", "xpath")

    def g_recaptcha_response_textarea(self):
        return self.sd.get_element("//*[@id='g-recaptcha-response']", "xpath")

    def root_div(self):
        return self.sd.get_element("//*[@id='root']", "xpath")

    def launcher_iframe(self):
        return self.sd.get_element("//*[@id='launcher']", "xpath")

    def login_btn(self):
        return self.sd.get_element("//*[@class='Button_button__URNp+ Button_primary__d2Jt3 Button_fullwidth__0HLEu']", "xpath")
