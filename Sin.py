from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
browser = webdriver.Firefox(executable_path=r'/home/ylli/PYTHON/geckodriver')
browser.get("https://www.instagram.com")
email = WebDriverWait(browser, 1000000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')))
# browser.find_element_by_css_selector("div.-MzZI:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)").send_keys("mcnalbania@gmail.com")
password = WebDriverWait(browser, 1000000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#div.-MzZI:nth-child(3) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')))
email.send_keys("mcnalbania@gmail.com")
password.send_keys("yllcaka1516457")
password.submit()
# browser.find_element_by_css_selector("#div.-MzZI:nth-child(3) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)").send_keys("yllcaka1516457").submit()

# WebDriverWait(browser, 1000000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '._1frb'))).send_keys("sinan hoxha")
# # browser.find_element_by_css_selector("._1frb")
# browser.find_element_by_css_selector("._1frb").submit()
# # ActionChains(browser).
# WebDriverWait(browser, 1000000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#xt_uniq_1 > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)"))).click()
# # ActionChains(browser).move_to_element(browser.find_element_by_css_selector("#xt_uniq_1 > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)"))
# WebDriverWait(browser, 1000000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#u_0_3m > a:nth-child(1)'))).click()
# WebDriverWait(browser, 1000000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '._6iiu > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)')))
# ActionChains(browser).move_to_element(browser.find_element_by_css_selector("._6iiu > span:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")).perform()
# WebDriverWait(browser, 1000000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.span._iuw:nth-child(5)'))).click()