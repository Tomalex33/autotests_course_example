
from atf.ui import *
from atf import log
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

sbis_site = 'https://fix.sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'

class MainSbisRu(Region):
    tabs = CustomList(By.CSS_SELECTOR, '.sbisru-Header__menu-item', 'Вкладки')
    start_work = Button(By.CSS_SELECTOR, '.sbisru-Button--xs', 'Кнопка')

class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-InputBase__nativeField_caretFilled.controls-InputBase__nativeField_caretFilled_theme_default', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default', 'пароль')

class MainOnline(Region):
    new_title = CustomList(By.CSS_SELECTOR, '.feed-Title', 'Заголовки новостей')
    popup_menu = Element(By.CSS_SELECTOR, '[templatename="Controls/menu:Popup"]', 'Меню')

class Test(TestCaseUI):

    def test(self):
        self.browser.open(sbis_site)
        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlExact(sbis_site), TitleExact(sbis_title))

        log('Проверить отображение четырех вкладок')
        sbis_ru = MainSbisRu(self.driver)
        sbis_ru.tabs.should_be(CountElements(4))

        log('Проверить текст, атрибут и видимость кнопки Начать работу')
        button_txt = 'Начать работу'
        sbis_ru.start_work.should_be(ExactText(button_txt), Attribute(title=button_txt))

        log('Перейти на страницу авторизации')
        self.browser.switch_to_new_window(sbis_ru.start_work.click)

        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlContains('fix-online.sbis.ru'), TitleExact('Вход в личный кабинет'))

        log('Авторизация')
        user_login, user_password = 'пчелкин', 'пчелкин123'
        auth = AuthOnline(self.driver)
        auth.login_inp.type_in(user_login+Keys.ENTER).should_be(ExactText(user_login))
        auth.password_inp.type_in(user_password+Keys.ENTER).should_be(Not(Visible))

        log('Навести курсор на новость и сделать контекстный клик')
        main_online = MainOnline(self.driver)
        main_online.new_title.item(3).scroll_into_view().context_click()


        log('Проверить отображение контекстного меню')
        main_online.popup_menu.should_be(Visible)



