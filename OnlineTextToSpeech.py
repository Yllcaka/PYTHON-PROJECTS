#! /usr/bin/python3
from selenium import webdriver
import sys
browser = webdriver.Firefox()
browser.get("https://www.google.com/search?source=hp&ei=EPZ0XsmeCquVlwSk54qgAw&q=translate&oq=translate&gs_l=psy-ab.3..0i131j0l9.322.1245..1453...0.0..0.210.1229.0j7j1......0....1..gws-wiz.S9lZXZqULVM&ved=0ahUKEwjJ5oD9wqnoAhWryoUKHaSzAjQQ4dUDCAU&uact=5")
browser.find_element_by_id("tw-source-text-ta").clear()
try:
    browser.find_element_by_id("tw-source-text-ta").send_keys(sys.argv[1].capitalize())
except IndexError:
    browser.find_element_by_id("tw-source-text-ta").send_keys("When launching the program enter something for it to work")
browser.find_element_by_id("tw-src-spkr-button").click()