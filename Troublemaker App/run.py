import time
import os
from EventHandler import EventHandler
from DatabaseError import DatabaseError
from DirectoryOverflow import DirectoryOverflow
from MemorySpike import MemorySpike
from Intensity import Intensity
from CPUOverload import CPUOverload
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
                userOption = int(input())
                if userOption == 1:
                    #Run CPU Overload test
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
                    
                    while True:
                        try:
                            duration = int(input("For how long in seconds? (Max 5 seconds): "))
                            duration = min(duration,5)
                            break
                        except Exception as e:
                            print("Error" + str(e))

                    cpuOverloadInstance = CPUOverload(level, None)
                    for i in range(repeat):
                        print(f"\n--- Spike Iteration {i+1} ---")
                        result = cpuOverloadInstance.triggerEvent(duration)
                        print(f"Stats: {result}")
                        time.sleep(4)                    
                if userOption ==  2:
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
                if userOption == 3:
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
                    

                if userOption ==  4:
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
                if userOption == 5:
                    print("What type of test would you like to schedule? (cpu, memory, directory, database): ")
                    test_type = input().strip().lower()

                    print("What intensity? (Low, Medium, High): ")
                    intensity = input().strip().capitalize()
                    if intensity not in ["Low", "Medium", "High"]:
                        print("Invalid intensity.")
                        return

                    print("When would you like to run it? (e.g., now + 1 minute or 16:30): ")
                    schedule_time = input().strip()

                    script_name = f"scheduled_{test_type}_test.sh"
                    python_cmd = ""

                    if test_type == "cpu":
                        python_cmd = (
                            f'from CPUOverload import CPUOverload; from Intensity import Intensity; '
                            f'import datetime; CPUOverload(Intensity.{intensity}, datetime.datetime.now()).triggerEvent()'
                        )
                    elif test_type == "memory":
                        python_cmd = (
                            f'from MemorySpike import MemorySpike; from Intensity import Intensity; '
                            f'import datetime; MemorySpike(Intensity.{intensity}, datetime.datetime.now()).triggerEvent()'
                        )
                    elif test_type == "directory":
                        python_cmd = (
                            f'from DirectoryOverflow import DirectoryOverflow; from Intensity import Intensity; '
                            f'import datetime; DirectoryOverflow(Intensity.{intensity}, datetime.datetime.now()).triggerEvent()'
                        )
                    elif test_type == "database":
                        python_cmd = (
                            f'from DatabaseError import DatabaseError; from Intensity import Intensity; '
                            f'import datetime; DatabaseError(Intensity.{intensity}, datetime.datetime.now()).triggerEvent()'
                        )
                    else:
                        print("Invalid test type.")
                        return

                    with open(script_name, "w") as f:
                        f.write("#!/bin/bash\n")
                        f.write(f"cd {os.getcwd()}\n")
                        f.write(f"python3 -c \"{python_cmd}\"\n")

                    os.chmod(script_name, 0o755)
                    os.system(f'echo "{os.getcwd()}/{script_name}" | at {schedule_time}')
                    print(f"✅ Scheduled {test_type} test at {schedule_time} with {intensity} intensity.")

                if userOption ==  0: 
                    print("Bye Bye\n")
                    loop = False

            except Exception as e:
                print("Wrong Input try again")
                print("Error: " + e)

        print("Owl Eye Shutting Down")
        


troubleMaker = run()
Runner = troubleMaker.run()