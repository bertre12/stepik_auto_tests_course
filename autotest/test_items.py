from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_find_card_button(browser):
    browser.get(link)
    button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert button
    time.sleep(10)
