import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

from seleniumwire import webdriver  # Import from seleniumwire

#time libraries to add wait times
from time import sleep

#add options functionality
chrome_options = Options()
#disable notifications
chrome_options.add_argument("--disable-notifications")
#Make webdriver invisible to user
#chrome_options.add_argument("--headless=new")

def get_professor_names(class_code):
    #initialize webdriver
    driver = webdriver.Chrome(options=chrome_options)
    # Set the interceptor on the driver
    #driver.request_interceptor = interceptor
    driver.get('https://nubanner.neu.edu/StudentRegistrationSsb/ssb/term/termSelection?mode=search') #Go to Banner
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, 'select2-chosen-1'))).click() #Click on the dropdown
    sleep(1)
    term_search = (driver.find_element(By.XPATH, '//input[@type="text"][@sanitize="true"]')) #click on search box for semester
    term_search.send_keys('Spring 2024 Semester') #type in semester search term
    sleep(1.5)
    term_search.send_keys(Keys.TAB) #Enter the Search Term
    driver.find_element(By.ID, 'term-go').click() #Click on the search button for the semester
    #sleep(100)
    subject_box = (WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="text"][@sanitize="true"]')))) #Click on subject box
    subjects = {'cs':'Computer Science', 'ds':'Data Science', 'cy':'Cybersecurity'}
    subject_box.send_keys(subjects[class_code[0:2].lower()]) #Enter the appropriate subject based on the course code
    sleep(1.5)
    subject_box.send_keys(Keys.ENTER)
    course_number = driver.find_element(By.ID, 'txt_courseNumber') #Find the box for the course number
    course_number.send_keys(class_code[2:]) #Enter the code
    driver.find_element(By.ID, 'search-go').click() #Hit Search

    names = set()
    while True:
        name_elements = []
        sleep(1)
        name_elements = (WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, '//a[@class="email"]'))))
        print(len(name_elements))
        for element in name_elements:
            print(element.text)
            names.add(element.text)
        try:
            driver.find_element(By.XPATH, '//button[@title="Next"][@disabled="disabled"]').click()
            break
        except:
            driver.find_element(By.XPATH, '//button[@title="Next"]').click()
    print(names)
    driver.quit()
    return names

# get_professor_names('cs2510')
