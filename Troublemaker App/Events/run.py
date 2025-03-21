from EventHandler import EventHandler
from DatabaseError import DatabaseError
from DirectoryOverflow import DirectoryOverflow
from MemorySpike import MemorySpike
from Intensity import Intensity
#from Events import Intensity,EventHandler,DatabaseError,DirectoryOverflow,MemorySpike
#Trouble: EventHandler

class run:

    def __init__(self ):
        pass
        #self.trouble = Trouble
    
    
    def run(self):
        """
        This method will be the menu to add events and will take in a trouble maker class

        """
        print("Welcome to the Owl Eye Troublemaker")
        userOption = ""
        loop = True
        while(loop):
            #Menu
            print("1. Run CPU overload test\n2. Run a Memory Overload test\n3. Run excessive Memory test\n"
            "4. Run Log File Corruption Test\n5. Schedule the Stress Tests Above\n0. Exit\nSelection: ")
            try:
                userOption = int(input());
                match(userOption):
                    case 1:
                        #Run CPU Overload Test
                        intensity= input("What intensity would you like to run it on? (Low, Medium, High):")
                        #Since we want the overload to run now don't send in a date.time
                        print("Not done yet")
                    case 2:
                        #Run Directory Overflow test
                        while True:
                            intensity= input("What intensity would you like to run it on? (Low, Medium, High):").lower()
                            #Since we want the overload to run now don't send in a date.time
                            if intensity == "low":
                                level = (Intensity(1))
                                break
                            elif intensity == "medium":
                                level = (Intensity(2))
                                break
                            elif intensity == "high":
                                level = (Intensity(3))
                                break
                            else:
                                print("Select a correct option (low, medium, high)")
                            
                        overflowInstance = DirectoryOverflow(Event, intensity,level)
                        overflowInstance.triggerEvent()
                    case 3:
                        #Run Memory Spike Test
                        intensity= input("What intensity would you like to run it on? (Low, Medium, High):")
                        #Since we want the overload to run now don't send in a date.time
                        while True:
                            intensity= input("What intensity would you like to run it on? (Low, Medium, High):").lower()
                            #Since we want the overload to run now don't send in a date.time
                            if intensity == "low":
                                level = (Intensity(1))
                                break
                            elif intensity == "medium":
                                level = (Intensity(2))
                                break
                            elif intensity == "high":
                                level = (Intensity(3))
                                break
                            else:
                                print("Select a correct option (low, medium, high)")
                            
                        memorySpike = MemorySpike(intensity,level)
                        memorySpike.triggerEvent

                    case 4:
                        #Run Database Log File Corruption Test
                        intensity= input("What intensity would you like to run it on? (Low, Medium, High):")
                        #Since we want the overload to run now don't send in a date.time
                        while True:
                            intensity= input("What intensity would you like to run it on? (Low, Medium, High):").lower()
                            #Since we want the overload to run now don't send in a date.time
                            if intensity == "low":
                                level = (Intensity(1))
                                break
                            elif intensity == "medium":
                                level = (Intensity(2))
                                break
                            elif intensity == "high":
                                level = (Intensity(3))
                                break
                            else:
                                print("Select a correct option (low, medium, high)")
                            
                        databaseError = DatabaseError(intensity,level)
                        databaseError.triggerEvent()
                    case 5:
                        #Schedule A Test
                        print("not done yet")
                    case 0: 
                        print("Bye Bye\n")
                        loop = False

            except Exception as e:
                print("Wrong Input try again")
                print("Error: " + e)

        print("Owl Eye Shutting Down")
        


troubleMaker = EventHandler()
Runner = troubleMaker.run()