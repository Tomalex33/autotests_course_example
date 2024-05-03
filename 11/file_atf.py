
from atf.ui import *
from atf import log
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

sbis_site = 'https://test.sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'

class MainSbisRu(Region):
    tabs = CustomList(By.CSS_SELECTOR, '.sbisru-Header__menu-item', 'Вкладки')
    start_work = Button(By.CSS_SELECTOR, '.sbisru-Button--xs', 'Кнопка')
class Test(TestCaseUI):

    def test(self):
        self.browser.open(sbis_site)
        log('Проверить адрес сайта и заголовок страницы')
        self.browser.should_be(UrlExact(sbis_site), TitleExact(sbis_title))

        log('Проверить отображение четырех вкладок')
        sbis_ru = MainSbisRu(self.driver)
        sbis_ru.tabs.should_be(CountElements(4))

        log('Проверить текст, атрибут и видимость кнопки Начать работу')
        buttons_txt = 'Начать работу'
        sbis_ru.start_work.should_be(ExactText(buttons_txt), Attribute(title=buttons_txt)).click()

        log('Перейти на страницу авторизации')
        self.browser.switch_to_new_window(sbis_ru.start_work.click)
        sbis_ru.start_work.click()

        driver.switch_to.window(driver.window_handles[1])
        sleep(3)
        login = driver.find_element(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-InputBase__nativeField_caretFilled.controls-InputBase__nativeField_caretFilled_theme_default')
        login.send_keys('тест', Keys.ENTER)
        sleep(2)
        # assert login.get_attribute('value') == 'my_login'
        password = driver.find_element(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default')
        password.send_keys('тест123', Keys.ENTER)
        sleep(4)
        news = driver.find_elements(By.CSS_SELECTOR, '[data-qa="list"]')
        action_chains = ActionChains(driver)
        action_chains.move_to_element(news[1])
        action_chains.context_click(news[1])
        action_chains.perform()
        sleep(3)
        context_menu = driver.find_element(By.CSS_SELECTOR, '[templatename="Controls/menu:Popup"]')
        context_menu.is_displayed()
        sleep(4)
