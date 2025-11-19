from playwright.sync_api import Page, expect, TimeoutError
import time

class UserManagement:
    def __init__(self, page: Page):
        self.page = page
        self.add_button = self.page.locator("xpath=/html/body/div[3]/div[1]/div[1]/div/div/div/div/div[2]/a")
        self.user_name = self.page.locator("xpath=//*[@id='userForm']/div[1]/div/div[1]/input")
        self.user_email = self.page.locator("xpath=//*[@id='userForm']/div[1]/div/div[2]/input")
        self.user_phone = self.page.locator("//*[@id='userForm']/div[1]/div/div[3]/div/div/input")
        self.user_pass = self.page.locator("//*[@id='password']")
        self.user_role = self.page.locator("//select[@id='userForm']/div[1]/div/div[5]/select")
        self.user_profile = self.page.get_by_label("profile_pic")
    def goto(self):
        self.page.goto("https://petcare.ezxdemo.com/admin/user/all")
        
    def add_user(self):
        try:
            if self.add_button.is_visible:
                self.add_button.click()
            else:
                self.add_button.wait_for(state="visible")
                self.add_button.click()
        except Exception as e:
            # Code that runs if an exception occurs
            print(f"An error occurred:{e}")
    
    def add_details(self, name, email, phone, password):
        self.user_name.fill(name)
        self.user_email.fill(email)
        self.user_phone.fill(phone)
        self.user_pass.fill(password)
        self.user_role.select_option(value="Pet Parent")
        self.user_profile.click()








