import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from help import scroll_to


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()

#task_1

def test_login(driver_chrome):
    driver_chrome.get("https://thedemosite.co.uk/login.php")
    xpath = '//*[@id="saveform"]/div/center/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/p/input'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.send_keys('username')
    xpath_2 = '//*[@id="saveform"]/div/center/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/p/input'
    element_2 = driver_chrome.find_element(By.XPATH, xpath_2)
    element_2.send_keys('asdfg')
    xpath_3 = '//*[@id="saveform"]/div/center/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/p/input'
    element_3 = driver_chrome.find_element(By.XPATH, xpath_3)
    element_3.click()

    
#task_2

def test_site(driver_chrome):
    driver_chrome.get("https://demo.guru99.com/test/newtours/register.php")
    xpath = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/input'
    first_name = driver_chrome.find_element(By.XPATH, xpath)
    first_name.send_keys('Vlad')


    xpath_2 = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[3]/td[2]/input'
    last_name = driver_chrome.find_element(By.XPATH, xpath_2)
    last_name.send_keys('Ratnikov')


    xpath_3 = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[4]/td[2]/input'
    phone = driver_chrome.find_element(By.XPATH, xpath_3)
    phone.send_keys('5556555')


    xpath_4 = '//*[@id="userName"]'
    email = driver_chrome.find_element(By.XPATH, xpath_4)
    email.send_keys('kk@mail.ru')


    xpath_5 = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[7]/td[2]/input'
    address = driver_chrome.find_element(By.XPATH, xpath_5)
    address.send_keys('ulica')


    xpath_6 = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[8]/td[2]/input'
    city = driver_chrome.find_element(By.XPATH, xpath_6)
    city.send_keys('soligorsk')


    xpath_7 = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/input'
    state = driver_chrome.find_element(By.XPATH, xpath_7)
    state.send_keys('minsk')


    xpath_8 = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[10]/td[2]/input'
    code = driver_chrome.find_element(By.XPATH, xpath_8)
    code.send_keys('123443')


    xpath_9 = '//*[@id="email"]'
    user_name = driver_chrome.find_element(By.XPATH, xpath_9)
    user_name.send_keys('style')


    xpath_10 = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[14]/td[2]/input'
    password = driver_chrome.find_element(By.XPATH, xpath_10)
    password.send_keys('123456')


    xpath_11 = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[15]/td[2]/input'
    password_c = driver_chrome.find_element(By.XPATH, xpath_11)
    password_c.send_keys('123456')


    xpath_12 = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[11]/td[2]/select'
    country = driver_chrome.find_element(By.XPATH, xpath_12)
    country.click()
    xpath_13 = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[11]/td[2]/select/option[22]'
    choose = driver_chrome.find_element(By.XPATH,xpath_13)
    choose.click()

    xpath_14 = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[17]/td/input'
    send = driver_chrome.find_element(By.XPATH, xpath_14)
    send.click()

    xpath_15 = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[1]/font/b'
    fio = driver_chrome.find_element(By.XPATH, xpath_15)
    assert fio.text == "Dear Vlad Ratnikov,"

    xpath_16 = '/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td/p[3]/font/b'
    u_n = driver_chrome.find_element(By.XPATH, xpath_16)
    assert u_n.text == "Note: Your user name is style."


#task_3

def test_site_anime_url(driver_chrome):
    driver_chrome.get('https://animego.org/')
    xpath = '/html/body/div[2]/header/nav/div/div/ul[1]/li[1]/a'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.click()
    assert driver_chrome.current_url == 'https://animego.org/anime'


def test_anime_attribute(driver_chrome):
    driver_chrome.get('https://animego.org/')
    xpath = '/html/body/div[2]/header/nav/div/div/ul[1]/li[1]/a'
    element = driver_chrome.find_element(By.XPATH, xpath)
    assert element.get_attribute('href') in 'https://animego.org/anime'

def test_anime_char(driver_chrome):
    driver_chrome.get('https://animego.org/')
    xpath = '/html/body/div[2]/header/nav/div/div/ul[1]/li[3]/a'
    element = driver_chrome.find_element(By.XPATH, xpath)
    element.click()
    assert driver_chrome.title == 'Список аниме персонажей'

def test_anime_scroll(driver_chrome):
    driver_chrome.get('https://animego.org/')
    scroll_to(driver_chrome)
    time.sleep(6)


def test_anime_text(driver_chrome):
    driver_chrome.get('https://animego.org/')
    css = 'body > div:nth-child(3) > header > nav > div > div > ul.nav.navbar-nav.mr-auto.ml-2 > li:nth-child(1) > a'
    element = driver_chrome.find_element(By.CSS_SELECTOR, css)
    assert element.text == "Аниме"
   





