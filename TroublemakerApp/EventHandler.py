import datetime
from MemorySpike import MemorySpike
from DatabaseError import DatabaseError
# from CPUOverload import CPUOverload (when ready)
from DirectoryOverflow import DirectoryOverflow
from Intensity import Intensity

class EventHandler:
    Event_List = []

    def __init__(self):
        pass

    def addEvent(self, type: str, occurence: datetime, intensity: Intensity) -> str:
        try:
            if type == "CPU Overload":
                # Call overloaded CPU Overload class and append (add) to list
                print("Not done yet")
                #event = CPUOverload(intensity, occurence)
                #self.Event_List.append(event) 
            elif type == "Memory Spike":
                # Call overloaded Memory Spike class and append (add) to list
                event = MemorySpike(intensity, occurence)
                self.Event_List.append(event)
            elif type == "Database Error":
                # Call overloaded Database Error class and append (add) to list
                event = DatabaseError(intensity, occurence)
                self.Event_List.append(event)
            elif type == "Directory Overflow":
                # Call overloaded Directory Overflow class and append (add) to list
                event = DirectoryOverflow(intensity, occurence)
                self.Event_List.append(event)
                
            else:
                raise TypeError("None of the types match available event classes")
            return f"{type} added for {occurence.strftime('%Y-%m-%d %H:%M:%S')} with intensity {intensity}"

        except Exception as e:
            return "error: " + e

    def removeEvent(self, referenceNum: int) -> str:
        try:
            for event in self.Event_List:
                if event.static_reference == referenceNum:
                    self.Event_List.remove(self.Event_List.index(referenceNum))
                    return "Removed"
            return "Reference number not found"
        except Exception as e:
            return "error: " + e
        
    def checkForEvent(self):
        for event in self.Event_List:
            if event.occurence_time == datetime.datetime.now():
                event.triggerEvent()