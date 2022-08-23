import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Обработчик опции командной строки: в командную строку передается параметр "language", например, '--language="ru"'.
# По умолчанию сайт загружается на английском языке.
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en, ...")

@pytest.fixture(scope="function")
def browser(request):
    # В переменную user_language передается параметр "language" из командной строки с пом.обработчика выше
    user_language = request.config.getoption("language")
    
    # Активизируется класс Options
    options = Options()
    
    # В опции вебдрайвера передаётся параметр из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    
    yield browser
    browser.quit()
