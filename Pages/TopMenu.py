from Pages.BasePage import BasePage
from Locators import LocatorsCommon


class TopMenu(BasePage):

    def click_sign_in(self):
        self._click(LocatorsCommon.sign_in_btn)
