#!/usr/bin/python3
# Image site downloader- auto searches photo sharing site for category and automatically downloads 100 images
from selenium import webdriver
from selenium.common.exceptions import TimeoutException  # Timeout exception
from selenium.webdriver.support.ui import WebDriverWait  # waits until webpage has loaded before completing action
import bs4
import requests
import os
import wget

def imageSearch():
    # Saves topic search to variable
    topic = input("What topic would you like to search:")
    topic.lstrip()
    topic.rstrip()
    return topic


def browserAccess(option):
    # Opens webpage and searches for topic
    option = saved_topic
    driver = webdriver.Firefox()
    driver.get('https://imgur.com/')
    delay = 5 # 5 seconds

    try:
        # Searches for topic suggested
        WebDriverWait(driver, delay)
        element = driver.find_element_by_css_selector('.Searchbar-textInput')
        element.send_keys(saved_topic)
        element.submit()
        saved = "https://imgur.com/search?q=" + saved_topic
        return saved
    except TimeoutException:
        print("Page took too long to load")
        driver.close()


def imageSourceFinder(url):
    # Parses webpage for top 100 images related to search topic and stores in a list
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    images = []
    i = 1
    for image in soup.findAll('img'):
            if i <= 100:
                images.append(image.get('src'))
                i = i + 1
    return images


def imageDownloader(links):
    # Loop through each link and download to current directory
    if len(links) == 0:
        print('We were unable to find any links associated with the search topic. Please rerun the program trying a different search topic')
        quit()
    else:
        cwd = os.getcwd()
        for link in links:
            link.rstrip()
            new_link = 'https:' + link
            print(str(new_link))
            wget.download(new_link, cwd)
            quit()


saved_topic = imageSearch()
newurl = browserAccess(option=saved_topic)
image_links = imageSourceFinder(url=newurl)
imageDownloader(links=image_links)
