import logging
from datetime import datetime
import sys
import os


class DummyLog:
    def __init__(self,
                 logName: str = datetime.now().strftime('%d_%m_%Y__%H_%M_%S'),
                 loggingLevel: str = 'debug',
                 stringFormat: str = '%(asctime)s: %(levelname)s: %(message)s',
                 datetimeFormat: str = '%m/%d/%Y %I:%M:%S %p',
                 logOnFolder: bool = True,
                 logFolderName: str = 'logs'
                 ):
        self.logName = logName
        self.logger = None
        self.loggingLevel = loggingLevel
        self.stringFormat = stringFormat
        self.datetimeFormat = datetimeFormat

        if logOnFolder:
            if not os.path.exists(logFolderName):
                os.mkdir(logFolderName)
            self.logName = logFolderName + '/' + self.logName

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
