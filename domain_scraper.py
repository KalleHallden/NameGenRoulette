from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ebird_api import get_bird_names 
import time
from menu import print_menu
import random

chrome_options = Options()  
chrome_options.add_argument("--headless") 
browser = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://uk.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=domainnamehellothere.com'
name_list = get_bird_names()

while True:
	print("----------------------------------")
	print("SEARCHING...")
	print("----------------------------------")

	n = random.randint(0,len(name_list) -1)
	domain_name = name_list[n]

	url = 'https://uk.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck=' + domain_name + ".com"

	browser.get(url)
	time.sleep(2)
	available = ''
	try:
		available = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]').text
	except:
		pass
	available = available.split(' ')[1].split('\n')[0]
	print(available)
	if available == 'Available' or available ==  'Domain':
		print(domain_name + ".com" + " is available!")
		print_menu()
		user_input = input(": ").rstrip()
		while True:
			try: 
				user_input = int(user_input)
				break
			except:
				user_input = input(": ").rstrip()
				continue
		if user_input == 1:
			# implement stuff
			new_browser = webdriver.Chrome()
			new_browser.get(url)
			continue
		if user_input == 2:
			# implement stuff
			pass
		if user_input == 3:
			# implement stuff
			break
	else:
		print(domain_name + ".com" + " is taken!")
		continue