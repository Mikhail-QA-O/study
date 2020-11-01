import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help="Browser. Valid options are firefox, ie and chrome",
    )
    parser.addoption(
        '--url',
        action='store',
        default='https://demo.opencart.com/',
        help='Base url'

    )


@pytest.fixture(scope='function')
def base_url(request):
    return request.config.getoption('--url')


@pytest.fixture()
def driver(request):
    driver = None
    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        driver = webdriver.ChromeOptions()
        driver.add_argument("--headless")
        driver = webdriver.Chrome(executable_path=r'drivers/chromedriver.exe', options=driver)
    elif browser == 'firefox':
        driver = webdriver.FirefoxOptions()
        driver.add_argument("--headless")
        driver = webdriver.Firefox(executable_path='drivers/geckodriver.exe', options=driver)
    elif browser == 'ie':
        driver = webdriver.IeOptions()
        driver.add_argument("--headless")
        driver = webdriver.Ie(executable_path='drivers/IEDriverServer.exe', options=driver)
    driver.maximize_window()
    yield driver
    driver.quit()
