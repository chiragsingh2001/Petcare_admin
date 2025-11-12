from playwright.sync_api import Page, expect

class UserManagement:
    def __init__(self, page: Page):
        self.page = page
    
    def goto(self):
        self.page.goto("https://petcare.ezxdemo.com/admin/user/all")




