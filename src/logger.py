"""
This script configures the logging system. It records execution steps, events, 
and errors into a text file to track and monitor the project's background workflow.
"""

import logging # Imports the built-in logging module to track events
import os # Imports the OS module to interact with the file system (create folders, paths)
from datetime import datetime # Imports datetime to stamp our log files with the exact time

# 1. Create a dynamic file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the path for the logs folder in the current working directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# 3. Create the directory. 'exist_ok=True' prevents errors if the folder already exists
os.makedirs(logs_path, exist_ok=True)

# 4. Define the complete, final path where the actual log file will be saved
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# 5. Configure the global logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH, # Set the file destination
    # Define the structure of each log message: [Time] Line_Number Name - Level - Message
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO, # Set the minimum severity level to record (INFO and above)
)

