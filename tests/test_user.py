import pytest
from pages.user_management import UserManagement
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("name, email, phone, password ",[("hemanth", "hemanth@mailinator.com", "7225163231", "Admin@123")])
def test_add_user(page: Page, name, email, phone, password):
    user = UserManagement(page)
    user.goto()
    user.add_user()
    user.add_details(name, email, phone, password)

