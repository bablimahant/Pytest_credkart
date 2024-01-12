import inspect

import logging

class Logging_class:

    @staticmethod
    def log_generator():
        name =inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("C:\\Babli\\python_revision_2\\Pytest_python_projects\\Pytest_credkart_project\\Logs\\Automation.log")
        format = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(funcName)s:%(message')
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger






# class Logging_class:
#
#     @staticmethod
#     def log_generator():
#         logging.basicConfig(filename="C:\Babli\python_revision_2\Pytest_python_projects\Pytest_credkart_project\Logs\Automation.log",
#                             format='%(asctime)s: %(levelname)s: %(message)',
#                             datefmt='%m%d%Y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger





