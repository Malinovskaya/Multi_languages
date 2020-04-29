from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en, es or fr")

@pytest.fixture
def browser(request):
    language_name = request.config.getoption("language")
    options = Options()
    print("\nstart chrome browser for test..")
    options.add_experimental_option('prefs', {'intl.accept_languages': language_name})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()