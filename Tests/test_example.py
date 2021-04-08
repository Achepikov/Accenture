import time

import pytest
from Pages import SignInPage, TopMenu
from Functions import FunctionsUtils


@pytest.mark.usefixtures("browser")
class Test_example:
    def test_example(self, browser):
        TopMenu(browser).click_sign_in()
        time.sleep(5)
        SignInPage(browser)\
            .set_email('Alex@domain.com')\
            .set_password('123456789Aa!') \
            .click_sign_in()

        assert SignInPage.get_error_message().find('incorrect') != -1
