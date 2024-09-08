print ("welcome to \nAdams test Site, V2")
print("where to go?")
print("1: print test!")
print("2: Device info")
print("3: Build a house! ")

answer=input("Where to go? ")
if answer=="1":
    print("Hello world!")
    
if answer=="2":
        import platform
        import os
        import sys
        
        def get_ios_device_info():
            # Gather general system information
            os_name = platform.system()
            os_version = platform.version()
            machine = platform.machine()
            processor = platform.processor()
            python_version = sys.version
        
            # Format and print the information
            print("\n==== iOS Device Information ====")
            print(f"Operating System    : {os_name}")
            print(f"OS Version          : {os_version}")
            print(f"Machine Type        : {machine}")
            print(f"Processor           : {processor}")
            print(f"Python Version      : {python_version}")
            print("===============================\n")
        
        # Call the function to display the info
        get_ios_device_info()
        
if answer=="3":
    print("Building a house!")
    print("      /\           ")
    print("     /  \          ")
    print("    /    \         ")
    print("    ------         ")
    print("   | [] []|        ")
    print("   |      |        ")
    print("   | [] []|        ")
    print("   --------        ")       
        