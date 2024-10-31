import webbrowser
import time
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
1. Facebook 2. Twitter 3. Whitepages 4. Google 
 \033[1;m      
==============================
\033[1;36m    99. About\033[1;33m    0. Exit\033[1;m
		""")
while True:
    menu = input("\033[1;m Input service to lookup?: ")
    
    #Facebook
    if menu == "1":
        while True: 
            choose = input("Name or phone number? (num): ")
            if choose == "num":
                FBnum = input("Phone number to look up with Facebook?: ")
                print("\033[1;35m\n bet \n")
                webbrowser.open("https://www.facebook.com/search/top/?init=quick&q="+FBnum)
                break
            elif choose == "name":
                FBfirst = input("First name? (if none, press ENTER): ")
                FBlast = input("Last name? (if none, press ENTER): ")
                FBlocation = input("Do you know the general location of the person? (yes/no): ")
                if FBlocation == "no" or FBlocation == "n":
                    print("\033[1;35m\n bet \n")
                    webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={FBfirst}+{FBlast}")
                elif FBlocation == "yes" or FBlocation == "y":
                    FBlocation = input("What is the general location of the person?: ")
                    print("\033[1;35m\n bet \n")
                    webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={FBfirst}+{FBlast}+{FBlocation}")
                break
            else: 
                print("Invalid Input!")
                time.sleep(1)
    
    #Twitter 
    elif menu == "2":
        while True:
            choose = input("Name or phone number? (num): ")
            if choose == "num":
                TWnum = input("Phone number to look up with Twitter?: ")
                print("\033[1;35m\n bet \n")
                webbrowser.open("https://twitter.com/search?q="+TWnum)
                break
            elif choose == "name":
                TWfirst = input("First name? (if none, press ENTER): ")
                TWlast = input("Last name? (if none, press ENTER): ")
                print("\033[1;35m\n bet \n")
                webbrowser.open(f"https://twitter.com/search?q={TWfirst}+{TWlast}")
                break
            else: 
                print("Invalid Input!")
                time.sleep(1)
    
    #Whitepages (The GOAT)
    elif menu == "3":
        while True:
            choose = input("Name or phone number? (num): ")
            if choose == "num":
                WPnum = input("Phone number to look up with Whitepages?: ")
                print("\033[1;35m\n bet \n")
                webbrowser.open(f"https://www.whitepages.com/phone/{WPnum}")
                break
            elif choose == "name":
                WPfirst = input("First name? (if none, press ENTER): ")
                WPlast = input("Last name? (if none, press ENTER): ")
                print("\033[1;35m\n bet \n")
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
                print("\033[1;35m\n bet \n")
                webbrowser.open(f"https://www.google.com/search?q={Gfullname}+{Glocation}+{Goccupation}")
                break
            elif choose == "num": 
                Gnum = input("What is their phone number?: ") 
                print("\033[1;35m\n bet \n") 
                webbrowser.open(f"https://www.google.com/search?q={Gnum}")
            elif choose == "both":
                Gfullname = input("Just give me their full name (if none, press ENTER, but that'd be goofy): ")
                Gnum = input("What is their phone number?: ")
                Glocation = input("Do you have their general location? (if not, press ENTER): ")
                Goccupation = input("What about their job/occupation? (if none or don't know, press ENTER): ")
                print("\033[1;35m\n bet \n")
                webbrowser.open(f"https://www.google.com/search?q={Gfullname}+{Gnum}+{Glocation}+{Goccupation}")
                break
            else: 
                print("Invalid Input!")
                time.sleep(1)

    #About
    elif menu == "99":
        print("""\033[1;34mOne of the most simplistic and sub-par lookup tools ever made, mostly out of boredom. Input the name and/or number(s) of who you wanna find, and the OSINT gods bestow their knowledege upon thee (if any).\033[1;m""")
        time.sleep(1.5)
    
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
        
