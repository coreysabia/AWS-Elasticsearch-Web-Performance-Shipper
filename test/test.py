import datetime as dt
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import config
from seleniumDataShipper import SeleniumDataShipper

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This file is currently under development.

def main():

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)

    webpage = "https://www.google.com"

    print("Loading: ", webpage)
    print()
    driver.get(webpage)
    data = driver.execute_script("return window.performance.timing.toJSON();")
    print("Collecting data:", data)
    print()
    print("Closing driver.")
    driver.quit()



if __name__ == "__main__":
    main()