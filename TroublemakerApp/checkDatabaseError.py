import os

DIR_TO_SCAN = "/home/EValenc6/SWE-4724_Team2_Project/TroublemakerApp/databaseError_test_dir"
OUTPUT_FILE = "/home/EValenc6/owl-monitoring/text-metrics/log_error_flag.prom"

error_found = 0

try:
    if os.path.isdir(DIR_TO_SCAN):
        for filename in os.listdir(DIR_TO_SCAN):
            file_path = os.path.join(DIR_TO_SCAN, filename)
            if filename.endswith(".log") and os.path.isfile(file_path):
                with open(file_path, "r") as f:
                    if "ERROR" in f.read():
                        error_found = 1
                        break
except Exception as e:
    print(f"Error scanning directory: {e}")

with open(OUTPUT_FILE, "w") as f:
    f.write("# HELP log_error_flag Whether an error is present in the log files\n")
    f.write("# TYPE log_error_flag gauge\n")
    f.write(f"log_error_flag {error_found}\n")
