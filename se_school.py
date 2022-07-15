from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time
import datetime

def main():
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

    # Need to: Calculate, according to current subject lessons, what projected finish date is if you do a given number of lessons per day each week day (and days you have left to finish)

    current_date = datetime.datetime.now()
    current_date_str = current_date.strftime(f'%m/%d/%y')
    end_date = datetime.datetime(2022, 12, 9)
    end_date_str = end_date.strftime(f'%m/%d/%y')

    print(f'Current date: {current_date_str}')
    print(f'End date: {end_date_str}')

    time_left = str((end_date - current_date)).rsplit(',', 1)[0] # get the time that you have left (in days) to complete all lessons
    time_left_num = int(time_left.rsplit(' ', 1)[0])
    time_left_msg = (f'You have {time_left} to finish the school year') 
    print(time_left_msg)

    try: 
        lessons_per_day = int(input('\nHow many lessons do you plan to do each day?\n'))
        print('...\n')
    except:
        print('Enter a valid input (1,2, etc.)\n')
    
    lesson_num_sum = 0
    for s in subjDict:
        if s != 'American Government': # don't take second semester course that hasn't been started into consideration
            lesson_num_sum += subjDict[s]

    lesson_num_avg = lesson_num_sum/len(subjDict)
    final_lesson_num = 170
    lessons_left = final_lesson_num - lesson_num_avg
    
    # Use weekdays_left to allow the user to enter a desired finish date, and output number of lessons per day that must be completed in order to finish by then
    # Calculations are probably incorrect; need to incorporate weekdays_left to get correct result
    weekdays_left = (time_left_num/30) * 22 # convert time_left (days left) to months and multiply by avg num of weekdays in a month (22) to obtain weekdays left
    
    proj_days_to_fin = lessons_left / lessons_per_day

    proj_finish_date = current_date + datetime.timedelta(days=proj_days_to_fin)
    proj_finish_date_str = proj_finish_date.strftime(f'%m/%d/%y')
    
    print(f'If you complete {lessons_per_day} lessons every week day, you will have completed all lessons by {proj_finish_date_str}') 
    


main()

    # Calculate how many subjects and/or lessons (subjects/num of subjects) must be done each day/week in order to finish by end date 
