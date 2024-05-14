# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили

from selenium import webdriver
from atf.ui import *
from atf import log
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

sbis_site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
sbis_title = 'Вход в личный кабинет'
contacts_url = 'https://fix-online.sbis.ru/page/dialogs'
contacts_title = 'Контакты'


class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-InputBase__nativeField_caretFilled.controls-InputBase__nativeField_caretFilled_theme_default', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default', 'пароль')

class MainOnline(Region):
    plus = Element(By.CSS_SELECTOR, '[data-name="sabyPage-addButton"]', 'Кнопка добавить')
    find = CustomList(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-Search__nativeField_caretEmpty.controls-Search__nativeField_caretEmpty_theme_default.controls-InputBase__nativeField_hideCustomPlaceholder', 'поиск сообщений')
    personal_inf = Element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]', 'Найденный контакт')
    messege = Element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]', 'Пишем сообщение')
    send_messege = Element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]', 'отправляем сообщение')
class Test(TestCaseUI):
    def test(self):
        self.browser.open(sbis_site)
        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlExact(sbis_site), TitleExact(sbis_title))

        log('Авторизация на сайте')
        user_login, user_password = 'пчелкин', 'пчелкин123'
        auth = AuthOnline(self.driver)
        auth.login_inp.type_in(user_login + Keys.ENTER).should_be(ExactText(user_login))
        auth.password_inp.type_in(user_password + Keys.ENTER).should_be(Not(Visible))

        self.browser.open(contacts_url)
        log('Проверить переход в контакты и заголовок страницы')
        self.browser.should_be(UrlExact(contacts_url), TitleExact(contacts_title))

        log('Отправляем сообщение самому себе')
        name = 'Пчелкин Алексей Павлович'
        main = MainOnline(self.driver)
        main.plus.click()
        main.find.should_be(CountElements(2))
        main.find.type_in(name)
        main.personal_inf.should_be(Attribute(title=name))
        main.personal_inf.click()
        main.messege.type_in('проверка')
        main.send_messege.click()

        log('Проверяем что сообщение есть в реестре')



