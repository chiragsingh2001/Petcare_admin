import pytest
from pages.user_management import UserManagement
from playwright.sync_api import Page, expect



@pytest.mark.parametrize("name, email, phone, password, image, testcase, testcaseid",[("hemanth", "hemanth@mailinator.com", "7225163231", "Admin@123", "C:\\Users\\ADMIN\\OneDrive\\Pictures\\Screenshots\\App_point_3.png", "with valid and new email", 1),
("hemanth", "hemanth@mailinator.com", "7225133231", "Admin@123", "C:\\Users\\ADMIN\\OneDrive\\Pictures\\Screenshots\\App_point_3.png", "with valid but registered email and unregistered number", 2),
("hemanth", "laalchand@mailinator.com", "7225163231", "Admin@123", "C:\\Users\\ADMIN\\OneDrive\\Pictures\\Screenshots\\App_point_3.png", "with valid but already registered number and unregistered email", 3)])
def test_add_user(page: Page, name, email, phone, password, image, testcase, testcaseid):
    user = UserManagement(page)
    user.goto()
    user.add_user()
    user.add_details(name, email, phone, password, image,testcase, testcaseid)
    print(f"Executed testcase:{testcase}")

