import datetime
import random
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
        if random.random() < 0.7:  # 70% chance of transaction failure
            print("Transaction rollback occurred")
