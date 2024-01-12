import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print("Launching Chrome browser")
        driver = webdriver.Chrome()
    elif browser == 'edge':
        print("Launching Edge browser")
        driver = webdriver.Edge()
    elif browser == 'firefox':
        print("Launching Firefox browser")
        driver = webdriver.Firefox()
    else:
        print("headless mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)

    # driver.maximize_window()
    yield driver
    driver.quit()


def pytest_metadata(metadata):
    metadata["Project Name"] = "CredKart"
    metadata["Environment"] = "QA Environment"
    metadata["Module"] = "User profile"
    metadata["Tester"] = "Kaleshwari"
    metadata.pop("Plugins", None)



@pytest.fixture(params=[
        ("tester4@gmail.com", "tester123", "Pass"),
        ("tester4@gmail.com1", "tester123", "Fail"),
        ("tester4@gmail.com", "tester1234","Fail"),
        ("tester4@gmail.com1","tester1234","Fail")

])
def getDataForLogin(request):
    return request.param






