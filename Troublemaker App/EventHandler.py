import datetime

class EventHandler:

    Event_List = []

    def addEvent(self, type, occurence, intensity):
        if type == "CPU Overload":
            # Call overloaded CPU Overload class and append (add) to list
            self.Event_List.append() 
        elif type == "Memory Spike":
            # Call overloaded Memory Spike class and append (add) to list
            self.Event_List.append()
        elif type == "Database Error":
            # Call overloaded Database Error class and append (add) to list
            self.Event_List.append()
        elif type == "Directory Overflow":
            # Call overloaded Directory Overflow class and append (add) to list
            self.Event_List.append()
        else:
            pass

    def removeEvent(self, referenceNum):
        for event in self.Event_List:
            if event.static_reference == referenceNum:
                self.Event_List.remove(self.Event_List.index(referenceNum))

    def checkForEvent(self):
        enumIndex = int(0)
        for event in self.Event_List:
            if event.occurence_time == datetime.datetime.now():
                self.Event_List.index(enumIndex).triggerEvent()
            enumIndex + 1