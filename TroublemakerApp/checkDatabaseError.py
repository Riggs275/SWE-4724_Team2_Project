import os

LOG_DIR = "/home/EValenc6/SWE-4724_Team2_Project/TroublemakerApp/databaseError_test_dir"
OUTPUT_FILE = "/home/EValenc6/owl-monitoring/text-metrics/log_error_flag.prom"

try:
    file_count = len(os.listdir(LOG_DIR))
except FileNotFoundError:
    file_count = 0

print(file_count)
with open(OUTPUT_FILE, "w") as f:
    f.write("# HELP directory_file_count Number of files in overflow test dir\n")
    f.write("# TYPE directory_file_count gauge\n")
    f.write(f"log_error_flag {file_count}\n")
