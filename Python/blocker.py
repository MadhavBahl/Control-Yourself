import json
import time
from datetime import datetime as dt
import platform

# Dynamically allotting host_file_path according to the Operating System
host_file_path=''
if platform.system()=='Linux':
    host_file_path= '/etc/hosts'
elif platform.system()=='Windows':
    host_file_path= 'C:\Windows\System32\drivers\etc\hosts'
else:
    print('Caution: Error while detecting the platform.')
    print('\tDetected Platform was',platform.system())

redirect_path = "127.0.0.1"
websites = json.load(open("data/websites.json"))

# To make the script running all the time
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 18) < dt.now() <  dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Time to block website!")
        # Open the hosts file
        with open(host_file_path, 'r+') as file:
            # Read the content and print it out on the terminal
            content = file.read()
            print(content)
            for website in websites:
                if website in content:
                    pass
                else:
                    file.write (redirect_path + " " + website + "\n")
    else:
        with open (host_file_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
        print("Websites are unblocked!")
    time.sleep(10)