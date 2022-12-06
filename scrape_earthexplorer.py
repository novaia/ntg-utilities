from bs4 import BeautifulSoup
from csv import writer
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://earthexplorer.usgs.gov/')