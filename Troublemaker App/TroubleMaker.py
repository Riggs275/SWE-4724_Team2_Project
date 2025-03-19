import datetime

class TroubleMaker:

    def __init__(self):
        self.eventList = []

    def addEvent(self, type: str, occurance: datetime, intensity: str) -> str:
        #Doesnt have an event class just yet
        try:
            if type == "CPUOverload":
                e = CPUOverload(intensity, occurance)
            elif type == "MemorySpike":
                e = MemorySpike(intensity,occurance)
            elif type == "DatabaseError":
                e = DatabaseError(intensity,occurance)
            elif type == "DirectoryOverflow":
                e = DirectoryOverflow(intensity,occurance)
            else:
                raise TypeError("None of the types match available event classes")
            
            self.eventList.append(e)
            return "Event Added"
        except Exception as e:
            return "error: " + e

    def removeEvent(self, referenceNum: int) -> str:
        try:
            for event in self.eventList:
                if event.referenceNum == referenceNum:
                    return "Removed"
            
            return "Reference number not found"
        except Exception as e:
            return "error: " + e


    def checkTriggerEvent(self):
        for event in self.eventList:
            print(type(event) + " | " + event.occurance + " | " + event.referenceNumber)


