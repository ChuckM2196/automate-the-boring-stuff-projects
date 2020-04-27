# Program opens all text files in a folder
# Matches user supplied regular expression
# Prints results to the screen

import re
import os


# Inputs keyword to search
def search_keyword():
    keyWord = input("input a keyword to search")
    return keyWord


# Loop that searches current directory for .txt files and stores them in a list
def file_search():
    fileNames = os.listdir(os.getcwd())
    filePaths = []
    for file in fileNames:
        # Splits file into two parts in a list. checks end of list
        ext = os.path.splitext(file)[-1].lower()
        if ext == '.txt':
            # Stores all txt files in a list and returns list.
            filePaths.append(os.path.abspath(file))
    return filePaths

# searches each text file and prints results to the screen
def text_search(keyword,dir_files):
    # run though each file in list finding all keywords and print to screen
    for textfile in storedFiles:
        open(textfile, 'r')
        print(re.findall(r'\w+',keyword))

# Execute functions
searchText = search_keyword()
storedFiles = file_search()
text_search(keyword=searchText,dir_files=storedFiles)

