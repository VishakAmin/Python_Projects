import time
from datetime import datetime as dt

host_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
website_list =["www.facebook.com","facebook.com"]
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 5):
        print("Working Hours.......")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            print(content)
            for web in website_list:
                if web in content:
                    pass
                else:
                    file.write(redirect+" "+web+"\n")

    else:
        with open(hosts_path, 'r+') as file:
            content= file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

            file.truncate()
        print("No")
    time.sleep(5)