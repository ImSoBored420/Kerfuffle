import webbrowser
import time
from datetime import datetime
import os
import abbreviate #omg it's a custom *module I'm so good hacker man :sunglasses:

log = open("logs.txt", "a")
log.write(f"[{datetime.now()}] Kerfuffle Opened\n")
print("""\033[1;35m
 ____  __.             _____       _____  _____.__           
|    |/ _|____________/ ____\_ ___/ ____\/ ____\  |   ____   
|      <_/ __ \_  __ \   __\  |  \   __\\   __\|  | _/ __ \  
|    |  \  ___/|  | \/|  | |  |  /|  |   |  |  |  |_\  ___/  
|____|__ \___  >__|   |__| |____/ |__|   |__|  |____/\___  > 
        \/   \/                                          \/
©2024 Inf Potentiality""")
time.sleep(3)

while True:
    print("""\033[1;m      
==============================
\033[1;34m
1. Facebook 2. Twitter 3. Whitepages 4. Google 5. UsPhoneLookup
6. Searchpeoplefree 7. Truepeoplesearch  98. Experimental (all services) 
 \033[1;m      
==============================
\033[1;36m    99. About\033[1;33m   100. Other Tools    0. Exit\033[1;m
		""")
    menu:str = input("\033[1;mInput service to lookup?: ")
    
    match menu:
    
        #Facebook
        case "1":
            
            log.write(f"[{datetime.now()}] Option Facebook Chosen\n")
            
            while True: 
                
                choose:str = input("Name or phone number? (num): ")
                
                match choose:
                    
                    case "num":
                        
                        log.write(f"[{datetime.now()}] Facebook option 'num' chosen\n")
                        #phone numbers can be formatted differently, so don't specify type to avoid exceptions
                        FBnum = input("Phone number to look up with Facebook?: ")
                        log.write(f"[{datetime.now()}] Facebook phone number inputted: '{FBnum}'\n")
                        print("\033[1;35m\n bet \n")
                        webbrowser.open(f"[{datetime.now()}] https://www.facebook.com/search/top/?init=quick&q={FBnum}")
                        log.write(f"[{datetime.now()}] Facebook link opened: 'https://www.facebook.com/search/top/?init=quick&q={FBnum}'\n")
                        log.close()
                        break
                    case "name":
                        
                        FBfirst:str = input("First name? (if none, press ENTER): ")
                        FBlast:str = input("Last name? (if none, press ENTER): ")
                        log.write(f"[{datetime.now()}] Facebook name inputted '{FBfirst}' + '{FBlast}'\n")
                        FBlocation:str = input("Do you know the general location of the person? (yes/no): ")
                        
                        if FBlocation == "no" or FBlocation == "n":
                            log.write(f"[{datetime.now()}] Facebook location option 'no' chosen\n")
                            print("\033[1;35m\nbet \n")
                            webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={FBfirst}+{FBlast}")
                            log.write(f"[{datetime.now()}] Facebook link opened: 'https://www.facebook.com/search/top/?init=quick&q={FBfirst}+{FBlast}'\n")
                            log.close()
                            break
                        
                        elif FBlocation == "yes" or FBlocation == "y":
                            log.write(f"[{datetime.now()}] Facebook location option 'yes' chosen\n")
                            FBlocation:str = input("What is the general location of the person?: ")
                            log.write(f"[{datetime.now()}] Facebook location inputted '{FBlocation}'\n")
                            print("\033[1;35m\nbet \n")
                            webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={FBfirst}+{FBlast}+{FBlocation}")
                            log.write(f"[{datetime.now()}] Facebook link opened: 'https://www.facebook.com/search/top/?init=quick&q={FBfirst}+{FBlast}+{FBlocation}'\n")
                            log.close()
                            break
                        
                    case _: 
                        log.write(f"[{datetime.now()}] Invalid input chosen \n")
                        print("Invalid Input!")
                        time.sleep(1)
        
        #Twitter 
        case "2":
            
            while True:
                
                choose:str = input("Name or phone number? (num): ")
                
                match choose:
                    
                    case "num":
                        
                        #not gonna add string type here in case they don't format it like (xxx)-xxx-xxxx
                        TWnum = input("Phone number to look up with Twitter?: ")
                        print("\033[1;35m\n bet \n")
                        webbrowser.open(f"https://twitter.com/search?q={TWnum}")
                        break
                    
                    case "name":
                        TWfirst:str = input("First name? (if none, press ENTER): ")
                        TWlast:str = input("Last name? (if none, press ENTER): ")
                        print("\033[1;35m\nbet \n")
                        webbrowser.open(f"https://twitter.com/search?q={TWfirst}+{TWlast}")
                        break
                    
                    case _: 
                        print("Invalid Input!")
                        time.sleep(1)
        
        #Whitepages (The GOAT)
        case "3":
            
            while True:
                
                choose:str = input("Name or phone number? (num): ")
                
                match choose:
                    
                    case "num":
                        #same as last time
                        WPnum = input("Phone number to look up with Whitepages?: ")
                        print("\033[1;35m\nbet \n")
                        webbrowser.open(f"https://www.whitepages.com/phone/{WPnum}")
                        break
                    
                    case "name":
                        WPfirst:str = input("First name? (if none, press ENTER): ")
                        WPlast:str = input("Last name? (if none, press ENTER): ")
                        print("\033[1;35m\nbet \n")
                        webbrowser.open(f"https://www.whitepages.com/name/{WPfirst}+{WPlast}")
                        break
                    
                    case _: 
                        print("Invalid Input!")
                        time.sleep(1)
            
        #Google
        case "4":
            
            while True:
                
                choose:str = input("name, phone number or both? (phone number only is 'num'): ")
                
                match choose:
                    
                    case "name":
                        Gfullname:str = input("Just give me their full name (if none, press ENTER, but that'd be goofy): ")
                        Glocation:str = input("Do you have their general location? (if not, press ENTER): ")
                        Goccupation:str = input("What about their job/occupation? (if none or don't know, press ENTER): ")
                        print("\033[1;35m\nbet \n")
                        webbrowser.open(f"https://www.google.com/search?q={Gfullname}+{Glocation}+{Goccupation}")
                        break
                    
                    case "num": 
                        #you know why I'm not adding types here atp
                        Gnum = input("What is their phone number?: ") 
                        print("\033[1;35m\nbet \n") 
                        webbrowser.open(f"https://www.google.com/search?q={Gnum}")
                        
                    case "both":
                        Gfullname:str = input("Just give me their full name (if none, press ENTER, but that'd be goofy): ")
                        #omg he's not gonna specify type for things possibly formatted both ways
                        Gnum = input("What is their phone number?: ")
                        Glocation:str = input("Do you have their general location? (if not, press ENTER): ")
                        Goccupation:str = input("What about their job/occupation? (if none or don't know, press ENTER): ")
                        print("\033[1;35m\nbet \n")
                        webbrowser.open(f"https://www.google.com/search?q={Gfullname}+{Gnum}+{Glocation}+{Goccupation}")
                        break
                    
                    case _: 
                        print("Invalid Input!")
                        time.sleep(1)
                    
        #USPhoneLookup
        case "5":
            
            while True:
                
                choose:str = input("This service is exclusively for phone numbers only located in the United States. Would you like to go back? (yes/no): ")
                
                if choose == "yes" or choose == "y":
                    print("\033[1;35m\nbet \n") 
                    break
                
                elif choose == "no" or choose == "n":
                    print("""
                        \033[1;36mPHONE NUMBER INPUT FORMATTING: 
                        -DO NOT use parenthesis for the area code [eg (xxx)-xxx-xxxx]
                        -USE DASHES where applicable
                        -DO NOT not* use dashes
                        EXAMPLE: xxx-xxx-xxxx
                        """)
                    #I'm not even gonna add comments to these anymore; you get it
                    UPLnum = input("\033[1;mWhat is the phone number of the person?: ")
                    print("\033[1;35m\nbet \n")
                    webbrowser.open(f"https://www.usphonebook.com/{UPLnum}")
                    break
                
                else: 
                    print("Invalid Input!")
                    time.sleep(1)
                    
        #searchpeoplefree
        case "6":
            
            while True:
                
                choose:str = input("name, name and general location, or number? (name and general location is 'both', and number is 'number'): ")
                
                match choose:
                    
                    case "name":
                        SPFname:str = input("name?: ")
                        print("\033[1;35m\nbet \n")
                        webbrowser.open(f"https://www.searchpeoplefree.com/find/{SPFname}")
                        break
                    
                    case "both":
                        SPFname:str = input("name?: ")
                        print("by the way the program might tweak if you use something uppercase (fixed but I don't wanna get rid of this print)")
                        SPFlocation:str = input("location? (only the state): ")
                        SPFlocation2 = SPFlocation.lower()
                        short_state = abbreviate.abbreviate_state(f"{SPFlocation2}")
                        SPFcity:str = input("city/town?: ") 
                        print("\033[1;35m\nbet \n")
                        webbrowser.open(f"https://www.searchpeoplefree.com/find/{SPFname}/{short_state}/{SPFcity}")
                        break
                    
                    case "number":
                        #*I'm aware I specified, but also come on what do you want from me :(
                        #Not even gonna lie, it works even with type specification, but I'm paranoid
                        SPFnumber = input("what's the number (no dashes or parenthesis for the area code): ")
                        print("\033[1;35m\nbet \n")
                        webbrowser.open(f"https://www.searchpeoplefree.com/phone-lookup/find/{SPFnumber}")
                        break
                    
                    case _:
                        print("Invalid Input!")
                        time.sleep(1)
                    
        #truepeoplesearch
        case "7":
            
            while True:
                
                print("""\033[1;36mCouple things:
                            there are like a TON of options for this one so bear with me here:
                            name, phone, address, and email.
                            make your choice, and since I haven't implemented a way to use multiple at once, just use it multiple times?""")
                choose:str = input("\033[1;choose: ")
                
                match choose:
                    
                    case "name":
                        TPSname:str = input("put in their full name: ")
                        print("\033[1;35m\nbet \n")
                        webbrowser.open(f"https://www.truepeoplesearch.com/results?name={TPSname}")
                        break
                    
                    case "phone":
                        #no
                        TPSnumber = input("put in their phone number: ")
                        print("\033[1;35m\nbet \n")
                        webbrowser.open(f"https://www.truepeoplesearch.com/resultphone?phoneno={TPSnumber}")
                        break
                    
                    case "address":
                        #mixed use letters and numbers
                        TPSaddress:str = input("put in their home address: ")
                        print("\033[1;35m\nbet \n")
                        webbrowser.open(f"https://www.truepeoplesearch.com/resultaddress?streetaddress={TPSaddress}")
                        break
                    
                    case "email":
                        #probably works
                        TPSemail:str = input("put in their email address")
                        print("\033[1;35m\nbet \n")
                        webbrowser.open(f"https://www.truepeoplesearch.com/resultemail?email={TPSemail}")
                        break   
                    
                    case _:
                        print("Invalid Input!")
                        time.sleep(1)       
                    
        #The short awaited and very buggy experimental all option
        case "98":
            
            print("""
                        \033[1;36mPLEASE NOTE:
                        THIS IS AN EXPERIMENTAL FEATURE, AND THEREFORE MAY BE UNRELIABLE (also it only works for phone numbers so far)
                        """)
            print("""
                        PHONE NUMBER INPUT FORMATTING: 
                        -DO NOT use parenthesis for the area code [eg (xxx)-xxx-xxxx]
                        -USE DASHES where applicable
                        -DO NOT not* use dashes
                        EXAMPLE: xxx-xxx-xxxx
                        """)
            choose:str = input("\033[1;mStill continue?: ") 
            
            if choose == "yes" or choose == "y":
                #I'll have two number 9s, a number 9 large, a number 6 with extra dip, a number 7, two number 45s, one with cheese, and a large soda
                ALLnum = input("What is the person's number?: ")
                webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={ALLnum}")
                webbrowser.open(f"https://twitter.com/search?q={ALLnum}")
                webbrowser.open(f"https://www.whitepages.com/phone/{ALLnum}")
                webbrowser.open(f"https://www.google.com/search?q={ALLnum}")
                webbrowser.open(f"https://www.usphonebook.com/{ALLnum}")
                
            elif choose == "no" or choose == "n":
                print("\033[1;35m\nbet \n") 
                break
            
            else: 
                print("Invalid Input!")
                time.sleep(1)
                

        #About
        case "99":
            print("""\033[1;34mOne of the most simplistic and sub-par lookup tools ever made, mostly out of boredom. Input the name and/or number(s) of who you wanna find, and the OSINT gods bestow their knowledege upon thee (if any).\033[1;m""")
            time.sleep(1.5)
            
        #Other Tools
        case "100":
            print("""\033[0;32m
__  __                      _          __  __ 
|  \/  |                    | |        / _|/ _|
| \  / | ___  _ __ ___   ___| |_ _   _| |_| |_ 
| |\/| |/ _ \| '__/ _ \ / __| __| | | |  _|  _|
| |  | | (_) | | |  __/ \__ \ |_| |_| | | | |  
|_|  |_|\___/|_|  \___| |___/\__|\__,_|_| |_|  
Still ©2024 Inf Potentiality""")
            time.sleep(3)
            print("""\033[1;m      
    ==============================
    \033[1;34m
    1. DoS-ish 2. 
    \033[1;m      
    ==============================
    \033[1;36m    99. About\033[1;33m 0. Exit\033[1;m
    """)
            while True:
                
                EXmenu:str =input("\033[1;mInput service to run?: ")
                
                match EXmenu:
                    
                    case "1":
                        
                        while True:
                            
                            print("This program attempts a Denial of Service attack on whatever target you want.")
                            print("\033[1;33mDISCLAIMER: I am not responsible for misuse of this program. Only use this program with express permission from the person this is used on.")
                            target:str = input("\033[1;mInput the IP address or the hostname of your target: ")
                            #omg integer specification; we're in the future now people :sunglasses:
                            size:int = input("How many bytes of data per ping should be sent? (max 65500): ")
                            
                            if size > 65500 or size <= 0:
                                print("Invalid data size!")
                                time.sleep(1)
                                break
                            
                            times:str = input("How many instances would you like to be ran?: ")
                            for i in range(times):
                                os.system(f"start cmd /k ping {target} -l {size} -t")
                            print("Done")
                            break
                        
                    #Extra About
                    case "99":
                        print("This is a continuation to the unpopular program by me, Kerfuffle. Now instead of JUST info gathering, there are even more sub-par things to do!")
                        time.sleep(1.5)
                        
                    #Extra Exit
                    case "0":
                        print("\033[1;34mReturning to menu...")
                        time.sleep(1)
                        break
                    
                    case _:
                        print("Invalid Input!")
                        time.sleep(1)
                        
        #Exit
        case "0":
            print("""\033[1;34mThanks for using this ig!""")
            time.sleep(0.5)
            print("""\033[1;34mClosing...\033[1;m""")
            time.sleep(1)
            break
        
        case _: 
            print("Invalid Input!")
            time.sleep(1)
            
