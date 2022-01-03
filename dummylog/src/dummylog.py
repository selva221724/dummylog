import logging
from datetime import datetime
import sys
import os


class DummyLog:
    def __init__(self,
                 log_name: str = 'temp',
                 logging_level: str = 'debug',
                 string_format: str = '%(asctime)s: %(levelname)s: %(message)s',
                 datetime_format: str = '%m/%d/%Y %I:%M:%S %p',
                 log_on_folder: bool = True,
                 log_folder_name: str = 'logs',
                 ):

        self.logName = log_name
        self.logger = None
        self.loggingLevel = logging_level
        self.stringFormat = string_format
        self.datetimeFormat = datetime_format

        if log_on_folder:
            if not os.path.exists(log_folder_name):
                os.mkdir(log_folder_name)
            self.logName = log_folder_name + '/' + self.logName

        self.initiateLogger()

    def initiateLogger(self):
        """ This function will initiate the logger as a single threaded log"""

        self.logger = logging.getLogger(self.logName)
        if self.loggingLevel == 'debug':
            self.loggingLevel = logging.DEBUG
        self.logger.setLevel(self.loggingLevel)
        logFormat = logging.Formatter(self.stringFormat, datefmt=self.datetimeFormat)

        # Creating and adding the console handler
        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setFormatter(logFormat)
        self.logger.addHandler(consoleHandler)

        # Creating and adding the file handler
        fileHandler = logging.FileHandler(self.logName + ".log", mode='w')
        fileHandler.setFormatter(logFormat)
        self.logger.addHandler(fileHandler)

    def kill(self):
        """ To kill the current handlers of the log"""
        handlers = self.logger.handlers[:]
        for handler in handlers:
            self.logger.removeHandler(handler)
            handler.flush()
            handler.close()
        self.logger = None
        self.logName = None
        self.loggingLevel = None
        self.stringFormat = None
        self.datetimeFormat = None
