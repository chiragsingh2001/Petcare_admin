from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("input[name='email']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("button[type='submit']")
        
        # Adjust selectors to match actual DOM (these are examples)
        self.error_message = page.locator("xpath=//*[@id='login-form']//span/strong")
        self.email_error = page.locator("#email-error")
        self.password_error = page.locator("#password-error")

    def goto(self):
        self.page.goto("https://petcare.ezxdemo.com/admin/login")

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_text(self) -> str:
        """Return visible validation message text if any."""
        if self.error_message.is_visible():
            return self.error_message.inner_text().strip()
        elif self.email_error.is_visible():
            return self.email_error.inner_text().strip()
        elif self.password_error.is_visible():
            return self.password_error.inner_text().strip()
        else:
            return ""

    def expect_any_error(self, expected_messages: list):
        """Check that any one of the provided messages appears."""
        visible_text = self.get_error_text()
        assert visible_text != "", "No validation message is visible."
        assert any(msg in visible_text for msg in expected_messages), \
            f"Unexpected error message: '{visible_text}'"
        print(f"✅ Validation message displayed: {visible_text}")
