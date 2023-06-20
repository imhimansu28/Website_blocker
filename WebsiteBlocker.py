import time
from datetime import datetime as dt

hosts_temp = "hosts.txt"
hosts_paths = r"c:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,
                                                                          23):
        print("Working Hours......")
        with open(hosts_paths, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write(f"{redirect} {website}" + "\n")
    else:
        with open(hosts_paths, 'r+') as file:
            content = file.readline()
            file.seek(0)
            for line in content:
                if all(website not in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(10)

