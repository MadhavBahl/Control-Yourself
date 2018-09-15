import time
from datetime import datetime as dt

host_file_path = "/etc/hosts"
redirect_path = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com", "twitter.com", "www.twitter.com"]

# To make the script running all the time
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 18) < dt.now() <  dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working Hours")
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
        print("Fun hours")
    time.sleep(5)