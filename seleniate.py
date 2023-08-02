#   ------------------------------------------- Selenium ----------------------------------------------    #

#   Used for UI testing and is a much powerful tool for webscraping
#   You will need webdrivers for different browsers
#   It is built-in for Safari so I am just gonna run with that for now.

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.keys import Keys

import time








def scrapedDataToDict(driver):
    #   Creating dictionaries to pass to database, files etc.
    shoeNames = driver.find_elements(By.CLASS_NAME, 'product-card__title')
    shoeCategories = driver.find_elements(By.CLASS_NAME, 'product-card__subtitle')
    shoeColours = driver.find_elements(By.CLASS_NAME, 'product-card__product-count')
    shoePrices = driver.find_elements(By.CLASS_NAME, 'product-price')
    shoeLinks = driver.find_elements(By.CLASS_NAME, 'product-card__link-overlay')
    myList=[]
    for index in range(len(shoePrices)):
        shoes = {
            "name": shoeNames[index].text,
            "category": shoeCategories[index].text,
            "colors": shoeColours[index].text,
            "price": shoePrices[index].text,
            "link": shoeLinks[index].get_attribute('href')
        }
        myList.append(shoes)
    return myList



def scrollToBottom(driver):
    #   This loop scrolls through the whole page to display all the elements. 
    while True:
        shoePrices = driver.find_elements(By.CLASS_NAME, 'product-price')
        
        if(len(shoePrices) >= 103):
            testnum = len(shoePrices)
            break
        
        # Scroll down the page by sending "END" key to the body element
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)  # Wait for a short time to let the page load




def initializeDriver(link):
    driver = webdriver.safari.webdriver.WebDriver()
    driver.get(link)
    return driver


def main():
    link = "https://www.nike.com/ca/w/football-shoes-1gdj0zy7ok"
    driver = initializeDriver(link)
    scrollToBottom(driver)
    shoeList = scrapedDataToDict(driver)
    print(shoeList)
    print(len(shoeList))

if __name__ == "__main__":
    main()
    
    



#   So far, I am still getting 24 shoes once again, so I will have to run some
#   commands to Selenium to scroll down the whole page to uncover all the shoe
#   elements first and then I will print out all the shoes.

#   New update: I have figured it out, it does print out all of them
#   The new code is now scrolling through the page to load all the shoes
#   and the loop creates a dictionary with the shoes.


time.sleep(16)


 