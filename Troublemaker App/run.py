import TroubleMaker

class run:

    def __init__(self, Trouble: TroubleMaker):
        self.trouble = Trouble
    
    
    def run():
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
                        #Run Overload Test

                    case 2:
                        #Run Memory Overload test

                    case 3:
                        #Run Excessive Memory Test

                    case 4:
                        #Run Log File Corruption Test

                    case 5:
                        #Schedule A Test

                    case 0: 
                        print("Bye Bye\n")
                        loop = False

            except Exception as e:
                print("Wrong Input try again")
                print("Error: " + e)

        print("Owl Eye Shutting Down")
        


troubleMaker = TroubleMaker()
Runner = run(troubleMaker)