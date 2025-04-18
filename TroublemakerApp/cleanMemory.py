import gc
import psutil


def cleanup_memory():
    print("🧠 Attempting to clean up memory...")
    gc.collect()

    mem_procs = [(p.pid, p.info['memory_info'].rss) for p in psutil.process_iter(['pid', 'memory_info'])]
    mem_procs.sort(key=lambda x: x[1], reverse=True)

    cleaned = 0
    for pid, mem_usage in mem_procs[:5]:
        try:
            p = psutil.Process(pid)
            print(f"🛑 Terminating high-memory process: PID {pid}, Memory: {mem_usage / (1024 * 1024):.2f} MB")
            p.terminate()
            cleaned += 1
        except Exception as e:
            print(f"⚠️ Could not terminate PID {pid}: {e}")
    print(f"✅ Memory cleanup complete. {cleaned} processes terminated.\n")


if __name__ == "__main__":
    cleanup_memory()