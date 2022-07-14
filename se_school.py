from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time
import datetime

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
subjDict = {}

for subj in subjList:
    subjName = subj.rsplit(':',1)[0]
    lessNumStr = subj.rsplit(':', 1)[-1] # get string ('Lesson 00') following colon in each subject in subjList
    lessNum = int(lessNumStr.rsplit(' ', 1)[-1]) # get number of lessNumStr
    subjDict[subjName] = lessNum # create new dict entry for each subject with subjName as key and lessNum as value

print(subjDict)

# Need to: Calculate, according to current subject lessons, what current end date is if you do a given number of lessons per day each week day





# Calculate how many subjects and/or lessons (subjects/num of subjects) must be done each day/week in order to finish by end date 
