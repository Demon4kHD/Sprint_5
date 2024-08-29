
class AllPagesElements:
    TOPLINE_CONSTRUCTOR = './/li[1]/*[@href="/"]'  # Переход на экран Конструктора
    TOPLINE_FEED = './/li[2]/*[@href="/feed"]'  # Переход на экран Лента заказов
    TOPLINE_LOGO = './/div/*[@href="/"]'  # Переход на экран Конструктора
    TOPLINE_ACCOUNT = './/*[@href="/account"]'  # Переход на экран Личный кабинет


class MainPageElements:
    MAIN_BURGER_BUN_GROUP = '//*[text()="Булки"]'
    MAIN_SAUCE_GROUP = '//*[text()="Соусы"]'
    MAIN_FILLING_GROUP = '//*[text()="Начинки"]'
    MAIN_PARENT_ELEMENT_BURGER_BUN = '//div[span[text()="Булки"]]'
    MAIN_PARENT_ELEMENT_SAUCE = '//div[span[text()="Соусы"]]'
    MAIN_PARENT_ELEMENT_FILLING = '//div[span[text()="Начинки"]]'
    MAIN_BUTTON_GET_AUTH = './/section[2]/div/button'
    MAIN_FIRST_SCROLL_ELEMENT = './/*[@alt="Мясо бессмертных моллюсков Protostomia"]'
    MAIN_SECOND_SCROLL_ELEMENT = './/*[@alt="Сыр с астероидной плесенью"]'
    MAIN_THIRD_SCROLL_ELEMENT = './/*[@alt="Флюоресцентная булка R2 - D3"]'


class RegistrationPageElements:
    REG_INPUT_NAME = './/fieldset[1]//input'  # Поле ввода имени
    REG_INPUT_EMAIL = './/fieldset[2]//input'  # Поле ввода email
    REG_INPUT_PASSWORD = './/fieldset[3]//input'  # Поле ввода пароля
    REG_BUTTON_GET_REG = \
        './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]'
        # Кнопка подтверждения регистрации
    REG_LINK_GET_AUTH = './/*[@href="/login"]'  # Текст-ссылка перехода на страницу Авторизации


class AuthorizationPageElements:
    AUTH_INPUT_EMAIL = './/input[@name="name"]'  # Поле ввода email
    AUTH_INPUT_PASSWORD = '*//fieldset[2]//input'  # Поле ввода пароля
    AUTH_BUTTON_GET_AUTH = './/form/button'  # Кнопка входа в аккаунт
    AUTH_LINK_GET_REG = './/*[@href="/register"]'  # Текст-ссылка перехода на страницу Регистрации
    AUTH_LINK_GET_FORGOT = './/*[@href="/forgot-password"]'  # Текст-ссылка перехода на страницу Восстановления пароля


class PersonalAccountElements:
    TOPLINE_ACCOUNT_ACTIVE = './/*[@class="AppHeader_header__link__3D_hX AppHeader_header__link_active__1IkJo"]'
    ACC_EXIT_BUTTON = './/li[3]/button'


class ForgotPasswordElements:
    FGP_LINK_GET_AUTH = './/*[@href="/login"]'


