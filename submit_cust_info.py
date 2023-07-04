from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from faker import Faker

# Initialize Faker generator
fake = Faker()

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()
sleep_interval = 2
# Navigate to the web application
driver.get("http://localhost:5000")
time.sleep(sleep_interval)
# Find the form fields and submit button
cust_name = driver.find_element(By.NAME, "cust_name")
address = driver.find_element(By.NAME, "address")
contact_no = driver.find_element(By.NAME, "contact_no")
age = driver.find_element(By.NAME, "age")
gender = driver.find_element(By.NAME, "gender")
id_proof = driver.find_element(By.NAME, "id_proof")
submit_btn = driver.find_element(By.XPATH, "//input[@type='submit']")

# Fill in the form fields
cust_name.send_keys(fake.name())
address.send_keys(fake.address())
contact_no.send_keys(fake.phone_number())
age.send_keys(random.randint(18, 65))
gender.send_keys(random.choice(["Male", "Female"]))
id_proof.send_keys(fake.random_element(["SSN","Driver's License", "Passport"]))

time.sleep(sleep_interval)
# Click the submit button
submit_btn.click()

# Wait for a moment to see the result
driver.implicitly_wait(5)
time.sleep(sleep_interval)

# Close the browser
driver.quit()
