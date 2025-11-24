import pytest
from pages.user_management import UserManagement
from playwright.sync_api import Page, expect


@pytest.mark.parametrize("name, email, phone, password, image",[("hemanth", "hemanth@mailinator.com", "7225163231", "Admin@123", "C:\\Users\\ADMIN\\OneDrive\\Pictures\\Screenshots\\App_point_3.png")])
def test_add_user(page: Page, name, email, phone, password, image):
    user = UserManagement(page)
    user.goto()
    user.add_user()
    user.add_details(name, email, phone, password, image)

