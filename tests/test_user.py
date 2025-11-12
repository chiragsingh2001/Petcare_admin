import pytest
from pages.user_management import UserManagement
from playwright.sync_api import Page, expect

def test_visibility(page: Page):
    user = UserManagement(page)
    user.goto()
    

