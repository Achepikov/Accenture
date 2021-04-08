import pytest
from selenium import webdriver
import os

safari_driver_locator = r""
firefox_driver_locator = r""
URL = "https://www.accenture.com/us-en"

def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")


@pytest.fixture
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        driver = webdriver.Chrome(get_chrome_drive_locator())
        driver.get(URL)
    elif browser_param == "firefox":
        driver = webdriver.Firefox(firefox_driver_locator)
    elif browser_param == "safari":
        driver = webdriver.Safari(safari_driver_locator)
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.execute_script("document.body.style.zoom='100 %'")
    driver.maximize_window()
    driver.implicitly_wait(15)
    request.addfinalizer(driver.close)
    request.cls.driver = driver
    return driver


@pytest.fixture(params=["chrome", "safari", "firefox"])
def parametrize_browser(request):
    browser_param = request.param
    if browser_param == "chrome":
        driver = webdriver.Chrome()
    elif browser_param == "firefox":
        driver = webdriver.Firefox()
    elif browser_param == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")

    driver.implicitly_wait(5)
    request.addfinalizer(driver.quit)
    request.cls.driver = driver
    return driver


def get_chrome_drive_locator():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'Drivers/chromedriver.exe')
    return filename
