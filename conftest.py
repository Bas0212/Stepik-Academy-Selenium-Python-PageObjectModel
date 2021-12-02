import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox or opera')
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    print('\nInit language on ...', language)

    browser_name = request.config.getoption('browser_name')
    browser = None
    if (browser_name == 'chrome'):
        print('\nStart Chrome browser for test ...')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        # options.add_argument(f'–lang= {language}')
        browser = webdriver.Chrome(options=options)
    elif (browser_name == 'firefox'):
        print('\nStart Firefox browser for test ...')
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', language)
        browser = webdriver.Firefox(firefox_profile=fp)
    elif (browser_name == 'opera'):
        print('\nStart Opera browser for test ...')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Opera(options=options)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox or opera')

    yield browser
    print('\nQuit browser ...')
    browser.quit()
