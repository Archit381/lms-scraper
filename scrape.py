from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://lms.bennett.edu.in")
details={"Course Name":[],
     "Course Tenure":[],
     "Course Progress":[],
     "Assignment Due": [],
     "Due Date": []
     }

username= driver.find_element(By.ID, "username")
username.send_keys("e21cseu0428")

password= driver.find_element(By.ID, "password")
password.send_keys("8Sm&5Xl&")

login= driver.find_element(By.ID, "loginbtn")
login.click()
time.sleep(5)

filter=driver.find_element(By.ID, "displaydropdown")
filter.click()
time.sleep(2)

list_filter=driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div[2]/div/div/section/div/aside/section[1]/div/div/div[1]/div[1]/div[4]/ul/li[2]/a")
list_filter.click()
time.sleep(2)

courses = driver.find_elements(By.CSS_SELECTOR, "div.col-md-9.d-flex.flex-column")
progress = driver.find_elements(By.CSS_SELECTOR, "div.text-muted.muted.d-flex.flex-wrap.mt-auto")
# timeline=driver.find_elements(By.CSS_SELECTOR, "div.container-fluid p-0")
timeline=driver.find_elements(By.CSS_SELECTOR, '[data-region="event-list-content-date"]')
timeline2=driver.find_elements(By.CSS_SELECTOR, "div.text-truncate.line-height-3.media-body")
timeline3=driver.find_elements(By.CSS_SELECTOR, "ul.media-list")

for i in courses:
    crsname=i.find_element(By.CSS_SELECTOR, "a.aalink.coursename").text
    crstenure=i.find_element(By.CSS_SELECTOR, "span.categoryname").text
    details["Course Name"].append(crsname) 
    details["Course Tenure"].append(crstenure)


for j in progress:
    crsprogress=j.find_element(By.CSS_SELECTOR, "div.progress-text").text
    details["Course Progress"].append(crsprogress)


# print(details)
for i in timeline:
     due_date=i.find_element(By.CSS_SELECTOR, 'h5.h6.d-inline.font-weight-bold.px-2').text
     c=0
     for j in timeline3:
        assign_name=i.find_element(By.CSS_SELECTOR, "small.text-muted.text-truncate").text
        details["Assignment Due"].append(assign_name)
        c=c+1
     
     for k in c:
        details["Due Date"].append(due_date)

# for i in timeline2:
#     assign_name=i.find_element(By.CSS_SELECTOR, "small.text-muted.text-truncate").text
#     details["Assignment Due"].append(assign_name)


print(details)