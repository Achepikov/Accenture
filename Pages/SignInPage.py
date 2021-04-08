from Pages.BasePage import BasePage
from Locators import LocatorsSignIn


class SignInPage(BasePage):

    def set_email(self, email):
        self._input(LocatorsSignIn.email, email)
        return self

    def set_password(self, password):
        self._input(LocatorsSignIn.password, password)
        return self

    def click_sign_in(self):
        self._click(LocatorsSignIn.sign_in_btn)
        return self

    def get_error_message(self):
        return self._element(LocatorsSignIn.error_message).get_attribute('innerHTML')