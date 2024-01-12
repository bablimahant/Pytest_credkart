

#### no need to create login page object bcoz already created in registration page object

# from selenium.webdriver.common.by import By
#
# class User_login_class:
#     Text_Email_ID = (By.ID, "email")
#     Text_Password_ID = (By.ID, "password")
#     Button_login_XPATH = (By.XPATH, "//button[@type='submit']")
#     Validation_login_XPATH = (By.XPATH, "//h2[normalize-space()='CredKart']")
#
#     def __ini__(self, driver):
#         self.driver = driver
#
#     def enter_email(self, email):
#         self.driver.find_element(*User_login_class.Text_Email_ID).send_keys(email)
#
#     def enter_password(self, password):
#         self.driver.find_element(*User_login_class.Text_Password_ID).send_keys(password)
#
#     def click_login(self):
#         self.driver.find_element(*User_login_class.Button_login_XPATH).click()
#
#     def validation_login(self):
#         try:
#             self.driver.find_element(*User_login_class.Validation_login_XPATH)
#             print("login pass")
#             return "login pass"
#         except:
#             print("login fail")
#             return "login fail"
#
#
