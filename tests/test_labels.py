import allure
from allure_commons.types import Severity


def test_no_labels():
    pass


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Tasks in the repository")
    allure.dynamic.story("Unauthorized user can't create an issue in the repository")
    allure.dynamic.link("https://github.com", name="Testing")
    pass


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "apolonov")
@allure.feature("Tasks in the repository")
@allure.story("Authorized user can create a task in the repository")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    pass
