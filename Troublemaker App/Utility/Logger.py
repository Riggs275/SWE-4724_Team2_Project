import logging
import os

# Create logs/ directory if not present
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/troublemaker.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger("TroubleMakerLogger")
