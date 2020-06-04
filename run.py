#!/usr/bin/python3

import requests
import socket
from colorama import init
from termcolor import colored
import os
init()

logo=(
"""
	▁ ▂ ▄ ▅ ▆ ▇ █   🎀 【﻿ ＡｌｔＳｕｂ 】 🎀   █ ▇ ▆ ▅ ▄ ▂ ▁
			   	
	linkedin -	https://www.linkedin.com/in/jimmisimon/	
	Site	 -	http://jimmisimon.in/projects.php

"""
)
print(logo)


def main():
	print(colored('File Should Not Contain http:// or https:// ','white','on_red'))
	fname = input("Enter file name : ")

	if os.path.exists(fname) == True:
		with open(fname, 'r') as f:
			str1 = "http"
			str2 = "https"
			if str1 in f.read():
				print(colored("File Have [ http:// ] or [ https:// ] remove that and try again",'white','on_red'))
			elif str2 in f.read():
				print(colored("File Have [ https:// ] or [ https:// ] remove that and try again",'white','on_red'))
			
			else:
				method = input("Enter The Method You Want to search http/https : ") 
				num_lines = 0
				with open(fname, 'r') as f:
				    for line in f:
				        num_lines += 1
				total_counts=num_lines
				with open(fname) as f:
				    content = f.readlines()    
				content = [x.strip() for x in content]
				print("")
				print('{:<40} {:<10} {:<20} {:<20}'.format("Host_Address","Status","Server","IP_Address"))
				print('{:<40} {:<10} {:<20} {:<20}'.format("------------","------","------","----------"))
				if method == str1:
					for i in range(total_counts):
						try:
							ip = socket.gethostbyname(content[i])
							url = "http://"+content[i]
							req = requests.get(url)
							code = req.status_code
							server = req.headers['server']
							if req:
								print(colored('{:<40} {:<10} {:<20} {:<20}'.format(url,code,server,ip),'green'))
							else:
								print(colored('{:<40} {:<10} {:<20} {:<20}'.format(url,code,server,ip),'yellow'))
						except:

							continue
					print(colored("Completed Happy Hunting....",'white'))	
				elif method == str2:
					for i in range(total_counts):
						try:
							ip = socket.gethostbyname(content[i])
							url = "https://"+content[i]
							req = requests.get(url)
							code = req.status_code
							server = req.headers['server']
							if req:
								print(colored('{:<40} {:<10} {:<20} {:<20}'.format(url,code,server,ip),'green'))
							else:
								print(colored('{:<40} {:<10} {:<20} {:<20}'.format(url,code,server,ip),'yellow'))
						except:

							continue
					print(colored("Completed Happy Hunting....",'white'))		
				else:
					print("Enter Correct Option")
	else:
		print("File Not Found")

if __name__== "__main__":
   main()
