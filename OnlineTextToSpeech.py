#! /usr/bin/python3
from selenium import webdriver
import sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Firefox(executable_path=r'/home/ylli/PYTHON/geckodriver')
browser.get("https://www.google.com/search?source=hp&ei=EPZ0XsmeCquVlwSk54qgAw&q=translate&oq=translate&gs_l=psy-ab.3..0i131j0l9.322.1245..1453...0.0..0.210.1229.0j7j1......0....1..gws-wiz.S9lZXZqULVM&ved=0ahUKEwjJ5oD9wqnoAhWryoUKHaSzAjQQ4dUDCAU&uact=5")
browser.find_element_by_id("tw-source-text-ta").clear()
try:
    browser.find_element_by_id("tw-source-text-ta").send_keys(" ".join(sys.argv[1:]).capitalize())
except IndexError:
    browser.find_element_by_id("tw-source-text-ta").send_keys("When launching the program enter something for it to work")
WebDriverWait(browser, 1000000).until(EC.element_to_be_clickable((By.ID, 'tw-src-spkr-button'))).click()
enter = input("Do you wanna enter anything else? ").upper()
if enter.startswith("Y"):
    while enter != "exit":
        enter = input("What do you want to write (enter: 'exit' to end)")
        if enter == "clear":
            browser.find_element_by_id("tw-source-text-ta").clear()
        else:
            browser.find_element_by_id("tw-source-text-ta").send_keys(
                enter)
            WebDriverWait(browser , 1000000).until(EC.element_to_be_clickable((By.ID , 'tw-src-spkr-button'))).click()
