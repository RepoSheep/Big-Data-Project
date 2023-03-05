"""
performing web scraping using selenium and pandas
"""

#import libraries
import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys
# import logging

# set up logging


# Print out the libraies version
print("Selenium version: {}".format(selenium.__version__))
print(f"python version: {sys.version.split(' ')[0]}")

# Create empty DataFrame to store the data.
columns = [
    'title',
    'company_name',
    'location',
    'employment_type',
    'level',
    'category',
    'min_experience',
    'salary_min',
    'salary_max',
    'job_description'
]
# ['title','company_name', 'location', 'employment_type', 'level', 'category', 'min_experience','salary_min', 'salary_max', 'job_description']

jobs = pd.DataFrame(columns=columns)

#start the selenium webdriver
driver = webdriver.Chrome()

#search for data analyst jobs
job_keyword = 'data analyst' 

count = -1
#loop first 2 pages only
for page in range(2): 
    driver.get(f'https://www.mycareersfuture.sg/search?search={job_keyword}&sortBy=new_posting_date&page={page}')
    assert 'MyCareersFuture' in driver.title #check if the page is loaded with MyCareersFuture
    sleep(6)
    #loop for first 2 jobs entries only
    for i in range(2):
        print("\n current page: {} \n job number:{}".format(page, i))
        # Extract job title using xpath
        title_elem = "//div[@class='card-list']/div[{}]/div/a/div[1]/div/section/div[2]/div/span".format(i+1)
        title = driver.find_element("xpath",title_elem).text
        company_element = "//div[@class='card-list']/div[{}]/div/a/div[1]/div/section/div[2]/p".format(i+1)
        company_name = driver.find_element('xpath',company_element).text
        print(company_name)
        # print(title)

        # Click in job details.
        # loc_elem = "//div[@class='card-list']/div[{}]/div/a/div[1]/div/section/div[2]/div[2]/section/p[1]".format(i+1)
        driver.find_element("xpath",title_elem).click()
        sleep(5)

        # Extract other detail job information.
        employment_type = driver.find_element(By.ID, 'employment_type').text
        location = driver.find_element(By.ID, 'address').text
        level = driver.find_element(By.ID, 'seniority').text
        category = driver.find_element(By.ID, 'job-categories').text
        min_experience = driver.find_element(By.ID, 'min_experience').text
        job_description = driver.find_element(By.ID, 'job_description').text

        try:
            salary_min = driver.find_element(By.XPATH, "//div[@class='lh-solid']/span[1]").text
            salary_max = driver.find_element(By.XPATH, "//div[@class='lh-solid']/span[2]").text[2:]
        except:
            salary_min = None
            salary_max = None

        print(title)
        print(company_name)
        print(location)
        print(employment_type)
        print(level)
        print(category)
        print(job_description)
        print(min_experience)
        print(salary_min)
        print(salary_max)
        # print(job_description)      
        
        count += 1
        jobs.loc[count] = [title, company_name, location, employment_type, level, category, min_experience,salary_min, salary_max, job_description]
        print(jobs)
        driver.back()
        sleep(3)


# Save the data to csv file.
jobs.to_csv(f'{job_keyword}.csv', index=False)
driver.close()