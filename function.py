from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

from selenium.webdriver.common.by import By


def filter(chrome):
    print("filter")
    chrome.find_element(By.XPATH, "//*[@name='jobPosition']").click()
    chrome.find_element(By.CLASS_NAME, "dropdown-down").click()
    chrome.find_element(By.XPATH, "//*[contains(text(),'Hong Kong')]").click()
    chrome.find_element(By.XPATH, "//*[contains(text(),'Indonesia')]").click()
    chrome.find_element(By.XPATH, "//*[contains(text(),'Philippines')]").click()
    time.sleep(1)
    chrome.find_element(By.CLASS_NAME, "dropdown-up").click()
    chrome.find_elements(By.CLASS_NAME, "dropdown-down")[1].click()
    chrome.find_element(By.XPATH, "//*[contains(text(),'Finished Contract')]").click()
    time.sleep(1)
    chrome.find_elements(By.CLASS_NAME, "dropdown-up")[1].click()
    time.sleep(5)