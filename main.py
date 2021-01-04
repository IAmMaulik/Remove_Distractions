import platform

if 'windows' in platform.system().lower():
    hosts_path = "C:\\Windows\\System32\\drivers\\etc"
else:
    hosts_path = "/etc/hosts"

redirect_ip = "127.0.0.1"

website_list = []

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
