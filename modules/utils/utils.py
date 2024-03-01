import logging
from datetime import datetime

def setup_logger(name, log_file, level=logging.INFO):
    """ Set up a logger for the application.

    Args:
        name (str): Name of the logger.
        log_file (str): File path for the log file.
        level (logging.Level): Logging level.

    Returns:
        logging.Logger: Configured logger.
    """
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def timestamp():
    """ Returns the current timestamp.

    Returns:
        str: Current timestamp in a readable format.
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def encrypt_password(password):
    """ Encrypts a password or sensitive data. (Placeholder function)

    Args:
        password (str): The password or data to encrypt.

    Returns:
        str: Encrypted password.
    """
    
    return password[::-1]  # Simple reverse for demonstration

def decrypt_password(encrypted_password):
    """ Decrypts an encrypted password or data. (Placeholder function)

    Args:
        encrypted_password (str): The encrypted password or data.

    Returns:
        str: Decrypted password.
    """
    # Placeholder for decryption logic
    return encrypted_password[::-1]  # Simple reverse for demonstration

# Additional utility functions can be added here as needed
# Common utilities and helper functions
