import os

DIR_TO_MONITOR = "/home/EValenc6/tmp-stress"
MAX_FILES = 100
OUTPUT_FILE = "/home/EValenc6/owl-monitoring/text-metrics/directory_overflow.prom"

file_count = len(os.listdir(DIR_TO_MONITOR))

with open(OUTPUT_FILE, "w") as f:
    f.write(f'# HELP directory_file_count Number of files in monitored directory\n')
    f.write(f'# TYPE directory_file_count gauge\n')
    f.write(f'directory_file_count {file_count}\n')
