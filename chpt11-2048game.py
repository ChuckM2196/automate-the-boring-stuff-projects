from selenium import webdriver
from selenium.webdriver.common.keys import Keys # allows keyboard presses
from selenium.webdriver.support.ui import WebDriverWait # waits until webpage has loaded before completing action
from selenium.webdriver.support import expected_conditions # expecting an alert to be present
from selenium.common.exceptions import TimeoutException # Timeout exception
from selenium.webdriver.common.by import By # How you locate elements

# Open url
def browserAccess():
    driver = webdriver.Firefox()
    driver.get('http://gabrielecirulli.github.io/')
    delay = 5   # seconds
    try:
        # Waits for webpage to load and element to be available else TimeoutException
        element_present = expected_conditions.presence_of_element_located((By.ID, 'html'))
        WebDriverWait(driver, delay).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
        driver.close()

    moves = driver.find_element_by_tag_name('html')
    while True:
        moves.send_keys(Keys.LEFT)
        moves.send_keys(Keys.UP)
        moves.send_keys(Keys.RIGHT)
        moves.send_keys(Keys.DOWN)


browserAccess()
