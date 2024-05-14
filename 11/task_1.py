# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

sbis_site = 'https://sbis.ru/'
sbis_site_about = 'https://tensor.ru/about'

driver = webdriver.Chrome()
sleep(1)

try:
    driver.maximize_window()
    driver.get(sbis_site)
    sleep(2)
    contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    contacts.click()
    sleep(2)
    banner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor.mb-12')
    banner.click()
    sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    power_of_people = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card')
    power_of_people.location_once_scrolled_into_view
    sleep(1)
    s = power_of_people.text[:12]
    assert s == 'Сила в людях'
    assert power_of_people.is_displayed()
    sleep(2)
    more_details = driver.find_element(By.CSS_SELECTOR, '[href="/about"].tensor_ru-Header__menu-link')
    more_details.click()
    assert driver.current_url == sbis_site_about
    print("Проверка прошла")
    sleep(2)
finally:
    driver.quit()

