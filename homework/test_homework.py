from datetime import time

from homework.homework import set_dark_theme_by_time, set_dark_theme_by_time_and_user_choice, find_suitable_user, \
    find_suitable_users, open_browser, go_to_companyname_homepage, find_registration_button_on_login_page


def test_set_dark_theme_by_time():
    assert set_dark_theme_by_time(time(hour=6)) is False
    assert set_dark_theme_by_time(time(hour=7)) is False
    assert set_dark_theme_by_time(time(hour=22)) is True
    assert set_dark_theme_by_time(time(hour=0)) is True


def test_set_set_dark_theme_by_time_and_user_choice():
    assert set_dark_theme_by_time_and_user_choice(current_time=time(hour=22), user_choice=None) is True
    assert set_dark_theme_by_time_and_user_choice(current_time=time(hour=6), user_choice=None) is False
    assert set_dark_theme_by_time_and_user_choice(current_time=time(hour=0), user_choice=None) is True
    assert set_dark_theme_by_time_and_user_choice(current_time=time(hour=7), user_choice=None) is False

    assert set_dark_theme_by_time_and_user_choice(current_time=time(hour=22), user_choice=True) is True
    assert set_dark_theme_by_time_and_user_choice(current_time=time(hour=6), user_choice=True) is True
    assert set_dark_theme_by_time_and_user_choice(current_time=time(hour=0), user_choice=True) is True
    assert set_dark_theme_by_time_and_user_choice(current_time=time(hour=7), user_choice=True) is True

    assert set_dark_theme_by_time_and_user_choice(current_time=time(hour=22), user_choice=False) is False
    assert set_dark_theme_by_time_and_user_choice(current_time=time(hour=6), user_choice=False) is False
    assert set_dark_theme_by_time_and_user_choice(current_time=time(hour=0), user_choice=False) is False
    assert set_dark_theme_by_time_and_user_choice(current_time=time(hour=7), user_choice=False) is False


def test_find_suitable_user():
    assert find_suitable_user() == {"name": "Olga", "age": 45}


def test_find_suitable_users():
    assert find_suitable_users() == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")
