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
    task_list = ControlsTreeGridView(By.CSS_SELECTOR, '.brTasksOnMe .controls-Grid', 'Выбор задачи из списка задач')
    popup = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-MoveDialog__explorer', 'Перенос в папку из popup меню')
    folders = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-FilterViewPanel_viewMode-default-vertical.controls-FilterViewPanel-transparent .controls-Grid', 'Выбор папки')
    number = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-Grid .controls-DecoratorNumber', 'Счетчик задач')

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

        log('Переход через аккордеон в раздел "Задачи"')
        acc = Side(self.driver)
        acc.side_menu.item(contains_text='Задачи').click()
        delay(1)
        acc.side_menu.item(contains_text='Задачи').click()

        log('Перемещаем задачу в папку Исходящие')
        list_task = TaskList(self.driver)
        list_task.task_list.item(contains_text='ewq').select_menu_actions('Переместить')
        list_task.popup.item(contains_text='Исходящие').click()
        delay(1)

        log('Переходим в папку исходящие и проверяем что задача перенеслась')
        list_task.folders.item(contains_text='Исходящие').click()
        list_task.task_list.should_be(ContainsText('ewq'))
        list_task.task_list.check_rows_number(2)


        log('Перемещаем обратно в папку входящие')
        list_task.task_list.item(contains_text='ewq').select_menu_actions('Переместить')
        list_task.popup.item(contains_text='Входящие').click()
