from atf.ui import *
from atf import *
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from controls import *

"""Написать тесты по реестру Контакты (можно использовать свой реестр, если в нём существуют подобные проверки)."""
"""Переместить запись в другую папку и проверить перемещение (убедиться в: наличии в папке и увеличении счётчика). И вернуть обратно."""

sbis_site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
sbis_title = 'Вход в личный кабинет'
task_url = 'https://fix-online.sbis.ru/page/tasks-in-work'
task_title = 'Задачи на мне'


class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-InputBase__nativeField_caretFilled.controls-InputBase__nativeField_caretFilled_theme_default', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default', 'пароль')


class Task(Region):
    task_page = NavigationPanelsSidebar()


class Side(Region):
    side_menu = NavigationPanelsAccordionView()


class TaskList(Region):
    task_list = ControlsTreeGridView(By.CSS_SELECTOR, '.brTasksOnMe .controls-Grid', 'Выбор задания')
    Popup = ControlsPopup()

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

        # task = Task(self.driver)
        # task.task_page.collapse()
        # task.task_page.expand()

        log('Переход через аккордеон в раздел "Задачи"')
        acc = Side(self.driver)
        acc.side_menu.item(contains_text='Задачи').double_click()

        log('Перемещаем задачу из папки в папку')

        list_task = TaskList(self.driver)

        # list_task.task_list.find_cell_by_column_number('ewq', 1).click()
        list_task.task_list.item(contains_text='ewq').select_menu_actions('Переместить', exact=True)

        # list_task.task_list.check_columns_number(1)
        list_task.Popup._get_item('Переместить')
        list_task.Popup.close()





