from datetime import datetime as dt
import time

hosts = r"C:\Windows\System32\drivers\etc\hosts"
#hosts_temp=r"D:\Python\website_blocker\hosts"
redirect = '127.0.0.1'
website_list=["www.facebook.com","facebook.com"]

while True : 
	if dt.now().hour > 8 and dt.now().hour < 17:
		print("Working hours")
		with open(hosts,'r+') as h:
			content = h.read()
			for web in website_list:
				if web in content:
					pass
				else:
					h.write(redirect+" "+web+"\n")
					
	else:
		print("Fun Hours")
		with open(hosts,'r+') as h:
			content = h.readlines()
			h.seek(0)
			for line in content:
				if not any(website in line for website in website_list):
					h.write(line)
			h.truncate()
	time.sleep(5)
						
			