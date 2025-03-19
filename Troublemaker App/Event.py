from abc import ABC, abstractmethod


class Event(ABC):

    static_reference = 0 # reference number

    @abstractmethod
    def triggerEvent(self):
        pass