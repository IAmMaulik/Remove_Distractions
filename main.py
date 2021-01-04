import time
import platform
from datetime import datetime as dt

# Checking Wheteher the computer is Windows Mac Or Linux
if 'windows' in platform.system().lower():
    hosts_path = "C:\\Windows\\System32\\drivers\\etc"
else:
    hosts_path = "/etc/hosts"

redirect_ip = "127.0.0.1"

website_list = []

# Taking input of the working hours
print("Enter the hour time in 24hr clock ONLY. Example: 8 or 16")
start_time = int(input("Enter the time you start working: "))
end_time = int(input("Enter the time you end working: "))

# Taking Input of websites
print("Enter the names of the website that you want to block. Write STOP to end")
while True:
    a = input("Enter the url: ")
    if a.lower() == 'stop':
        break
    else:
        if 'www.' in a:
            website_list.append(a)
            a = a.replace('www.', '')
            website_list.append(a)
        else:
            website_list.append(a)
            a = 'www.' + a
            website_list.append(a)

# Main Loop of the program
while True:
    if (dt(dt.now().year, dt.now().month, dt.now().day, start_time) < dt.now()) and (dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_time)):
        print("Working Hours...")
    else:
        print("Fun Hours...")
    time.sleep(6)
