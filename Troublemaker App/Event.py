from abc import ABC, abstractmethod
import datetime


class Event(ABC):

    static_reference = 0 # reference number
    occurence_time = datetime.datetime.now() # intially set to current time but will change when overloaded

    @abstractmethod
    def triggerEvent(self):
        pass