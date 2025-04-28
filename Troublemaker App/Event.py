from abc import ABC, abstractmethod
import datetime

class Event(ABC):
    static_reference = 0  

    def __init__(self, intensity, occurence_time):
        Event.static_reference += 1
        self.reference_id = f"E{Event.static_reference:04d}"  # Ex: E0001
        self.intensity = intensity
        self.occurence_time = occurence_time or datetime.datetime.now()

    @abstractmethod
    def triggerEvent(self):
        pass
