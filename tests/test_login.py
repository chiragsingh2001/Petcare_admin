import pytest
from pages.login import LoginPage
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("email,password,expect_success,TestCase", [
    ("petcare.admin@yopmail.com", "PetCare@Admin2025", True, "With valid Email and password"),
    ("petcare.admin@yopmail.com", "wrongPassword", False, "With valid Email and invalid password"),
    ("unregistered@example.com", "PetCare@Admin2025", False, "With invalid Email and valid password"),
    ("", "", False, "Without Email and password"),
    ("", "PetCare@Admin2025", False, "Without Email and with password"),
    ("petcare.admin@yopmail.com", "", False, "With Email and Without Password"),
    ("petcare.admin@yopmail.com", "qmiabus", False, "With Email and Short Length Password")
])
@pytest.mark.login
def test_login(page: Page, email, password, expect_success, TestCase):
    login = LoginPage(page)
    login.goto()
    login.login(email, password)

    if expect_success:
        expect(page).to_have_url("https://petcare.ezxdemo.com/admin/home", timeout=5000)
        print(f"✅ {TestCase} passed (successful login)")
    else:
        expected_errors = [
            "Please enter a valid email address",
            "The password field must be at least 8 characters.",
            "Please provide a password",
            "This field is required.",
            "Invalid email or password."
        ]
        login.expect_any_error(expected_errors)
        print(f"✅ {TestCase} passed (error validation working)")