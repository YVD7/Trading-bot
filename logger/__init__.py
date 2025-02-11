import logging

class CustomLogger:
    def __init__(self, name):
        """
        Initialize the CustomLogger using the module's __name__.
        """
        # Use __name__ to get the name of the current module
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Create file handler which logs even debug messages
        file_handler = logging.FileHandler(f"{name}.log")
        file_handler.setLevel(logging.DEBUG)

        # Create console handler with higher log levels
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.ERROR)

        # Create formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        # Add formatter to handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        """Return the configured logger instance."""
        return self.logger
