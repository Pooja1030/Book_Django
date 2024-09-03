# books/utils.py
import logging


logger = logging.getLogger(__name__)

def log_method_call(method):
    def wrapper(*args, **kwargs):
        logger.info(f"Calling method: {method.__name__}")
        response = method(*args, **kwargs)
        logger.info(f"Method {method.__name__} executed successfully")
        return response
    return wrapper
