import logging
import os
from datetime import datetime
from from_root import from_root

# Define log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Correct logs directory path
log_folder = os.path.join(from_root(), 'logs')

# Ensure logs folder exists
if not os.path.exists(log_folder):
    os.makedirs(log_folder, exist_ok=True)
    print(f"Created logs folder at: {log_folder}")  # Debugging message

# Define full log file path
LOG_FILE_PATH = os.path.join(log_folder, LOG_FILE)

# Ensure logging writes to both file & console
logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),  # File logging
        logging.StreamHandler()  # Console logging
    ]
)

logging.info("Logging setup complete. Logs will be saved in the logs/ folder.")
