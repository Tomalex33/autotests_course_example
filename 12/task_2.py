# Авторизоваться на сайте https://fix-online.sbis.ru/ +
# Перейти в реестр Задачи на вкладку "В работе" +
# Убедиться, что выделена папка "Входящие" и стоит маркер.
# Убедиться, что папка не пустая (в реестре есть задачи) +
# Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято
# Создать новую папку и перейти в неё
# Убедиться, что она пустая
# Удалить новую папку, проверить, что её нет в списке папок

from atf.ui import *
from atf import log
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

sbis_site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
sbis_title = 'Вход в личный кабинет'
task_url = 'https://fix-online.sbis.ru/page/tasks-in-work'
task_title = 'Задачи на мне'

class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-InputBase__nativeField_caretFilled.controls-InputBase__nativeField_caretFilled_theme_default', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default', 'пароль')

class MainOnline(Region):
    task_in = Element(By.CSS_SELECTOR, '[data-qa="row"]:has([title="Входящие"])', 'Входящие задачи')
    marker = Element(By.CSS_SELECTOR, '.controls-ListView__itemV_marker.controls-ListView__itemV_marker_size_content-xs', 'маркер')
    task_out = Element(By.CSS_SELECTOR, '[title="Исходящие"]', 'Исходящие задачи')
    task_list = Element(By.CSS_SELECTOR, '[title="Выполнение"]', 'Задача в папке')
    add_task = Element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]', 'Кнопка создания задачи')
    create_folder = Element(By.CSS_SELECTOR, '[data-target="menu_item_folderItem"]', 'Создаем папку')
    name_folder = Element(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-InputBase__nativeField_caretFilled.controls-InputBase__nativeField_caretFilled_theme_default.controls-InputBase__nativeField_hideCustomPlaceholder', 'Ввод текста')
    save_button = Element(By.CSS_SELECTOR, '.controls-BaseButton__wrapper.controls-Button__wrapper_viewMode-outlined.controls-BaseButton__wrapper_captionPosition_end.controls-Button_textAlign-center.controls-Button__wrapper_mode-button', 'Сохраняем новую папку')
    row_expander = Element(By.CSS_SELECTOR, '[data-qa="row-expander"]', 'Раскрывающийся список')
    new_folder = Element(By.CSS_SELECTOR, '[title="тест"]', 'Создаем подпапку')
    delete_new_folder = Element(By.CSS_SELECTOR, '[title="Удалить папку"]', 'Удаляем папку')
    accepte_delete = Element(By.CSS_SELECTOR, '[data-qa="controls-ConfirmationDialog__button-true"]', 'Потверждаем удаление')
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

        log('Переходим во вкладку Задачи/работа')
        self.browser.open(task_url)

        log('Проверить адрес задач и заголовок')
        self.browser.should_be(UrlExact(task_url), TitleExact(task_title))

        main = MainOnline(self.driver)

        log('Проверить, что выделена папка "Входящие" и стоит маркер')
        main.task_in.element('[data-qa="marker"]').should_be(Displayed)

        log('Проверить, что папка не пустая (в реестре есть задачи)')
        main.task_list.should_be(Displayed)

        log('Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято')
        main.task_out.click()
        main.task_in.element('[data-qa="marker"]').should_not_be(Displayed)

        log('Создать новую папку и перейти в неё, Убедиться, что она пустая')
        name_text_folder = 'тест'
        main.add_task.click()
        main.create_folder.click()
        main.name_folder.click()
        main.name_folder.type_in(name_text_folder+Keys.ENTER)
        main.save_button.click()
        main.new_folder.click()
        main.task_list.should_not_be(Displayed)

        log('Удалить новую папку, проверить, что её нет в списке папок')
        main.new_folder.mouse_over()
        main.new_folder.context_click()
        main.delete_new_folder.click()
        main.accepte_delete.click()
        main.task_out.element('[title="тест"]').should_not_be(Displayed)
        main.task_out.should_be(Attribute(title='Исходящие'))

