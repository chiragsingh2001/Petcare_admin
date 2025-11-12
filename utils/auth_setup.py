import sys
import os

# Get the absolute path of the project root: C:\playwright_automation
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print("PROJECT ROOT:", PROJECT_ROOT)

# # Add project root to Python path
sys.path.insert(0, PROJECT_ROOT)

from pages.login import LoginPage
from playwright.sync_api import sync_playwright


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        page = context.new_page()
        login = LoginPage(page)

        login.goto()
        login.login("petcare.admin@yopmail.com", "PetCare@Admin2025")

        page.wait_for_url("https://petcare.ezxdemo.com/admin/home")

        state_path = os.path.join(PROJECT_ROOT, "state.json")
        context.storage_state(path=state_path)

        print("✅ Session saved at:", state_path)

        browser.close()


if __name__ == "__main__":
    run()
