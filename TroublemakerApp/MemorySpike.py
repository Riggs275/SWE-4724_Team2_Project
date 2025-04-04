import datetime
import time
from Intensity import Intensity
import subprocess
import re
from Event import Event

class MemorySpike(Event):
    MAX_MB = 2000  # Safety cap: max 2GB allocation
    CHUNK_SIZE = 10**6  # 1MB

    def __init__(self, intensity: Intensity, occurence: datetime):
        super().__init__(intensity,occurence)
        MemorySpike.static_reference += 1
        self.reference = MemorySpike.static_reference

    def get_available_memory_bytes(self):
        try:
            with open('/proc/meminfo', 'r') as f:
                meminfo = f.read()
            match = re.search(r'MemAvailable:\s+(\d+)\s+kB', meminfo)
            if match:
                kb = int(match.group(1))
                return kb * 1024  # convert to bytes
        except Exception as e:
            print(f"/proc/meminfo parse failed: {e}")
        return None

    def log_system_memory(self, label=""):
        mem = self.get_available_memory_bytes()
        if mem:
            print(f"{label}Available system memory: {mem // (1024 ** 2)} MB")
        
    def triggerEvent(self, dry_run=False):
        print(f"[{datetime.datetime.now()}] Triggering Memory Spike - Intensity: {self.intensity}")
        spike_data = []
        self.log_system_memory("Before spike - ")

        try:
            avail_mem = self.get_available_memory_bytes()
            if not avail_mem:
                print("Unable to determine system memory — using fallback")
                num_chunks = 250
            else:
                if self.intensity == Intensity.Low:
                    target_usage = int(avail_mem * 0.4)
                elif self.intensity == Intensity.Medium:
                    target_usage = int(avail_mem * 0.6)
                elif self.intensity == Intensity.High:
                    target_usage = int(avail_mem * 0.9)
                else:
                    print("Unknown intensity")
                    return None

                num_chunks = target_usage // self.CHUNK_SIZE
                num_chunks = min(num_chunks, self.MAX_MB)

            print(f"Attempting to allocate ~{num_chunks}MB of memory")

            if dry_run:
                print("[Dry Run] Allocation skipped.")
                return {
                    "intensity": self.intensity,
                    "chunks": num_chunks,
                    "used_mb": num_chunks,
                    "timestamp": datetime.datetime.now(),
                    "dry_run": True
                }


            spike_data = [bytearray(self.CHUNK_SIZE) for _ in range(num_chunks)]
            time.sleep(5)

        except MemoryError:
            print("Memory spike caused an error!")
        finally:
            del spike_data
            print("Memory released after spike")
            self.log_system_memory("After spike  - ")

        return {
            "intensity": self.intensity,
            "chunks": num_chunks,
            "used_mb": num_chunks,
            "timestamp": datetime.datetime.now(),
            "dry_run": False
        }


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()

    from MemorySpike import MemorySpike
    import datetime
    intensity = Intensity(3)
    event = MemorySpike(intensity,datetime.datetime.now())
    repeat = 3

    for i in range(repeat):
        print(f"\n--- Spike Iteration {i+1} ---")
        result = event.triggerEvent()
        print(f"Stats: {result}")
        time.sleep(4)

    tracemalloc.stop()
