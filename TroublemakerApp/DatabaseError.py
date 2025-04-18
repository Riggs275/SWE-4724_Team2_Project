import datetime
import random
import os

from Event import Event
from Intensity import Intensity


class DatabaseError(Event):
    def __init__(self, intensity: Intensity, occurance: datetime):
        super().__init__(intensity, occurance)
    
    def triggerEvent(self):

        # Simulates a database error
        connection_errors = [
            "Connection timed out",
            "Too many connections",
            "Authentication failed",
            "Query execution error",
            "Deadlock detected"
        ]

        error_message = random.choice(connection_errors)
        print(f"Database error: {error_message}")

        # Simulate increasing database latency
        query_time = random.uniform(1.0, 10.0)
        print(f"Query execution time: {query_time:.2f} seconds")

        # Simulate failed transactions
        transaction_status = "Transaction successful"
        if random.random() < 0.7:  # 70% chance of transaction failure
            transaction_status = "Transaction rollback occurred"
        print(transaction_status)

        # ✅ Write error to a file in the monitored log directory
        log_dir = "/home/EValenc6/SWE-4724_Team2_Project/TroublemakerApp/databaseError_test_dir"
        os.makedirs(log_dir, exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_path = os.path.join(log_dir, f"db_error_{timestamp}.log")

        with open(log_path, "w") as f:
            f.write(f"{timestamp}\n")
            f.write(f"Database error: {error_message}\n")
            f.write(f"Query time: {query_time:.2f}s\n")
            f.write(f"{transaction_status}\n")

