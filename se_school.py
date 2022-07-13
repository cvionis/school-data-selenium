from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time

driverPath = os.path.abspath('chromedriver')
driver = webdriver.Chrome(driverPath)
driver.get('https://academy.abeka.com/Video2/Streaming/Default.aspx?cs=y')

