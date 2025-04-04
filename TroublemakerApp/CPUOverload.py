import time
import threading
import os
from Event import Event
from Intensity import Intensity

class CPUOverload(Event):
    def __init__(self, intensity, occurence_time):
        super().__init__(intensity, occurence_time)

    def _burn_cpu(self, usage_percent, duration):
        interval = 0.1  # 100ms
        busy_time = interval * (usage_percent / 100.0)
        sleep_time = interval - busy_time

        end_time = time.time() + duration
        while time.time() < end_time:
            start = time.time()
            while (time.time() - start) < busy_time:
                _ = sum(i * i for i in range(1000))
            if sleep_time > 0:
                time.sleep(sleep_time)

    def triggerEvent(self, duration=5):
        core_count = os.cpu_count()

        if self.intensity == Intensity.Low:
            usage = 60   # % per core
            threads = max(1, core_count // 3)
        elif self.intensity == Intensity.Medium:
            usage = 75
            threads = max(1, core_count // 2)
        elif self.intensity == Intensity.High:
            usage = 85
            threads = core_count
        else:
            print("Unknown intensity")
            return

        print(f"Overloading CPU to ~{usage}% on {threads} cores for {duration} seconds...")

        thread_list = []
        for _ in range(threads):
            t = threading.Thread(target=self._burn_cpu, args=(usage, duration))
            t.start()
            thread_list.append(t)

        for t in thread_list:
            t.join()

        print("CPU overload complete.")
