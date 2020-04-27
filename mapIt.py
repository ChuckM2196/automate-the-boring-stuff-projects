#!/usr/bin/python3
# mapIt.py Launches a map in the browser using an address from the cmd line or clipboard

# sys.argv reads information as inputted like a list
# ex sys.argv ['870', 'Valencia', 'St.']
import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line
    # 'mapIt.py ['870', 'Valencia', 'St.'] -> 870 Valencia St.
    address = ' '.join(sys.argv[1:]) # Joins list from the 1st index
else:
    # Get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

