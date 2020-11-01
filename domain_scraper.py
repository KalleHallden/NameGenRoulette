from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ebird_api import get_bird_name 
import time

chrome_options = Options()  
# chrome_options.add_argument("--headless") 
browser = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://ph.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck='

domain_name = get_bird_name()

url = url + domain_name + ".com"

browser.get(url)
time.sleep(2)
available = browser.find_element_by_xpath('//*[@id="search-app"]/div/div/div[2]/div/div/div/div/div[2]/div[1]/div[1]/span').text

if available.split(' ')[-1] == 'available':
	print(domain_name + ".com" + " is available!")
else:
	print(domain_name + ".com" + " is taken!")