# Предварительные действия (Создайте эталонную задачу, заполнив обязательные поля)
# Авторизоваться на сайте https://fix-online.sbis.ru/
# Откройте эталонную задачу по прямой ссылке в новой вкладке браузера
# Убедитесь, что в заголовке вкладки отображается "Задача №НОМЕР от ДАТА",
# где ДАТА и НОМЕР - это ваши эталонные значения
# Проверьте, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными значениями

from atf.ui import *
from atf import *
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

sbis_site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
sbis_title = 'Вход в личный кабинет'
task_url = 'https://fix-online.sbis.ru/page/tasks-in-work'
task_title = 'Задачи на мне'
etalon_task = 'https://fix-online.sbis.ru/opendoc.html?guid=81f9dd04-2517-4f4c-9537-2ad529b61312&client=201379546'


class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-InputBase__nativeField_caretFilled.controls-InputBase__nativeField_caretFilled_theme_default', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default', 'пароль')


class Task(Region):
    task_date = CustomList(By.CSS_SELECTOR, '.controls-EditableArea__Text__inner', 'Дата задания')
    task_number = Element(By.CSS_SELECTOR, '[title="5"]', 'Номер задания')


class Test(TestCaseUI):
    def test(self):
        self.browser.open(sbis_site)
        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlExact(sbis_site), TitleExact(sbis_title))

        log('Авторизация на сайте')
        user_login, user_password = 'пчелкин', 'пчелкин123'
        auth = AuthOnline(self.driver)
        auth.login_inp.click()
        auth.login_inp.type_in(user_login + Keys.ENTER).should_be(ExactText(user_login))
        auth.password_inp.type_in(user_password + Keys.ENTER).should_be(Not(Visible))

        self.browser.create_new_tab(etalon_task)
        self.browser.switch_to_window(1)

        main = Task(self.driver)

        assert_that(lambda: main.task_number.get_attribute('title'), equal_to('5'), 'не верный номер', and_wait())
        assert_that(lambda: main.task_date.item(1).text, equal_to('16 мая, чт'), 'не верная дата', and_wait())


