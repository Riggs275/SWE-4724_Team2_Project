import os

LOG_DIR = "/home/EValenc6/SWE-4724_Team2_Project/TroublemakerApp/databaseError_test_dir"
OUTPUT_FILE = "/home/EValenc6/owl-monitoring/text-metrics/log_error_flag.prom"

try:
    file_count = len(os.listdir(LOG_DIR))
except FileNotFoundError:
    file_count = 0
