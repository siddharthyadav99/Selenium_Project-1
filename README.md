# Web Scraping Project: Job Data Collection Using Python and Selenium

This project is a comprehensive **web Scraping Script** built using **Python** and **Selenium** to extract job listings from a popular job portal in the UK. The tool automates the process of gathering job-related information, providing a robust solution for data collection and analysis.

## Features

- **Automated Job Search**: Navigate through job search results and pages dynamically, simulating user actions to retrieve relevant data.
- **Data Extraction**: Scrapes key job details, including:
  - **Job Title**: The title or designation of the job position.
  - **Company Name**: The organization offering the job.
  - **Location**: Where the job is based, including city or region.
  - **Salary**: The salary range or details (if provided).
  - **Job Description**: A summary of the role's responsibilities and requirements.
- **Pagination Handling**: Automatically iterates through multiple pages of search results to collect comprehensive data.
- **CSV Export**: Saves the scraped data into a structured CSV file for easy analysis and storage.

## Tools & Technologies

- **Selenium**: Used for automating browser interactions and simulating user actions.
- **Python**: The core programming language for scripting the web scraping logic and handling data.
- **Pandas**: For organizing and exporting the scraped data into a CSV file.

## Use Cases

- **Job Market Analysis**: Gather insights into trends in job titles, salaries, and skills across industries.
- **Personal Job Search**: Streamline your search for specific roles and locations by collecting data in bulk.
- **HR & Recruitment**: Monitor competitor job postings or industry hiring trends.

## How It Works

1. **Setup WebDriver**: The Selenium WebDriver is configured to control a Chrome browser instance.
2. **Login Automation**: The tool logs in to the job portal with user-provided credentials.
3. **Dynamic Job Search**: Users specify job roles and locations to target specific opportunities.
4. **Data Scraping**: The script navigates search results, clicks on individual job links, and extracts details from job postings.
5. **Data Export**: The collected data is organized into a DataFrame and exported as a CSV file.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver (compatible with your Chrome browser version)
- Pandas

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git

2. Install dependencies:
   ```pip install selenium pandas```

3. Download ChromeDriver and update the script with the path to the driver executable.

## Usage
1. Update the script with your LinkedIn login credentials.
2. Specify the job title and location you want to search for in the script.
3. Run the script:
   In Case if you want to provide Number of Pages to be Scrapped:
   ```bash
   python JobsiteUK_Scraping.py
   ```

   In case if you want to Scrape completely
   ```bash
   python JobsiteUK_Scraping2.py
   ```
      
5. The results will be saved as a CSV file in the same directory as the script.
