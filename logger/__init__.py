import logging

class CustomLogger:

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    
    def __init__(self, name, file_log_level=logging.DEBUG, console_log_level=logging.ERROR):
        """
        Initialize the CustomLogger with the specified file and console log levels.
        
        :param name: Name of the logger (typically __name__)
        :param file_log_level: The logging level for file output (default is DEBUG)
        :param console_log_level: The logging level for console output (default is ERROR)
        """
        # Use __name__ to get the name of the current module
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Create file handler which logs even debug messages
        file_handler = logging.FileHandler(f"{name}.log")
        file_handler.setLevel(file_log_level)

        # Create console handler with higher log levels
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_log_level)

        # Define a custom formatter for color-coded log levels
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

    def log_with_color(self, level, msg):
        """Log a message with a color based on log level."""
        if level == logging.DEBUG:
            color = self.grey
        elif level == logging.INFO:
            color = self.yellow
        elif level == logging.WARNING:
            color = self.yellow
        elif level == logging.ERROR:
            color = self.red
        elif level == logging.CRITICAL:
            color = self.bold_red
        else:
            color = self.reset

        # Log the message with color
        formatted_msg = f"{color}{msg}{self.reset}"
        self.logger.log(level, formatted_msg)

