
import time

# This function overloads the CPU for a specific duration.
def cpu_overload(duration=5):
   

    print(f"Overloading CPU for {duration} seconds...")
    end_time = time.time() + duration
    while time.time() < end_time:
        # Perform a busy wait to overload the CPU
        _ = sum(i * i for i in range(10000))
    print("CPU overload complete.")
    

    if __name__ == "__main__":
        cpu_overload(5)
