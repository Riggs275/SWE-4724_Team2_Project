import os
import time
import psutil


def cleanup_cpu():
    print("🧩 Attempting to relieve CPU usage...")
    cpu_procs = [(p.pid, p.info['cpu_percent']) for p in psutil.process_iter(['pid', 'cpu_percent'])]
    cpu_procs.sort(key=lambda x: x[1], reverse=True)

    adjusted = 0
    for pid, cpu_percent in cpu_procs[:5]:
        try:
            p = psutil.Process(pid)
            p.nice(10)
            print(f"🔻 Lowered priority of PID {pid}, CPU: {cpu_percent:.2f}%")
            adjusted += 1
        except Exception as e:
            print(f"⚠️ Could not adjust PID {pid}: {e}")
    print(f"✅ CPU priority adjustment complete. {adjusted} processes updated.\n")


if __name__ == "__main__":
    cleanup_cpu()