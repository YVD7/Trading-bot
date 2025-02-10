import logging

class Logger:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # create file handler which logs even debug messages
        fh = logging.FileHandler(f"{self.logger}.log")
        fh.setLevel(logging.DEBUG)

        # create console handler with to higher log levels
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        # 
        formatter = logging.Formatter("%")