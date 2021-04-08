from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def __element(self, selector: dict, index: int, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_elements(by, selector)[index]

    def _click(self, selector, index=0):
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()

    def _input(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, link_text=None, index=0, wait=5):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
            WebDriverWait(self.driver, wait).until(
                EC.visibility_of_element_located((by, selector))
            )

    def _get_element_attribute(self, selector, attribute, index=0):
        return self.__element(selector, index).get_attribute(attribute)

    def _upload(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.send_keys(value)

    def _mouse_over(self, selector, index=0):
        ActionChains(self.driver) \
            .move_to_element(self.__element(selector, index)).perform()

    def _element(self, selector, index=0):
        return self.__element(selector, index)

    def _get_current_url(self):
        return self.driver.current_url

    def _exist_element(self, selector: dict, link_text: str = None):
        self.driver.implicitly_wait(10)
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        s = len(self.driver.find_elements(by, selector))
        if s > 0:
            return True
        else:
            return False
