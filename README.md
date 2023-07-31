# nike.com-webscrape | Nike Football Shoe Extractor

This repository contains my learning progress of webscraping in Python. So far, I have worked with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Selenium](https://selenium-python.readthedocs.io/). I decided to solve the problem of extracting shoe information directly from the Nike Canada site. 

Number of hours in: 1 hour of BeautifulSoup and 4 hours of Selenium.

My takeaways so far are: 
1.  [<ins>BeautifulSoup</ins>] is a very simple webscraping library that cannot handle JavaScript as it is useful to extract the HTML source code.
2.  The problem I faced with BeautifulSoup was that out of the 103 shoes that were displayed on the website, I found that only <ins>24</ins> shoes were being displayed, the rest is only displayed once the user scrolls through the page.
3.  This problem was easily solved with <ins>Selenium</ins> because it allows testing the website's UI through automation of interactions. So, I called in a scroll method to keep scrolling until all the shoes were loaded in the page. (103 shoes)
4.  Once all the shoes were visible on the website, I used the WebDriver to extract the visible shoe details from that page into a dictionary. 

My goals for this learning experience is:
1.  With the links to the shoes or by using Selenium to click on the shoes, find available sizes.
2.  Further cleaning and organizing webdata by sorting by price, name, size availability etc using [Pandas](https://pandas.pydata.org/docs/).

