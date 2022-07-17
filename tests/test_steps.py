import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps(browser_management):
    with allure.step('Open main page'):
        browser.open('/')

    with allure.step('Search the repository'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()

    with allure.step('Go to repository link'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Open tab Issues'):
        s('#issues-tab').click()

    with allure.step('Verify that issue number 76 exists'):
        s(by.partial_text('#76')).should(be.visible)


def test_decorator_steps(browser_management):
    open_main_page()
    search_the_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_tab_issues()
    should_see_issue_with_number(76)


@allure.step('Open main page')
def open_main_page():
    browser.open('/')


@allure.step('Search the repository {repo}')
def search_the_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()


@allure.step('Go to repository link {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Open tab Issues')
def open_tab_issues():
    s('#issues-tab').click()


@allure.step('Verify that issue number 76 exists')
def should_see_issue_with_number(number):
    s(by.partial_text(f'#{number}')).should(be.visible)
