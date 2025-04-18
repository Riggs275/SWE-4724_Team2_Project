from datetime import datetime, timedelta
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
    
    # Additional Cron Management Utilities
    def view_cron_jobs(self):
        print("\n--- Current Cron Jobs ---")
        os.system("crontab -l")
        print("-------------------------\n")

    def clear_all_cron_jobs(self):
        confirm = input("Are you sure you want to clear all TroubleMaker cron jobs? (1=yes/2=no): ").strip().lower()
        if confirm == "1":
            open("troublemaker_cron.txt", "w").close()  # Empty file
            os.system("crontab -r")
            print("✅ All TroubleMaker cron jobs cleared.\n")
        else:
            print("❌ Cancelled. No changes made.\n")

    def remove_specific_cron_job(self):
        try:
            with open("troublemaker_cron.txt", "r") as f:
                lines = f.readlines()

            if not lines:
                print("No cron jobs to remove.")
                return

            print("\n--- Scheduled Cron Jobs ---")
            for i, line in enumerate(lines):
                print(f"{i + 1}. {line.strip()}")

            index = int(input("Enter the number of the job to remove: ")) - 1
            if 0 <= index < len(lines):
                removed = lines.pop(index)
                with open("troublemaker_cron.txt", "w") as f:
                    f.writelines(lines)
                os.system("crontab troublemaker_cron.txt")
                print(f"✅ Removed: {removed.strip()}")
            else:
                print("❌ Invalid selection.")
        except Exception as e:
            print(f"Error: {e}")


    def scheduleEvent(self):
        print("What type of test would you like to schedule? ((1)cpu, (2)memory, (3)directory, (4)database): ")
        test_type = input().strip().lower()

        print("What intensity? ((1)Low, (2)Medium, (3)High)): ")
        intensity = input().strip().capitalize()
        if intensity not in ["1", "2", "3"]:
            print("Invalid intensity.")
            return
        intensity = int(intensity)

    

        day = int(input("Enter day of week to run (0=Sun, 1=Mon, ..., 6=Sat): ").strip())
        time_input = input("Enter time in HH:MM (24-hr format): ").strip()
        hour, minute = map(int, time_input.split(":"))
        weeks = int(input("Repeat for how many weeks (1,2,....99,-1=Indefinitely): ").strip())

        script_name = f"scheduled_{test_type}_test.sh"
        python_cmd = ""

        if test_type == "1":
            python_cmd = (
                f'from CPUOverload import CPUOverload; from Intensity import Intensity; '
                f'import datetime; CPUOverload(Intensity({intensity}), datetime.datetime.now()).triggerEvent()'
            )
        elif test_type == "2":
            python_cmd = (
                f'from MemorySpike import MemorySpike; from Intensity import Intensity; '
                f'import datetime; MemorySpike(Intensity({intensity}), datetime.datetime.now()).triggerEvent()'
            )
        elif test_type == "3":
            python_cmd = (
                f'from DirectoryOverflow import DirectoryOverflow; from Intensity import Intensity; '
                f'import datetime; DirectoryOverflow(Intensity({intensity}), datetime.datetime.now()).triggerEvent()'
            )
        elif test_type == "4":
            python_cmd = (
                f'from DatabaseError import DatabaseError; from Intensity import Intensity; '
                f'import datetime; DatabaseError(Intensity({intensity}), datetime.datetime.now()).triggerEvent()'
            )
        else:
            print("Invalid test type.")
            return

        # ✅ Create the .sh script regardless of whether we use `cron` or `at`
        with open(script_name, "w") as f:
            f.write("#!/bin/bash\n")
            f.write(f"cd {os.getcwd()}\n")
            f.write("export PYTHONPATH=$(pwd)/TroubleMakerApp\n")
            f.write(f"echo 'Running {script_name} at $(date)' >> ~/troublemaker_log.txt\n")
            f.write(f"python3 -c \"{python_cmd}\"\n")

        os.chmod(script_name, 0o755)
        if weeks != -1:
            now = datetime.now()
            first_run = now + timedelta((day - now.weekday()) % 7)
            first_run = first_run.replace(hour=hour, minute=minute, second=0, microsecond=0)

            for i in range(weeks):
                run_time = first_run + timedelta(weeks=i)
                at_time = run_time.strftime("%H:%M %m/%d/%Y")
                os.system(f'echo "{os.getcwd()}/{script_name}" | at {at_time}')
                print(f"Scheduled run {i+1} at {at_time}")
        else:
            cron_entry = f"{minute} {hour} * * {day} {os.getcwd()}/{script_name} # troublemaker_{test_type}_{intensity}\n"

            # Ensure troublemaker_cron.txt exists
            if not os.path.exists("troublemaker_cron.txt"):
                with open("troublemaker_cron.txt", "w") as f:
                    pass  # create empty file

            # Read existing cron jobs
            with open("troublemaker_cron.txt", "r") as f:
                existing_cron = f.read()

            # Add only if it's new
            if cron_entry not in existing_cron:
                with open("troublemaker_cron.txt", "a") as f:
                    f.write(cron_entry)
                os.system("crontab troublemaker_cron.txt")
                print("✅ Cron job scheduled.")
            else:
                print("⚠️ Cron job already exists. Skipping.")


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
            "4. Run Database File Corruption Test\n5. Scheduling Menu\n0. Exit\nSelection: ")
            try:
                userOption = int(input())
                if userOption == 1:
                    #Run CPU Overload test
                    while True:
                        intensity= input("What intensity would you like to run it on? ((1)Low, (2)Medium, (3)High):").strip().lower()
                        #Since we want the overload to run now don't send in a date.time
                        if intensity == "1":
                            level = (Intensity(1))
                            break
                        elif intensity == "2":
                            level = (Intensity(2))
                            break
                        elif intensity == "3":
                            level = (Intensity(3))
                            break
                        else:
                            print("Select a correct option ((1)Low, (2)Medium, (3)High))")
                    
                    while True:
                        try:
                            repeat = int(input("How many times would you like it to repeat with 4 second intervals? (Max 5): "))
                            repeat = min(repeat,5)
                            break 
                        except Exception as e:
                            print("Error: " + str(e))
                    
                    while True:
                        try:
                            duration = int(input("For how long in seconds? (Max 15 seconds): "))
                            duration = min(duration,15)
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
                        intensity= input("What intensity would you like to run it on? ((1)Low, (2)Medium, (3)High):").strip().lower()
                        #Since we want the overload to run now don't send in a date.time
                        if intensity == "1":
                            level = (Intensity(1))
                            break
                        elif intensity == "2":
                            level = (Intensity(2))
                            break
                        elif intensity == "3":
                            level = (Intensity(3))
                            break
                        else:
                            print("Select a correct option ((1)Low, (2)Medium, (3)High))")
                    
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
                        intensity= input("What intensity would you like to run it on? ((1)Low, (2)Medium, (3)High):").strip().lower()
                        #Since we want the overload to run now don't send in a date.time
                        if intensity == "1":
                            level = Intensity(1)
                            break
                        elif intensity == "2":
                            level = Intensity(2)
                            break
                        elif intensity == "3":
                            level = Intensity(3)
                            break
                        else:
                            print("Select a correct option ((1)Low, (2)Medium, (3)High))")
                    
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
                        intensity= input("What intensity would you like to run it on? ((1)Low, (2)Medium, (3)High):").strip().lower()
                        #Since we want the overload to run now don't send in a date.times
                        if intensity not in ["1","2","3"]:
                            print("Select a correct option (1, 2, 3)")
                        level = Intensity((int(intensity)))
                        break

                    while True:
                        try:
                            repeat = int(input("How many times would you like it to repeat? (Max 5)"))
                            repeat = min(repeat,5)
                            break 
                        except Exception as e:
                            print("Error: " + str(e))
                    

                    databaseError = DatabaseError(level,None)

                    for i in range(repeat):
                        print(f"\n--- Database Iteration {i+1} ---")
                        result = databaseError.triggerEvent()

                        print(f"Stats: {result}")
                        time.sleep(4)
                    databaseError.triggerEvent()
                if userOption == 5:
                    print("Welcome to the Scheduler")
                    while True:
                        print("1. Schedule a new event\n2. View Current Events\n3. Remove an Event\n4. Clear all Events\n0. Back to main menu")
                        userInput = input("").strip().lower()
                        if(userInput == "1"):
                            self.scheduleEvent(); 
                        elif(userInput == "2"):
                            self.view_cron_jobs()
                        elif(userInput == "3"):
                            self.remove_specific_cron_job()
                        elif(userInput == "4"):
                            self.clear_all_cron_jobs()
                        elif(userInput == "0"):
                            break
                        else:
                            print("Select one of the options (1,2,3,4,0)")                   
                if userOption ==  0: 
                    print("Bye Bye\n")
                    loop = False

            except Exception as e:
                print("Wrong Input try again")

        print("Owl Eye Shutting Down")
        


troubleMaker = run()
Runner = troubleMaker.run()