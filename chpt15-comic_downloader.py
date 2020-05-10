#!/usr/bin/python3
# Web Comic Downloader- Automatically checks the websites of several comics and automatically downloads the images
                        # if the comic was updated since the program last run
                        # Downloads comics from https://www.exocomics.com


import os, wget, bs4, requests,

# Checks if comic folder exists, creates if not
def folder_check():
    try:
        cdir = os.getcwd()
        if 'comics' not in os.listdir():
            os.makedirs('comics')
            os.chdir('comics')
        else:
            os.chdir('comics')
    except OSError:
        print("Directory or Permissions issue")
        exit()

# check if last url was saved to file if saved load into variable
def saved_url():
    p_url = os.path.exists('last_downloaded.txt')
    if p_url == False:
        print("No previous comics have been downloaded")
    else:
        print("Found previous url")
        f = open('last_downloaded.txt', 'r')
        p_url = f.read()
        print(p_url)
        return p_url

# Web scrapes for the latest url
def comic_download():
    url = 'https://www.exocomics.com/'
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    for href_tag in soup.find_all(href=True, class_='ir last'):
        new_url = href_tag.get('href')
        return new_url

# Compares urls, and downloads ones that do not match
def url_compare_and_download(prevurl,newurl):
    # Checks if urls match, and skips if they match run in a while loop
    cwd = os.getcwd()
    while newurl != prevurl:
        res = requests.get(newurl)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        for href_comic in soup.findAll(class_='image-style-main-comic'):
            comic = href_comic.get('src')
        # Downlods comics that dont match, goes back one comic set to newurl
            wget.download(comic,cwd)
            ls = os.listdir(os.getcwd())
            print(ls)
        for prev_comic in soup.findAll(class_='ir prev'):
            newurl = prev_comic.get('href')
            print(newurl)
            break

    # If URLs match, saves url to last_downloaded.txt
    if newurl == prevurl:
        last_downloaded = open('last_downloaded.txt', 'w')
        last_downloaded.write(newurl)
        last_downloaded.close()
        f = open('last_downloaded.txt', 'r')
        last_comic = f.read()
        print(last_comic)
        f.close()

    # If webpage doesn't have a previous link, goes to last comic and saves to last_downloaded.txt, this to prevent
    # redownloading old webcomics

    else:
        # new URL will equal first webcomic url, needs to go to last comic to save to last_downloaded.txt
        res = requests.get('https://www.exocomics.com/01')
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        for href_tag in soup.find_all(href=True, class_='ir last'):
            latest_url = href_tag.get('href')
            f = open('last_downloaded.txt', 'w')
            f.write(latest_url)
            f.close()


# Calling Functions
folder_check()
old_saved = saved_url()
new_saved = comic_download()
url_compare_and_download(prevurl=old_saved,newurl=new_saved)