from selenium import webdriver
from pageObjects.UserProfilePage import UserProfile_Class
from utilities.readproperties import Readconfig
from utilities.logger import Logging_class

class Test_UserProfile:
    Registration_url = Readconfig.get_registration_url()
    Login_url = Readconfig.get_login_url()
    Name = Readconfig.get_name()
    Username = Readconfig.get_username()
    Password = Readconfig.get_password()
    log = Logging_class.log_generator()


    # def test_registration_001(self, setup):
    #     self.driver = setup
    #     self.log.info("*** opening browser***")
    #
    #     # self.driver = webdriver.Chrome()
    #     # self.driver.maximize_window()
    #     self.ur = UserProfile_Class(self.driver)
    #     self.log.info("*** test_registration_001 is started***")
    #
    #     self.driver.get(self. Registration_url)
    #     self.log.info("Go to url--> " + self. Registration_url)
    #     self.ur.Enter_Name(self.Name)
    #     self.ur.Enter_Email(self.Username)
    #     self.log.info("enter email ")
    #     self.ur.Enter_Password(self.Password)
    #     self.log.info("password ")
    #     self.ur.Enter_ConfirmPassword(self.Password)
    #     self.ur.Click_login_or_Register_button()
    #     self.log.info("click on Registration button ")
    #
    #     if self.ur.Validation_login_or_Registration() == "Registration or login  pass":
    #         self.log.info("test_registration_001 is Pass")
    #         self.driver.save_screenshot(
    #             "C:\\Babli\\python_revision_2\\Pytest_python_projects\\Pytest_credkart_project\\Screenshots\\Registration_pass.png"
    #         )
    #         self.driver.close()
    #         assert True
    #     else:
    #         self.log.error("test_registration_001 is Fail")
    #         self.driver.save_screenshot(
    #             "C:\\Babli\\python_revision_2\\Pytest_python_projects\\Pytest_credkart_project\\Screenshots\\Registration_fail.png"
    #         )
    #         self.driver.close()
    #         assert False


    def test_user_login_004(self, setup, getDataForLogin):
        self.driver = setup
        self.log.info("*** opening browser ***")
        self.ur = UserProfile_Class(self.driver)
        self.log.info("test_user_login_004 is started")
        self.driver.get(self.Login_url)
        self.log.info("go to url")
        self.ur.Enter_Email(getDataForLogin[0])
        self.log.info("enter email")
        self.ur.Enter_Password(getDataForLogin[1])
        self.log.info("enter password")
        self.ur.Click_login_or_Register_button()
        self.log.info("click on login button")

        if self.ur.Validation_login_or_Registration() == "Registration or login  pass":
            self.log.info("test_user_login_004 is pass")
            if getDataForLogin[2] == "Pass":
                self.driver.save_screenshot(
                "C:\\Babli\\python_revision_2\\Pytest_python_projects\\Pytest_credkart_project\\Screenshots\\Login_pass.png"
            )
            assert True
        elif getDataForLogin[2] == "Fail":
            self.driver.save_screenshot(
                "C:\\Babli\\python_revision_2\\Pytest_python_projects\\Pytest_credkart_project\\Screenshots\\Login_pass.png"
            )
            assert False

        else:
            if getDataForLogin[2] == "Pass":
                self.driver.save_screenshot(
                    "C:\\Babli\\python_revision_2\\Pytest_python_projects\\Pytest_credkart_project\\Screenshots\\Login_pass.png"
                )
                assert False
            elif getDataForLogin[2] == "Fail":
                self.driver.save_screenshot(
                    "C:\\Babli\\python_revision_2\\Pytest_python_projects\\Pytest_credkart_project\\Screenshots\\Login_pass.png"
                )
                assert True
            self.log.error("test_user_login_004 is fail")
            self.driver.save_screenshot(
                "C:\\Babli\\python_revision_2\\Pytest_python_projects\\Pytest_credkart_project\\Screenshots\\Login_fail.png"
            )
            self.driver.close()
            assert False

