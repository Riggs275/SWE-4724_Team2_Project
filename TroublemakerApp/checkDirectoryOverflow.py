import os

DIR_TO_MONITOR = "/home/EValenc6/SWE-4724_Team2_Project/TroublemakerApp/overflow_test_dir"
OUTPUT_FILE = "/home/EValenc6/owl-monitoring/text-metrics/directory_overflow.prom"

try:
    file_count = len(os.listdir(DIR_TO_MONITOR))
except FileNotFoundError:
    file_count = 0

print(file_count)
#with open(OUTPUT_FILE, "w") as f:
  #  f.write("# HELP directory_file_count Number of files in overflow test dir\n")
   # f.write("# TYPE directory_file_count gauge\n")
    #f.write(f"directory_file_count {file_count}\n")
#/Users/evanv/owlEye/SWE-4724_Team2_Project/TroublemakerApp/checkDirectoryOverflow.py