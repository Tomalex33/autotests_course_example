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
    login.send_keys('тест', Keys.ENTER)
    sleep(3)
    password = driver.find_element(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled.controls-Password__nativeField_caretFilled_theme_default')
    password.send_keys('тест', Keys.ENTER)
    sleep(4)
    driver.get(contacts_url)
    sleep(2)
    plus = driver.find_element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]')
    plus.click()
    sleep(2)
    find = driver.find_element(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-Search__nativeField_caretEmpty.controls-Search__nativeField_caretEmpty_theme_default.controls-InputBase__nativeField_hideCustomPlaceholder')
    find.click()
    sleep(2)
    find.send_keys('Тест Сверки')
    sleep(3)
    fio_find = driver.find_element(By.CSS_SELECTOR, '[title="Тест Сверки"]')
    fio_find.click()
    sleep(3)
    messege = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    messege.click()
    messege.send_keys('Проверка')
    sleep(2)
    send_messege = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    send_messege.click()
    sleep(2)
    messege_in_list = driver.find_element(By.CSS_SELECTOR, '[data-qa="items-container"] [data-qa="item"].controls-ListView__itemV-relative.controls-ListView__itemV.controls-ListView__item_default.js-controls-ListView__editingTarget.controls-ListView__itemV_cursor-pointer.controls-ListView__item_showActions.controls-ListView__item_showCheckbox.js-controls-ListView__measurableContainer.controls-ListView__item__marked_default.controls-ListView__item_highlightOnHover.controls-hover-background-default.msg-dialogs-item-wrapper')
    sleep(1)
    assert messege_in_list.is_displayed()
    pmo_button = driver.find_element(By.CSS_SELECTOR, '[title="Отметить"]')
    pmo_button.click()
    sleep(1)
    check_box = driver.find_element(By.CSS_SELECTOR, '[data-qa="controls-CheckboxMarker"]')
    check_box.click()
    sleep(1)
    delete_msg = driver.find_element(By.CSS_SELECTOR, '[data-qa="remove"]')
    delete_msg.click()
    sleep(1)
    empty_msg = driver.find_element(By.CSS_SELECTOR, '.hint-Template__text_message.hint-Template__text_message_m')
    assert empty_msg.text == 'В этой папке нет сообщений'
    print("Тест прошел")
    sleep(2)
finally:
    driver.quit()
