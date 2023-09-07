from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

@app.route('/get_course_details', methods=['POST'])
def get_course_details():
    try:
        # Get the username and password from the request JSON
        data = request.get_json()
        username = data['username']
        password = data['password']

        # Selenium code to log in and retrieve course details
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://lms.bennett.edu.in")

        # Fill in the username and password fields
        username_elem = driver.find_element(By.ID, "username")
        username_elem.send_keys(username)

        password_elem = driver.find_element(By.ID, "password")
        password_elem.send_keys(password)

        login_elem = driver.find_element(By.ID, "loginbtn")
        login_elem.click()

        time.sleep(5)

        # Scrape course details
        courses = driver.find_elements(By.CSS_SELECTOR, "div.col-md-9.d-flex.flex-column")
        progress = driver.find_elements(By.CSS_SELECTOR, "div.text-muted.muted.d-flex.flex-wrap.mt-auto")

        course_details = {
            "Course Name": [],
            "Course Tenure": [],
            "Course Progress": []
        }

        for i in courses:
            crsname = i.find_element(By.CSS_SELECTOR, "a.aalink.coursename").text
            crstenure = i.find_element(By.CSS_SELECTOR, "span.categoryname").text
            course_details["Course Name"].append(crsname)
            course_details["Course Tenure"].append(crstenure)

        for j in progress:
            crsprogress = j.find_element(By.CSS_SELECTOR, "div.progress-text").text
            course_details["Course Progress"].append(crsprogress)

        # Close the WebDriver
        driver.quit()

        return jsonify(course_details)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
