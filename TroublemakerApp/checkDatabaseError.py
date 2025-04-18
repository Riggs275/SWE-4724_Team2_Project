LOG_PATH = "/home/EValenc6/myapp.log"
OUTPUT_FILE = "/home/EValenc6/owl-monitoring/text-metrics/log_error_flag.prom"

with open(LOG_PATH, "r") as f:
    log_data = f.read()

error_flag = 1 if "ERROR" in log_data else 0

with open(OUTPUT_FILE, "w") as f:
    f.write(f'# HELP log_error_flag Whether an error is present in the log file\n')
    f.write(f'# TYPE log_error_flag gauge\n')
    f.write(f'log_error_flag {error_flag}\n')
