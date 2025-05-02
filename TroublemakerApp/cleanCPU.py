import os
import psutil

# Only protect these by keywords in their command line
SAFE_KEYWORDS = ["prometheus", "grafana", "node_exporter", "auto_resolver.py"]

def is_safe(proc):
    try:
        cmdline = " ".join(proc.cmdline())
        for keyword in SAFE_KEYWORDS:
            if keyword.lower() in cmdline.lower():
                return True
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return True
    return False

def cleanup_cpu():
    print("🧩 Attempting to relieve CPU usage...")
    psutil.cpu_percent(interval=0.1)

    cpu_procs = [(p, p.cpu_percent(interval=0.1)) for p in psutil.process_iter(['pid', 'cmdline'])]
    cpu_procs.sort(key=lambda x: x[1], reverse=True)

    adjusted = 0
    for proc, cpu_percent in cpu_procs[:10]:
        try:
            if is_safe(proc):
                print(f"🔒 Skipping protected: {proc.pid} - {' '.join(proc.cmdline())}")
                continue
            if cpu_percent < 5:
                break
            proc.nice(10)
            print(f"🔻 Lowered priority of PID {proc.pid}, CPU: {cpu_percent:.2f}%")
            adjusted += 1
        except Exception as e:
            print(f"⚠️ Could not adjust PID {proc.pid}: {e}")
    print(f"✅ CPU priority adjustment complete. {adjusted} processes updated.\n")

if __name__ == "__main__":
    cleanup_cpu()
