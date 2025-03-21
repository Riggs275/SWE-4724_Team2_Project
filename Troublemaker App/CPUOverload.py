
import time
from Event import Event

class CPUOverload(Event):
    # This function overloads the CPU for a specific duration.
    def __init__(self, intensity, occurence_time):
        super().__init__(intensity, occurence_time)

    def triggerEvent(self, duration=5):
    

        print(f"Overloading CPU for {duration} seconds...")
        end_time = time.time() + duration
        while time.time() < end_time:
            # Perform a busy wait to overload the CPU
            _ = sum(i * i for i in range(10000))
        print("CPU overload complete.")
        

    if __name__ == "__main__":
        triggerEvent(5)
