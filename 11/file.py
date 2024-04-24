from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

sbis_site = 'https://test.sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
driver = webdriver.Chrome()

try:
    driver.get(sbis_site)
    sleep(2)
    assert driver.current_url == sbis_site, 'Не верно открыт сайт'
    assert driver.title == sbis_title, 'Не верный заголовок'
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4, 'Должно быть 4 вкладки'

    sleep(2)
    start_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Button--xs')
    assert start_btn.text == 'Начать работу'
    assert start_btn.get_attribute('title') == 'Начать работу'
    assert start_btn.is_displayed()
    start_btn.click()
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-InputBase__nativeField_caretFilled.controls-InputBase__nativeField_caretFilled_theme_default')
    login.send_keys('my_login', Keys.ENTER)
    assert login.get_attribute('value') == 'my_login'
    password = driver.find_element(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default')
    password.send_keys('password')
finally:
    driver.quit()
