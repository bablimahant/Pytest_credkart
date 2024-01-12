import pytest
from pageObjects.UserProfilePage import UserProfile_Class
from utilities.readproperties import Readconfig
from utilities import ExcelFileOperation
from utilities.logger import Logging_class


class Test_UserProfile_DDT_class:
    Login_url = Readconfig.get_login_url()

    path = "C:\\Babli\\python_revision_2\\Pytest_python_projects\\Pytest_credkart_project\\TestData\\loginData.xlsx"

    @pytest.mark.sanity
    def test_login_ddt_005(self, setup):
        self.driver = setup

        self.ur = UserProfile_Class(self.driver)
        self.rows = ExcelFileOperation.rows_count(self.path, 'Sheet1')

        Result_list = []
        for r in range(2, self.rows + 1):
            self.email = ExcelFileOperation.ReadData(self.path, 'Sheet1', r, 1)
            self.password = ExcelFileOperation.ReadData(self.path, 'Sheet1', r, 2)
            self.Expected_Result = ExcelFileOperation.ReadData(self.path,'Sheet1', r, 3)

            self.driver.get(self.Login_url)
            self.ur.Enter_Email(self.email)
            self.ur.Enter_Password(self.password)
            self.ur.Click_login_or_Register_button()
            if self.ur.Validation_login_or_Registration() == "Registration or login  pass":
                if self.Expected_Result == "Pass":
                    Result_list.append("Pass")
                    ExcelFileOperation.WriteData(self.path, 'Sheet1', r, 4, "Pass")
                    self.driver.save_screenshot(
                        "C:\\Babli\\python_revision_2\\Pytest_python_projects\\Pytest_credkart_project\\Screenshots\\loginpass_DDT.png"
                    )
                    self.ur.Click_Drpdown()
                    self.ur.Click_Logout()
                elif self.Expected_Result == "Fail":
                    Result_list.append("Fail")
                    ExcelFileOperation.WriteData(self.path, 'Sheet1', r, 4, "Fail")
                    self.driver.save_screenshot(
                        "C:\\Babli\\python_revision_2\\Pytest_python_projects\\Pytest_credkart_project\\Screenshots\\loginfail_DDT.png"
                    )
                    self.ur.Click_Drpdown()
                    self.ur.Click_Logout()

            elif self.ur.Validation_login_or_Registration() == "Registration or login  fail":
                if self.Expected_Result == "Pass":
                    Result_list.append("Fail")
                    ExcelFileOperation.WriteData(self.path, 'Sheet1', r, 4, "Fail")
                    self.driver.save_screenshot(
                        "C:\\Babli\\python_revision_2\\Pytest_python_projects\\Pytest_credkart_project\\Screenshots\\loginfail_DDT.png"
                    )

                elif self.Expected_Result == "Fail":
                    Result_list.append("Pass")
                    ExcelFileOperation.WriteData(self.path, 'Sheet1', r, 4, "Pass")
                    self.driver.save_screenshot(
                        "C:\\Babli\\python_revision_2\\Pytest_python_projects\\Pytest_credkart_project\\Screenshots\\loginfail_DDT.png"
                    )


        print(Result_list)

        if "Fail" not in Result_list:
            assert True
        else:
            assert False









