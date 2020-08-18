from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
from selenium import webdriver
from selenium.webdriver.common.by import By
from CreateProxyExtensionHelper import *

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#web driver selenium
driver_path =r"C:\Users\shailendra bisht\Downloads\chromedriver"
driver = webdriver.Chrome(driver_path)

url_main = 'https://www.appbrain.com/apps/country-india/finance/'

driver.get(url_main)
# No of applications on the link
no_of_apps = len(driver.find_elements(By.CLASS_NAME,'browse-app-large'))

print(no_of_apps)

list = []
list1 = []
dictionary = {}

for tag in range(no_of_apps) :
    driver.get(url_main)
    driver.find_elements(By.CLASS_NAME,'browse-app-large')[tag].click()

    url_html = driver.current_url
    html = urlopen(url_html, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    features = soup.find_all( 'div', class_= ['infotile-text','infotile-subtext', 'infotile-bottom'])
    #print(features)
    app_name = soup.find('h1').text

    list = []
    # All the features of an app is in list
    list.append('separator')
    list.append(app_name)

    for feature in features :
        list.append(feature.text)

    dictionary['name'] = list[1]

    if '\nDownloads\n' in list :
        a = list.index("\nDownloads\n")
        dictionary['Downloads'] = list[a-2] + list[a-1]

    if '\nRating\n' in list : #@11
        a = list.index("\nRating\n")
        dictionary['Rating'] = list[a-2] + list[a-1]

    if '\nRanking\n' in list : #@14
        a = list.index("\nRanking\n")
        dictionary['Ranking'] = list[a-2] + list[a-1]

    if '\nLibraries\n' in list : #@16
        a = list.index("\nLibraries\n")
        dictionary['Libraries'] = list[a-1]

    if '\nAndroid version\n' in list : #@18
        a = list.index("\nAndroid version\n")
        dictionary['Android version'] = list[a-1]

    if '\nLast updated\n' in list : #@20
        a = list.index("\nLast updated\n")
        dictionary['Last updated'] = list[a-1]

    if '\nApp age\n' in list : #@23
        a = list.index("\nApp age\n")
        dictionary['App age'] = list[a-2] + list[a-1]

    if '\nApp size\n' in list : #@25
        a = list.index("\nApp size\n")
        dictionary['App size'] = list[a-1]

    if '\nPrice\n' in list : #@29
        a = list.index("\nPrice\n")
        dictionary['Price'] = list[a-1]

    for key in dictionary :
        print(key,dictionary[key])


    #print(dictionary['name'])
