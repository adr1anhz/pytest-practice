import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_search(browser):
    browser.get("https://www.duckduckgo.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("pytest selenium")
    search_box.submit()
    assert "pytest selenium" in browser.title.lower()

def test_login(browser):
    browser.get("https://demo.applitools.com/")
    login = browser.find_element(By.ID, "username")
    login.send_keys("testowyuser123")
    password = browser.find_element(By.ID, "password")
    password.send_keys("haslo123123")
    submit = browser.find_element(By.ID, "log-in")
    submit.click()
    time.sleep(5)
    assert "app.html" in browser.current_url