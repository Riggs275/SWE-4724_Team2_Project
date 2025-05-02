import os
import time
import psutil

# Protect these processes from being adjusted
SAFE_PROCESSES = ["prometheus", "grafana", "node_exporter", "auto_resolver", "python3"]

def is_safe(proc):
    try:
        name = proc.name()
        for safe in SAFE_PROCESSES:
            if safe.lower() in name.lower():
                return True
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return True
    return False

def cleanup_cpu():
    print("🧩 Attempting to relieve CPU usage...")
    psutil.cpu_percent(interval=0.1)  # Prime the data
    
    cpu_procs = [(p, p.cpu_percent(interval=0.1)) for p in psutil.process_iter(['pid', 'name'])]
    cpu_procs.sort(key=lambda x: x[1], reverse=True)

    adjusted = 0
    for proc, cpu_percent in cpu_procs[:10]:
        try:
            if is_safe(proc):
                print(f"🔒 Skipping safe process: {proc.pid} ({proc.name()})")
                continue
            if cpu_percent < 5:
                break  # Skip low-CPU processes
            proc.nice(10)
            print(f"🔻 Lowered priority of PID {proc.pid}, CPU: {cpu_percent:.2f}%")
            adjusted += 1
        except Exception as e:
            print(f"⚠️ Could not adjust PID {proc.pid}: {e}")
    print(f"✅ CPU priority adjustment complete. {adjusted} processes updated.\n")

if __name__ == "__main__":
    cleanup_cpu()
