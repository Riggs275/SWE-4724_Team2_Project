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

    mem_procs = [(p.pid, p.info['memory_info'].rss) for p in psutil.process_iter(['pid', 'memory_info'])]
    mem_procs.sort(key=lambda x: x[1], reverse=True)

    cleaned = 0
    for proc in high_memory_procs:
        
        try:
            mem = proc.memory_info().rss/(1024*1024)
            if mem < 100:
                print(f"🔒 Skipping low memory process: {proc.pid} ({proc.name()})")
                continue  # Skip low-usage processes
            if is_safe(proc):
                print(f"🔒 Skipping safe process: {proc.pid} ({proc.name()})")
                continue

            print(f"🛑 Terminating high-memory process: PID {proc.pid}, Memory: {mem:.2f} MB")
            proc.terminate()
            proc.wait(timeout=3)
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            print(f"⚠️ Could not terminate PID {proc.pid}: {e}")
    print(f"✅ Memory cleanup complete. {cleaned} processes terminated.\n")


if __name__ == "__main__":
    cleanup_memory()