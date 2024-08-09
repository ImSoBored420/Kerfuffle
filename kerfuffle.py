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
1. Facebook 2. Twitter 3. Whitepages    
 \033[1;m      
==============================
\033[1;36m    99. About\033[1;33m    0. Exit\033[1;m
		""")
while True:
    menu = input("Input service to lookup?: ")
    if menu == "1":
        while True: 
            choose = input("name or phone number? (num): ")
            if choose == "num":
                FBnum = input("phone number to look up with Facebook?: ")
                webbrowser.open("https://www.facebook.com/search/top/?init=quick&q="+FBnum)
                break
            elif choose == "name":
                FBfirst = input("First name? (if none, press ENTER): ")
                FBlast = input("Last name? (if none, press ENTER): ")
                webbrowser.open(f"https://www.facebook.com/search/top/?init=quick&q={FBfirst}+{FBlast}")
                break
            else: 
                print("Invalid Input!")
                time.sleep(1)
    elif menu == "2":
        while True:
            choose = input("name or phone number? (num): ")
            if choose == "num":
                TWnum = input("phone number to look up with Twitter?: ")
                webbrowser.open("https://twitter.com/search?q="+TWnum)
                break
            elif choose == "name":
                TWfirst = input("First name? (if none, press ENTER): ")
                TWlast = input("Last name? (if none, press ENTER): ")
                webbrowser.open(f"https://twitter.com/search?q={TWfirst}+{TWlast}")
                break
            else: 
                print("Invalid Input!")
                time.sleep(1)
    elif menu == "3":
        while True:
            choose = input("name or phone number? (num): ")
            if choose == "num":
                WPnum = input("phone number to look up with Whitepages?: ")
                webbrowser.open("https://www.whitepages.com/phone/"+WPnum)
                break
            elif choose == "name":
                WPfirst = input("First name? (if none, press ENTER): ")
                WPlast = input("Last name? (if none, press ENTER): ")
                webbrowser.open(f"https://www.whitepages.com/name/{WPfirst}+{WPlast}")
                break
            else: 
                print("Invalid Input!")
                time.sleep(1)
    elif menu == "99":
        print("""\033[1;34mOne of the most simplistic and sub-par lookup tools ever made, mostly out of boredom. Input numbers and who you wanna find, and the OSINT gods bestow their knowledege upon thee (if any).\033[1;m""")
        time.sleep(1.5)
    elif menu == "0":
        print("""\033[1;34mThanks for using this ig!""")
        time.sleep(0.5)
        print("""\033[1;34mClosing...\033[1;m""")
        time.sleep(1)
        break
    else: 
        print("Invalid Input!")
        time.sleep(1)
        