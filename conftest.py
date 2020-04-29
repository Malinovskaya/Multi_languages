from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en, es or fr")

@pytest.fixture
def browser(request):
    language_name = request.config.getoption("language")
    browser = None
    options = Options()
    if language_name == "en":
        print("\nstart chrome browser for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
        browser = webdriver.Chrome(options=options)
    elif language_name == "es":
        print("\nstart chrome browser for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': "es"})
        browser = webdriver.Chrome(options=options)
    elif language_name == "fr":
        print("\nstart chrome browser for test..")
        options.add_experimental_option('prefs', {'intl.accept_languages': "fr"})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be en, es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()