# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

sbis_site = 'https://fix-online.sbis.ru/'
contacts_url = 'https://fix-online.sbis.ru/page/dialogs'

driver = webdriver.Chrome()
sleep(1)

try:
    driver.maximize_window()
    driver.get(sbis_site)
    sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, '.controls-InputBase__nativeField_caretFilled.controls-InputBase__nativeField_caretFilled_theme_default')
    login.send_keys('пчелкин', Keys.ENTER)
    sleep(3)
    password = driver.find_element(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled.controls-Password__nativeField_caretFilled_theme_default')
    password.send_keys('пчелкин123', Keys.ENTER)
    sleep(4)
    driver.get(contacts_url)
    sleep(2)
    plus = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')
    plus.click()
    sleep(2)
    find = driver.find_element(By.CSS_SELECTOR, '.controls_search_theme-default.controls-Search__buttons')
    find.send_keys('пчелкин алексей')
    fio_find = driver.find_element(By.CSS_SELECTOR, '[title="Пчелкин Алексей Павлович"]')
    fio_find.click()
    sleep(3)
finally:
    driver.quit()
