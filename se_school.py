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

    current_date = datetime.datetime.now()
    current_date_str = current_date.strftime(f'%m/%d/%y')
    end_date = datetime.datetime(2022, 12, 9)
    end_date_str = end_date.strftime(f'%m/%d/%y')

    print(f'\nCurrent date: {current_date_str}\n')
    print(f'End date: {end_date_str}i\n')

    time_left = str((end_date - current_date)).rsplit(',', 1)[0] # get the time that you have left (in days) to complete all lessons
    time_left_num = int(time_left.rsplit(' ', 1)[0])

    try: 
        lessons_per_day = int(input('\nHow many lessons do you plan to do each day?\n'))
        print('\n...\n')
    except:
        print('Enter a valid input (1,2, etc.)\n')
    
    lesson_num_sum = sum([subjDict[s] for s in subjDict if subjDict[s] >= 50]) # don't include subject lesson numbers < 50 in lesson number sum (e.g. lesson numbers for classes that haven't been started)
    
    lesson_num_avg = round((lesson_num_sum/(len(subjDict)-1)), 0)
    final_lesson_num = 170
    lessons_left = final_lesson_num - lesson_num_avg
    
    weekdays_left = round(((time_left_num/30) * 22), 0) # convert time_left (days left) to months and multiply by avg num of weekdays in a month (22) to obtain weekdays left
    weekends_left = round(((time_left_num - weekdays_left)/2), 0)
   
    proj_days_to_fin = round((lessons_left / lessons_per_day), 0) # the number of days it will currently take you to finish
 
    proj_finish_date = current_date + datetime.timedelta(days=(proj_days_to_fin + weekends_left)) 
    proj_finish_date_str = proj_finish_date.strftime(f'%m/%d/%y')
    
    print(f'''Your current average lesson number is {lesson_num_avg}\n
            You currently have {lessons_left} lessons to go.\n
            -----------------------------------------------------------------\n
            You have {time_left_num} days left to complete the school year...\n
            You have {weekdays_left} weekdays to complete the school year...\n
            There are {weekends_left} weekends left before the end of the school year...\n
            -----------------------------------------------------------------\n
            At your current rate ({lessons_per_day} lessons each weekday), it will take you {proj_days_to_fin} days to finish.\n 
            This means you will finish on {proj_finish_date_str}.\n\n''')

main()
