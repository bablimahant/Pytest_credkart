import configparser


config = configparser.RawConfigParser()
config.read("C:\\Babli\\python_revision_2\\Pytest_python_projects\\Pytest_credkart_project\\Configurations\\config.ini")

class Readconfig():


    @staticmethod
    def get_registration_url():
        registration_url = config.get('User info', 'Registration_url')
        return registration_url

    @staticmethod
    def get_login_url():
        login_url = config.get('User info', 'Login_url')
        return login_url

    @staticmethod
    def get_name():
        name = config.get('User info', 'Name')
        return name

    @staticmethod
    def get_username():
        username = config.get('User info', 'Username')
        return username

    @staticmethod
    def get_password():
        password = config.get('User info', 'Password')
        return password


