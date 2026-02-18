import os

import allure
import pytest
from datetime import datetime
from playwright.sync_api import sync_playwright
from utils.config_loader import load_config


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default=None, help="Environment: qa/staging/prod")
    parser.addoption("--browser", action="store", default=None, help="Override browser")
    parser.addoption("--headless", action="store_true", help="Run in headless mode")


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    return load_config(env)


@pytest.fixture(scope="session")
def playwright_instance():
    pw = sync_playwright().start()
    yield pw
    pw.stop()


@pytest.fixture(scope="session")
def browser(request, playwright_instance, config):
    browser_name = request.config.getoption("--browser") or config["browser"]
    headless = request.config.getoption("--headless") or config["headless"]
    browser = getattr(playwright_instance, browser_name).launch(headless=headless)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def browser_context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(browser_context, config, request):
    test_name = request.node.name.replace(" ", "_")
    page = browser_context.new_page()
    page.set_default_timeout(config["timeout"])
    yield page
    page.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Let pytest run the test first
    outcome = yield
    result = outcome.get_result()

    # Run only if test failed AND has 'page' fixture
    if result.failed and "page" in item.fixturenames:
        page = item.funcargs.get("page", None)
        if page:
            os.makedirs("reports/allure-results", exist_ok=True)
            screenshot_path = f"reports/allure-results/{item.name}.png"
            page.screenshot(path=screenshot_path)
            # Attach screenshot to Allure report if available
            try:
                allure.attach.file(
                    screenshot_path,
                    name=f"Failure - {item.name}",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception:
                pass  # Safe ignore if Allure not active