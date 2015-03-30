import re
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

"""
// Flipkart toll free number//
print("called in test file!!!!!!!!!!!!!!!")
redditFile = urlopen("https://www.flipkart.com/s/contact")
redditHtml = redditFile.read()
redditFile.close()
soup = BeautifulSoup(redditHtml)
redditAll = soup.find_all("p", class_="bmargin10 fk-font-14")
for links in redditAll:
    print("Flipkart Toll-free Number:",links.text)
"""


"""
//Airtel MH Circle Contact number//
print("called in test file!!!!!!!!!!!!!!!")
redditFile = urlopen("http://www.airtel.in/mobile/prepaid/reach-airtel/mobile-customersupport/?CIRCLE=11&CIRCLENAME=Maharashtra%20and%20Goa")
redditHtml = redditFile.read()
redditFile.close()
soup = BeautifulSoup(redditHtml)
redditAll = soup.find_all("span", class_="arial11red")
for links in redditAll:
    print("Airtel Contact Number:",links.text)

"""

"""
//Hcl Customer Care Number//
print("called in test file!!!!!!!!!!!!!!!")
redditFile = urlopen("http://www.touchservicesupport.com/contact")
redditHtml = redditFile.read()
redditFile.close()
soup = BeautifulSoup(redditHtml)
redditAll = soup.find_all("div", class_="topnumber")
for links in redditAll:
    print("HCL Contact Number:",links.text)

"""

print("called in test file!!!!!!!!!!!!!!!")
redditFile = urlopen("https://www.sony.co.in/section/contactus")
redditHtml = redditFile.read()
redditFile.close()
soup = BeautifulSoup(redditHtml)
'''redditAll = soup.find_all("div", class_="right contactUsRightCol BodyText")'''
redditAll = soup.select("#CategoryLanding > div.right.contactUsRightCol > div:nth-child(1) > p:nth-child(4)")
for links in redditAll:
    print("Sony Contact Number:",links.text)
