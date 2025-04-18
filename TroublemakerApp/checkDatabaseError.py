import os

LOG_DIR = "/home/EValenc6/SWE-4724_Team2_Project/TroublemakerApp/databaseError_test_dir"
OUTPUT_FILE = "/home/EValenc6/owl-monitoring/text-metrics/log_error_flag.prom"

error_found = False

if os.path.exists(LOG_DIR):
    for filename in os.listdir(LOG_DIR):
        file_path = os.path.join(LOG_DIR, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r") as f:
                if "error" in f.read().lower():  # case-insensitive search
                    error_found = True
                    break

with open(OUTPUT_FILE, "w") as f:
    f.write("# HELP log_error_flag Whether an error is present in the log files\n")
    f.write("# TYPE log_error_flag gauge\n")
    f.write(f"log_error_flag {1 if error_found else 0}\n")
