

def set_dark_theme_by_time(current_time):
    """
    Напишите функцию, которая включает тёмную тему на сайте в зависимости от времени
    С 22 до 6 часов утра - ночь, тёмная тема включена
    """
    is_dark_theme = None
    return is_dark_theme


def set_dark_theme_by_time_and_user_choice(current_time, user_choice):
    """
    Напишите функцию, которая включает тёмную тему на сайте в зависимости от времени и выбора пользователя
    С 22 до 6 часов утра - ночь, тёмная тема включена

    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    is_dark_theme = None

    return is_dark_theme


users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]


def find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    suitable_user = None
    # TODO найдите пользователя с именем "Olga"
    return suitable_user


def find_suitable_users():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    suitable_users = []
    # TODO найдите всех пользователей младше 20 лет
    return suitable_users


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже и присвойте значение переменной actual_result
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"

def readable_function(func, *args, **kwargs):
    result = None
    return result


def open_browser(browser_name):
    actual_result = None
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = None
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = None
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
