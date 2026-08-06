"""
This script provides custom exception handling. It generates detailed error messages, 
pinpointing the exact file and line number to make debugging easier and faster.
"""

import sys # Imports the sys module to track system errors and execution details
from src.logger import logging # Imports our custom logger to record errors in a file

def error_message_detail(error, error_detail:sys): # Defines a function to extract precise details about the error
    _, _, exc_tb = error_detail.exc_info() # Gets the error traceback (exc_tb), ignoring the first two unused values
    file_name = exc_tb.tb_frame.f_code.co_filename # Digs into the traceback to extract the exact file name where the error happened
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format( # Prepares a clean, formatted text template
     file_name, exc_tb.tb_lineno, str(error)) # Fills the template with the file name, line number, and original error text

    return error_message # Returns the final, easy-to-read error string

class CustomException(Exception): # Creates our wrapper class that inherits from Python's built-in Exception class
    def __init__(self, error_message, error_detail:sys): # The constructor method that runs when the error is triggered
        super().__init__(error_message) # Passes the basic error to the parent (Python) so it still acts like a real error
        self.error_message = error_message_detail(error_message, error_detail=error_detail) # Uses our function to create and store the detailed error message
    
    def __str__(self): # A built-in method that dictates what happens if we print() this error
        return self.error_message # Forces Python to print our detailed message instead of its default messy output
        return self.error_message


