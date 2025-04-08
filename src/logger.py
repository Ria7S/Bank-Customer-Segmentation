import logging
import os
from datetime import datetime

# Create logs directory path
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Set log file name with date
log_file = f"{datetime.now().strftime('%Y-%m-%d')}.log"
log_file_path = os.path.join(log_dir, log_file)

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    format='%(asctime)s %(message)s',
    level=logging.INFO,
)
