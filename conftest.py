import pytest
import os
from playwright.sync_api import sync_playwright

STATE_FILE = "state.json"


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="session")
def login_session(browser):
    """Ensure state.json exists before using it in tests."""

    if not os.path.exists(STATE_FILE):
        raise RuntimeError("❌ No saved login session found. Run auth_setup.py first.")

    return STATE_FILE


@pytest.fixture(scope="function")
def page(request, browser, login_session):
    """Fresh context for login tests, stored session for all others."""

    if request.node.get_closest_marker("login"):
        print("\n➡️ Using FRESH context for LOGIN test")
        context = browser.new_context()
    else:
        print("\n➡️ Using STORED SESSION for authenticated test")
        context = browser.new_context(storage_state=login_session)

    page = context.new_page()
    yield page
    context.close()
