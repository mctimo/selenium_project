import time as t
from datetime import datetime
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_button(browser):
    browser.get(link)
    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"), 'basket button not found'