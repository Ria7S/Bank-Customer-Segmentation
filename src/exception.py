import sys

def error_message_detail(error, error_detail: sys):
    """
    Function to get the error message details.
    :param error: Exception object
    :param error_detail: sys object
    :return: str
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with error message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    """
    Custom Exception class to handle exceptions in the pipeline.
    :param error: Exception object
    :param error_detail: sys object
    """
    def __init__(self, error, error_detail: sys):
        super().__init__(error)
        self.error_message = error_message_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
