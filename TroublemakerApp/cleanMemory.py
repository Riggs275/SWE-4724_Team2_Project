import gc
import psutil

# Process names or substrings you want to exclude from termination
SAFE_PROCESSES = ["prometheus", "grafana", "node_exporter", "auto_resolver", "python3"]

def is_safe(proc):
    try:
        name = proc.name()
        for safe_name in SAFE_PROCESSES:
            if safe_name.lower() in name.lower():
                return True
        return False
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return True  # If unsure, don't kill

def cleanup_memory():
    print("🧠 Attempting to clean up memory...")
    gc.collect()

    # Define the high memory usage threshold (in bytes)
    mem_threshold = 100 * 1024 * 1024  # 100 MB

    # Gather processes using more than the threshold
    high_memory_procs = [p for p in psutil.process_iter(['pid', 'name', 'memory_info'])
                         if not is_safe(p) and p.info['memory_info'].rss > mem_threshold]

    high_memory_procs.sort(key=lambda p: p.info['memory_info'].rss, reverse=True)

    cleaned = 0
    for proc in high_memory_procs:
        try:
            mem = proc.memory_info().rss / (1024 * 1024)
            print(f"🛑 Terminating high-memory process: PID {proc.pid}, Memory: {mem:.2f} MB")
            proc.terminate()
            proc.wait(timeout=3)
            cleaned += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            print(f"⚠️ Could not terminate PID {proc.pid}: {e}")
    print(f"✅ Memory cleanup complete. {cleaned} processes terminated.\n")

if __name__ == "__main__":
    cleanup_memory()
