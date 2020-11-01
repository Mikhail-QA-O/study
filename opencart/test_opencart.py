from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

button_my_account = '.pull-right li.dropdown a.dropdown-toggle'
button_continue = 'input.btn.btn-primary'


def test_open_wk(driver, base_url):
    driver.get(base_url)
    assert driver.current_url == base_url

    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, button_my_account)),
                                    "Кнопка My Account не отображается на странице")

    driver.get(base_url + '/index.php?route=account/register')

    WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, button_continue)),
                                    "Кнопка Continue не отображается на странице")
