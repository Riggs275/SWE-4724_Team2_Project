import datetime

class EventHandler:

    Event_List = []

    def addEvent(self, type: str, occurence: datetime, intensity: str) -> str:
        try:
            if type == "CPU Overload":
                # Call overloaded CPU Overload class and append (add) to list
                event = CPUOverload(intensity, occurence)
                self.Event_List.append(event) 
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
            return type + " added for " + occurence + " with an intensity of " + intensity
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
        enumIndex = int(0)
        for event in self.Event_List:
            if event.occurence_time == datetime.datetime.now():
                self.Event_List.index(enumIndex).triggerEvent()
            enumIndex + 1