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
        self.user_role = self.page.locator("//*[@id='userForm']/div[1]/div/div[5]/select")
        self.user_profile = self.page.locator("#profile_pic")
        self.user_add = self.page.locator("xpath=//*[@id='userForm']/div[2]/button[1]")

    # generate random email
    def generate_email(self):
        timestamp = int(time.time() * 1000)
        rand = ''.join(random.choices(string.ascii_lowercase, k=5))
        return f"test_{timestamp}_{rand}@mailinator.com"

    # generate random number
    def generate_phone(self):
        timestamp = int(time.time() * 1000)
        return "9" + str(timestamp)[-9:]

    def goto(self):
        self.page.goto("https://petcare.ezxdemo.com/admin/user/all")
        self.page.wait_for_load_state("load") 
    
    # clicking on the add button    
    def add_user(self):
        try:
            expect(self.add_button).to_be_visible()
            self.add_button.click()
        except Exception as e:
            # Code that runs if an exception occurs
            print(f"An error occurred:{e}")
    
    def add_details(self, name, email, phone, password, image, testcase):

        if testcase == "with valid and new email":
            email = self.generate_email()
            phone = self.generate_phone()
            print(f"{email}, {phone}")

        elif testcase == "with valid but registered email and unregistered number":
            phone = self.generate_phone()

        elif testcase == "with valid but already registered number and unregistered email":
            email = self.generate_email()

        self.user_name.fill(name)
        self.user_email.fill(email)
        self.user_phone.fill(phone)
        self.user_pass.fill(password)
        self.user_role.select_option(value="Pet Parent")
        self.user_profile.set_input_files(image)
        self.user_add.click()
   










