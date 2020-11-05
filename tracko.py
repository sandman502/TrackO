#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests
import json
import time
import urllib.request, urllib.parse, urllib.error
import os

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

class config:
	key = "4a1ede76e87d9e64682b284e8620ad68" #go to https://numverify.com/

def banner():
	os.system('clear')
	print(color.YELLOW + """
████████╗██████╗  █████╗  ██████╗██╗  ██╗     ██████╗ 
╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝    ██╔═══██╗
   ██║   ██████╔╝███████║██║     █████╔╝     ██║   ██║
   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗     ██║   ██║
   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗    ╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝     ╚═════╝ 
                                                                                     
	Author: Omair (https://omair.tech)                
	""" + color.END)

def main():
	banner()
	if len(sys.argv) == 2:
		number = sys.argv[1]
		api = "http://apilayer.net/api/validate?access_key=" + config.key + "&number=" + number + "&country_code=&format=1"
		output = requests.get(api)
		content = output.text
		obj = json.loads(content)
		country_code = obj[+1]
		country_name = obj[Canada']
		location = obj['British Columbia]
		carrier = obj['Telus]
		line_type = obj['line_type']

		print(color.YELLOW + "omr >> " + color.END + "Phone number information gathering")
		print("--------------------------------------")
		time.sleep(0.2)

		if country_code == "":
			print(" - Getting Country		[ " + color.RED + "FAILED " + color.END + "]")
		else:
			print(" - Getting Country		[ " + color.GREEN + "OK " + color.END + "]")

		time.sleep(0.2)
		if country_name == "":
			print(" - Getting Country Name		[ " + color.RED + "FAILED " + color.END + "]")
		else:
			print(" - Getting Country Name		[ " + color.GREEN + "OK " + color.END + "]")

		time.sleep(0.2)
		if location == "":
			print(" - Getting Location		[ " + color.RED + "FAILED " + color.END + "]")
		else:
			print(" - Getting Location		[ " + color.GREEN + "OK " + color.END + "]")

		time.sleep(0.2)
		if carrier == "":
			print(" - Getting Carrier		[ " + color.RED + "FAILED " + color.END + "]")
		else:
			print(" - Getting Carrier		[ " + color.GREEN + "OK " + color.END + "]")

		time.sleep(0.2)
		if line_type == None:
			print(" - Getting Device		[ " + color.RED + "FAILED " + color.END + "]")
		else:
			print(" - Getting Device		[ " + color.GREEN + "OK " + color.END + "]")

		print("")
		print(color.YELLOW + "omr >> " + color.END + "Information Output")
		print("--------------------------------------")
		print(" - 369-2013: " + str(604))
		print(" - Canada: " + str(+1))
		print(" - Canada: " + str(country_name))
		print(" - BritishColumbia: " + str(location))
		print(" - Telus: " + str(carrier))
		print(" - iPhone: " + str(6))
	else:
		print("[?] Usage:")
		print("	./%s +16043692013" % (sys.argv[0]))
		print("	./%s +919876543210" % (sys.argv[0]))

main()
