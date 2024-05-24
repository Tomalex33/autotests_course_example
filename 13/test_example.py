from atf.ui import *
from atf import *
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from controls import ControlsTreeGridView

sbis_site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
sbis_title = 'Вход в личный кабинет'
task_url = 'https://fix-online.sbis.ru/page/tasks-in-work'
task_title = 'Задачи на мне'


class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-InputBase__nativeField_caretFilled.controls-InputBase__nativeField_caretFilled_theme_default', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default', 'пароль')


class OpenContexMenu(Region):
    tasks = Element(By.CSS_SELECTOR, '[title="Пчелкин-Сити"]', 'Задачи')
    setting = CustomList(By.CSS_SELECTOR, '.controls-Menu__row', 'Опции')
    setting_css = '.icon-SettingsNew'


class Test01(TestCaseUI):
    def test_01(self):
        self.browser.open(sbis_site)
        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlExact(sbis_site), TitleExact(sbis_title))

        log('Авторизация на сайте')
        user_login, user_password = 'пчелкин', 'пчелкин123'
        auth = AuthOnline(self.driver)
        auth.login_inp.click()
        auth.login_inp.type_in(user_login + Keys.ENTER).should_be(ExactText(user_login))
        auth.password_inp.type_in(user_password + Keys.ENTER).should_be(Not(Visible))

        log('Переходим во вкладку Задачи/работа')
        self.browser.open(task_url)

        task = OpenContexMenu(self.driver)
        task.tasks.mouse_over()
        task.tasks.element('.icon-SettingsNew')
        # task.tasks.open_context_menu()

        # new_task = ControlsTreeGridView()
        # new_task.row(1).select_menu_actions('.controls-Menu__row')
        #
        #
        # task.tasks.element('.icon-SettingsNew').click()

        # task_item = self.tasks.item(contains_text=task)
        # task_item.mouse_over()
        # task_item.element(self.setting_css).click()
        # self.setting.item(contains_text=setting).click()

# ".controls-BaseControl_showActions.controls-BaseControl_showActions_onhover"
# " "