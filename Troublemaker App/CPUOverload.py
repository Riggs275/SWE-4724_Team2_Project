import time
import threading
from Event import Event
from Intensity import Intensity

class CPUOverload(Event):
    def __init__(self, intensity, occurence_time):
        super().__init__(intensity, occurence_time)

    def _burn_cpu(self, usage_percent, duration):
        print(f"Overloading CPU to ~{usage_percent}% for {duration} seconds...")
        end_time = time.time() + duration
        interval = 0.1 

        busy_time = interval * (usage_percent / 100.0)
        sleep_time = interval - busy_time

        while time.time() < end_time:
            start = time.time()
            while (time.time() - start) < busy_time:
                _ = sum(i * i for i in range(1000))  # simulate CPU work
            time.sleep(sleep_time)

        print("CPU overload complete.")

    def triggerEvent(self, duration=5):
        if self.intensity == Intensity.Low:
            usage = 30
        elif self.intensity == Intensity.Medium:
            usage = 60
        elif self.intensity == Intensity.High:
            usage = 90
        else:
            print("Unknown intensity")
            return

        self._burn_cpu(usage, duration)
