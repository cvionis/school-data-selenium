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

subjList = list(filter(None, subjList))

print(subjList)

lessNumList = []
for subject in subjList:
    lessNumStr = subject.rsplit(':', 1)[-1] # get string ('Lesson 00') following colon in each subject in subjList
    lessNum = lessNumStr.rsplit(' ', 1)[-1] # get number of lessNumStr
    lessNumList.append(lessNum)
    
print(lessNumList)



