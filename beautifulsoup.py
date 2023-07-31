#   ------------------------------ Introduction to Web Scraping --------------------------------    #
#   We will be covering the following: beautifulsoup, selenium, scrapy, puppeteer
#   We will be using the same link for the following projects. After we cover all the topics,
#   I will be testing other webpages as well. 

#   -------------------------------------- Beautiful Soup --------------------------------------    #

from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    
}

url = "https://www.nike.com/ca/w/football-shoes-1gdj0zy7ok"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')
#print(soup.prettify())
#print(soup.get_text())
A = soup.prettify()
#print(A[0].get_text())
#print(A[1].get_text())

#   These two lines will create html source file of the webpage being scraped above (comment out)

with open("soup-nike.html", "w") as file:
    file.write(str(A))


#   Find classes like this, these 4 lines are looking for the following div classes containing shoe data
shoeNames = soup.find_all("div", {"class": "product-card__title"})
shoeCategories = soup.find_all("div", {"class": "product-card__subtitle"})
shoeColours = soup.find_all("div", {"class":"product-card__product-count"})
shoePrices = soup.find_all("div", {"class": "product-price"})

#   To store all the shoe data being scraped from the HTML source page
shoeList = []

for index in range(len(shoeNames)):
    
    shoes = {
        "name": shoeNames[index].get_text(),
        "category": shoeCategories[index].get_text(),
        "colors": shoeColours[index].get_text(),
        "price": shoePrices[index].get_text()
    }
    shoeList.append(shoes)

#   Printing dict that can now be used with Pandas and stored to NoSQL databases 
print(json.dumps(shoeList, indent=4))
#   Prints 24 shoes because the rest is shown through JavaScript functions (I think)
print(len(shoeList))
    
#   Find tags like this 
# mydivs = soup.find_all("div")
    

#   Progress Report: After learning and researching BeautifulSoup for an hour, it has come to my attention
#   that it has limitations. In this example, I can only get the first 24 shoes from the above link whereas
#   there are more than 100 in that website. I believe, the other shoes are rendered once the user scrolls.

#   So we will now learn Selenium which apparently is much stronger as it can kind of mimic user interaction
#   when it comes to web scraping, like it scrapes the site like a user which is actually kinda cool. 






    
