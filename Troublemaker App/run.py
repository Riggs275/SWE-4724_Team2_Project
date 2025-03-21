import time
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
            print("1. Run CPU overload test\n2. Run a Directory Overflow test\n3. Run Memory Spike Test\n"
            "4. Run Database File Corruption Test\n5. Schedule the Stress Tests Above\n0. Exit\nSelection: ")
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
                        
                        while True:
                            try:
                                repeat = int(input("How many times would you like it to repeat with 4 second intervals? (Max 5): "))
                                repeat = min(repeat,5)
                                break 
                            except Exception as e:
                                print("Error: " + str(e))
                            
                        overflowInstance = DirectoryOverflow(level, None)
                        for i in range(repeat):
                            print(f"\n--- Spike Iteration {i+1} ---")
                            result = overflowInstance.triggerEvent()

                            print(f"Stats: {result}")
                            time.sleep(4)
                    case 3:
                        #Run Memory Spike Test
                        #Since we want the overload to run now don't send in a date.time
                        while True:
                            intensity= input("What intensity would you like to run it on? (Low, Medium, High):").lower()
                            #Since we want the overload to run now don't send in a date.time
                            if intensity == "low":
                                level = Intensity(1)
                                break
                            elif intensity == "medium":
                                level = Intensity(2)
                                break
                            elif intensity == "high":
                                level = Intensity(3)
                                break
                            else:
                                print("Select a correct option (low, medium, high)")
                        
                        while True:
                            try:
                                repeat = int(input("How many times would you like it to repeat with 4 second intervals? (Max 5): "))
                                repeat = min(repeat,5)
                                break 
                            except Exception as e:
                                print("Error: " + str(e))

                        
                        memorySpike = MemorySpike(level, None)

                        for i in range(repeat):
                            print(f"\n--- Spike Iteration {i+1} ---")
                            result = memorySpike.triggerEvent()

                            print(f"Stats: {result}")
                            time.sleep(4)
                        

                    case 4:
                        #Run Database Log File Corruption Test
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

                        while True:
                            try:
                                repeat = int(input("How many times would you like it to repeat? (Max 5)"))
                                repeat = min(repeat,5)
                                break 
                            except Exception as e:
                                print("Error: " + str(e))
                        

                        databaseError = DatabaseError(intensity,level)

                        for i in range(repeat):
                            print(f"\n--- Database Iteration {i+1} ---")
                            result = databaseError.triggerEvent()

                            print(f"Stats: {result}")
                            time.sleep(4)
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
        


troubleMaker = run()
Runner = troubleMaker.run()