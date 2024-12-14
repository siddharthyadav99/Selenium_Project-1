from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Set up WebDriver
s = Service("D:/VS Code/web scraping/Selenium/chromedriver-win64 (1)/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://www.jobsite.co.uk/")
driver.maximize_window()
time.sleep(2)

# Accept Cookies
try:
    cookie = driver.find_element(By.XPATH, "/html/body/div[4]/section/div/section/div[2]/div[1]/div[2]/div")
    cookie.click()
    time.sleep(2)
except Exception as e:
    print("Cookie banner not found or already dismissed.", e)

# Enter job title
jobtitle = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/div/div/div/div/div[1]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/input")
jobtitle.send_keys("Software Engineer")
time.sleep(2)

# Enter location
city = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/div/div/div/div/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/input")
city.send_keys("London")
time.sleep(2)

# Click search
search = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div/div/div/div/div/div/div[1]/div[2]/button/span/span")
search.click()
time.sleep(3)

# Initialize lists for data
job_titles = []
company_name = []
net_salary = []
locations = []
job_description = []

# Scrape data until the last page
while True:
    # Collect job data from the current page
    job_elements = driver.find_elements(By.XPATH, "//h2[contains(@class, 'res-1tassqi')]/a")
    for job in job_elements[:25]:  # Limit to the first 25 elements on each page
        job_titles.append(job.text.strip() if job.text.strip() else "N/A")

    companies = driver.find_elements(By.XPATH, "//span[contains(@class, 'res-17gmubg')]/span")
    for company in companies:
        company_name.append(company.text.strip() if company.text.strip() else "N/A")

    salaries = driver.find_elements(By.XPATH, "//span[contains(@class,'res-c0o836')]/span")
    for salary in salaries:
        net_salary.append(salary.text.strip() if salary.text.strip() else "N/A")

    location = driver.find_elements(By.XPATH, "//div[contains(@class, 'res-qchjmw')]//span[@class='res-c0o836']")
    for area in location:
        locations.append(area.text.strip() if area.text.strip() else "N/A")

    descriptions = driver.find_elements(By.XPATH, "//div[contains(@class, 'res-1fiv1iy')]/div")
    for description in descriptions:
        job_description.append(description.text.strip() if description.text.strip() else "N/A")

    # Pagination: Click the "Next" button to go to the next page
    try:
        # Find the "Next" button
        next_button = driver.find_element(By.XPATH, '//a[@aria-label="Next"]')
        if next_button.is_enabled():  # Ensure the button is enabled
            next_button.click()  # Click the "Next" button
            time.sleep(3)  # Wait for the next page to load
        else:
            print("Next button is disabled, no more pages.")
            break  # Stop if the next button is not available
    except Exception as e:
        print(f"Error finding the 'Next' button: {e}")
        break  # Stop if there is an issue with finding the 'Next' button

# Ensure all lists are of equal length (fill missing values with 'N/A')
max_length = max(len(job_titles), len(company_name), len(net_salary), len(locations), len(job_description))
job_titles.extend(["N/A"] * (max_length - len(job_titles)))
company_name.extend(["N/A"] * (max_length - len(company_name)))
net_salary.extend(["N/A"] * (max_length - len(net_salary)))
locations.extend(["N/A"] * (max_length - len(locations)))
job_description.extend(["N/A"] * (max_length - len(job_description)))

# Create DataFrame
data = {
    "Job Title": job_titles,
    "Company Name": company_name,
    "Salary": net_salary,
    "Location": locations,
    "Job Description": job_description
}
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("scraped_jobs.csv", index=False)

print("Data has been saved to scraped_jobs.csv")

# Keep the browser open
print("Scraping complete. Browser will remain open.")
