import time
from datetime import datetime as dt

#Using the r formatter to avoid python thinking we are using special keywords
#Or I could use \\
#THIS is for WINDOWS on mac and linux is it is different
hosts_temp = r"C:\Users\Bryce\Desktop\website-blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list=["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 23):
        print("working hours")
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


## TODO:
# Can we detect their os systems -1
# Can we grab the websites from a textput inbox
# Can we grab times they want the sites blocked from a textinput
