from selenium import webdriver
from selenium.webdriver.common.by import By

class UserProfile_Class:
    Text_Name_ID = (By.ID, "name")
    Text_Email_ID = (By.ID, "email")
    Text_Password_ID = (By.ID, "password")
    Text_ConfirmPassword_ID =(By.ID, "password-confirm")
    Click_login_or_Register_XPATH = (By.XPATH, "//button[normalize-space()='Login']")
    Validation_Login_or_Registration_XPATH = (By.XPATH, "//h2[normalize-space()='CredKart']")
    Click_Drpdown_XPATH = (By.XPATH, "//a[@role='button']")
    Click_Logout_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")


    def __init__(self, driver):
        self.driver = driver

    def Enter_Name(self, name):
        self.driver.find_element(*UserProfile_Class.Text_Name_ID).send_keys(name)

    def Enter_Email(self, email):
        self.driver.find_element(*UserProfile_Class.Text_Email_ID).send_keys(email)

    def Enter_Password(self, password):
        self.driver.find_element(*UserProfile_Class.Text_Password_ID).send_keys(password)

    def Enter_ConfirmPassword(self, confirmpassword):
        self.driver.find_element(*UserProfile_Class.Text_ConfirmPassword_ID).send_keys(confirmpassword)

    def Click_login_or_Register_button(self):
        self.driver.find_element(*UserProfile_Class.Click_login_or_Register_XPATH).click()



    def Validation_login_or_Registration(self):
        try:
            self.driver.find_element(*UserProfile_Class.Validation_Login_or_Registration_XPATH)
            print("Registration or login  pass")
            return "Registration or login  pass"
        except:
            print("Registration or login  fail")
            return "Registration or login  fail"

    def Click_Drpdown(self):
        self.driver.find_element(*UserProfile_Class.Click_Drpdown_XPATH).click()

    def Click_Logout(self):
        self.driver.find_element(*UserProfile_Class.Click_Logout_XPATH).click()

