from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#web driver selenium
driver_path =r"C:\Users\shailendra bisht\Downloads\chromedriver"
driver = webdriver.Chrome(driver_path)

url_main = 'https://www.appbrain.com/apps/country-india/finance/'

driver.get(url_main)
no_of_apps = len(driver.find_elements(By.CLASS_NAME,'browse-app-large'))

print(no_of_apps)

for tag in range(no_of_apps) :
    driver.get(url_main)
    driver.find_elements(By.CLASS_NAME,'browse-app-large')[tag].click()

    url_html = driver.current_url
    html = urlopen(url_html, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    features = soup.find_all( 'div', class_= ['infotile-text','infotile-subtext'])
    #print(features)
    for feature in features :
        print(feature.text)

#html_first = urlopen(url_main, context=ctx)
#soup_first = BeautifulSoup(html_first, "html.parser")
#
#app1 = driver.find_element_by_class_name('vmargin-s')
#app1.click()

#Traverse in 20 pages


# Scrape data from application inside page

	#url = input('Enter - ')
	#html = urlopen(url, context=ctx).read()
	#soup = BeautifulSoup(html, "html.parser")

	#tag = soup('div')
	#tags = soup.find_all( 'div', {'class': 'infotile-text'})
	#soup.findAll('div', class_=['A', 'B'])


#app_switch(url_main)
