from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time

driverPath = os.path.abspath('chromedriver')
driver = webdriver.Chrome(driverPath)
driver.get('https://academy.abeka.com/Video2/Streaming/Default.aspx?cs=y')

driver.implicitly_wait(20)

lessonsGroup = driver.find_element(By.ID, 'dvLessonsToday')

subjList = []
subjects = lessonsGroup.find_elements(By.CLASS_NAME, 'dailyLesson')

for s in subjects:
    subjList.append(s.text.replace('\n',':'))

print(subjList)

lessNumList = []
for subject in subjList:
    lessNum = subject.rsplit(':', 1)[-1]
    lessNumList.append(lessNum)

print(lessNumList)



