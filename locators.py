
from selenium.webdriver.common.by import By
class AllPagesElements:
    TOPLINE_CONSTRUCTOR = (By.XPATH, './/li[1]/*[@href="/"]')  # Переход на экран Конструктора
    TOPLINE_FEED = (By.XPATH, './/li[2]/*[@href="/feed"]')  # Переход на экран Лента заказов
    TOPLINE_LOGO = (By.XPATH, './/div/*[@href="/"]')  # Переход на экран Конструктора
    TOPLINE_ACCOUNT = (By.XPATH, './/*[@href="/account"]')  # Переход на экран Личный кабинет


class MainPageElements:
    MAIN_BURGER_BUN_GROUP = (By.XPATH, '//*[text()="Булки"]')
    MAIN_SAUCE_GROUP = (By.XPATH, '//*[text()="Соусы"]')
    MAIN_FILLING_GROUP = (By.XPATH, '//*[text()="Начинки"]')
    MAIN_PARENT_ELEMENT_BURGER_BUN = (By.XPATH, '//span[text()="Булки"]/parent::*')
    MAIN_PARENT_ELEMENT_SAUCE = (By.XPATH, '//span[text()="Соусы"]/parent::*')
    MAIN_PARENT_ELEMENT_FILLING = (By.XPATH, '//span[text()="Начинки"]/parent::*')
    MAIN_BUTTON_GET_AUTH = (By.XPATH, './/section[2]/div/button')
    MAIN_FIRST_SCROLL_ELEMENT = (By.XPATH, './/*[@alt="Мясо бессмертных моллюсков Protostomia"]')
    MAIN_SECOND_SCROLL_ELEMENT = (By.XPATH, './/*[@alt="Сыр с астероидной плесенью"]')
    MAIN_THIRD_SCROLL_ELEMENT = (By.XPATH, './/*[@alt="Флюоресцентная булка R2 - D3"]')


class RegistrationPageElements:
    REG_INPUT_NAME = (By.XPATH, './/label[text()="Имя"]/following-sibling::input')  # Поле ввода имени
    REG_INPUT_EMAIL = (By.XPATH, './/label[text()="Email"]/following-sibling::input')  # Поле ввода email
    REG_INPUT_PASSWORD = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input')  # Поле ввода пароля
    REG_BUTTON_GET_REG = (By.XPATH, './/*[contains(@class,"button_button")]')
        # Кнопка подтверждения регистрации
    REG_LINK_GET_AUTH = (By.XPATH, './/*[@href="/login"]')  # Текст-ссылка перехода на страницу Авторизации
    REG_ERROR_MESSAGE = (By.XPATH, '//*[text()="Некорректный пароль"]')


class AuthorizationPageElements:
    AUTH_INPUT_EMAIL = (By.XPATH, './/input[@name="name"]')  # Поле ввода email
    AUTH_INPUT_PASSWORD = (By.XPATH, './/input[@name="Пароль"]')  # Поле ввода пароля
    AUTH_BUTTON_GET_AUTH = (By.XPATH, './/form/button')  # Кнопка входа в аккаунт
    AUTH_LINK_GET_REG = (By.XPATH, './/*[@href="/register"]')  # Текст-ссылка перехода на страницу Регистрации
    AUTH_LINK_GET_FORGOT = (By.XPATH, './/*[@href="/forgot-password"]')  # Текст-ссылка перехода на страницу Восстановления пароля
    AUTH_H2_ENTRANCE = (By.XPATH, ".//*[text()='Вход' ]")


class PersonalAccountElements:
    TOPLINE_ACCOUNT_ACTIVE = (By.XPATH, './/*[contains(@class="link_active"]')
    ACC_EXIT_BUTTON = (By.XPATH, './/li[3]/button')


class ForgotPasswordElements:
    FGP_LINK_GET_AUTH = (By.XPATH, './/*[@href="/login"]')
