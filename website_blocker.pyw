import tkinter as tk
import time
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list=[]

window = tk.Tk()
window.title('Website Blocker')

def validation():
    if len(entryStartingHour.get()) != 0 and len(entryEndHour.get()) != 0:
        if 0 <= int(entryStartingHour.get()) < 24 and 0 <= int(entryEndHour.get()) < 24 and int(entryEndHour.get()) > int(entryStartingHour.get()):
            if len(website_list) != 0:
                #Getting the start and end hour variables
                startingHour = int(entryStartingHour.get())
                endingHour = int(entryEndHour.get())
                window.destroy()
                #IF inputs are valid we can run the program and the list isn't empty
                while True:
                    if dt(dt.now().year, dt.now().month, dt.now().day, startingHour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, endingHour):
                        #print("working hours")
                        with open(hosts_path, 'r+') as file:
                            content = file.read()
                            for website in website_list:
                                #If it's there already pls don't add it again
                                if website in content:
                                    pass
                                else:
                                    file.write(redirect+ " " + website + "\n")
                    else:
                        with open(hosts_path, 'r+') as file:
                            content = file.readlines()
                            file.seek(0)
                            for line in content:
                                if not any(website in line for website in website_list):
                                    file.write(line)
                                file.truncate()
                    time.sleep(5)
            else:
                entryWebsites.focus_set()
        else:
            if int(entryStartingHour.get()) < 0 or int(entryStartingHour.get()) >= 24 :
                entryStartingHour.focus_set()
            elif int(entryEndHour.get()) < 0 or int(entryEndHour.get()) >= 24:
                entryEndHour.focus_set()
            elif int(entryEndHour.get()) < int(entryStartingHour.get()):
                entryEndHour.focus_set()

    else: #Is empty
        if len(entryStartingHour.get()) != 0:
            entryEndHour.focus_set()
        elif len(entryEndHour.get()) != 0:
            entryStartingHour.focus_set()

def add_websites():
    new_website = entryWebsites.get()
    #Validation so it doesn't append empty strings
    if len(new_website) == 0:
        entryWebsites.focus_set()
    else:
        website_list.append(new_website)
        entryWebsites.delete(0, "end")
        print(website_list)


labelStartingTime = tk.Label(window, text = "Enter starting hour(24h clock): ")
labelStartingTime.grid(column=0, row=0, ipadx=5, pady=5, sticky=tk.W+tk.N)

labelEndTime = tk.Label(window, text = "Enter end hour(24th clock): ")
labelEndTime.grid(column=0, row=1, ipadx=5, pady=5, sticky=tk.W+tk.S)

labelWebsites = tk.Label(window, text = "Enter a website to be blocked: ")
labelWebsites.grid(column=0, row=2, ipadx=5, pady=5, sticky=tk.W+tk.S)

entryStartingHour = tk.Entry(window, width=20)
entryStartingHour.grid(column=1, row=0, padx=10, pady=5, sticky=tk.N)

entryEndHour = tk.Entry(window, width=20)
entryEndHour.grid(column=1, row=1, padx=10, pady=5, sticky=tk.S)

entryWebsites = tk.Entry(window, width=20)
entryWebsites.grid(column=1, row=2, padx=10, pady=5, sticky=tk.S)

addWebsiteButton = tk.Button(window, text = 'Add', command=add_websites)
addWebsiteButton.grid(column=2, row=2, padx=10)

instructionsText = tk.Label(window, text = "Example website: Facebook.com \n*add* www.facebook.com *add*")
instructionsText.grid(column=1, row=3, ipadx=5, sticky=tk.W+tk.S, columnspan=2)

finishButton = tk.Button(window, text = 'Finish', command = validation)
finishButton.grid(column=1, row=4, pady=10, sticky=tk.S)

window.mainloop()

#HAVE  TO RUN CMDLINE AS ADMINISTRATOR
#Your anti virus might be a little pissed off


#change extension to pyw
# to set on launch we go to task scheduler
#create task on right
# Name WebsiteBlock configure for your setting
#CHECK OFF RUN WITH HIGHEST PRIVILEGES
#New Triggers At Startup
#Actions: start a program
#Click your file pyw
#Conditions ie on battery not on battery
