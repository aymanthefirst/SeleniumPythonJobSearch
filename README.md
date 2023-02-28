Job Search Automation with Selenium WebDriver
=============================================

This is a Python script for automating the job search process on the Totaljobs website. The script uses Selenium WebDriver to navigate through the website, search for job vacancies using the provided search parameters, and apply to the relevant vacancies.

Requirements
------------

-   Python 3.x
-   Selenium WebDriver for Chrome
-   Google Chrome browser

Usage
-----

1.  Install the required packages by running `pip install -r requirements.txt`.
2.  Replace the values for `email`, `password`, `job`, and `location` in the script with your own details.
3.  Run the script by running `python jobsearch.py` in your terminal.

How it works
------------

The script searches for job vacancies that match the provided search parameters and apply to the vacancies that meet specific criteria. It applies to jobs that:

-   Have not been applied to in the current session
-   Do not contain any of the keywords to avoid
-   Allow online applications

The script performs the following steps:

1.  Log in to the Totaljobs website using the provided credentials.
2.  Navigate to the search results page using the provided search parameters.
3.  Click on the first job listing and keep clicking the next job listing button until a new job is displayed.
4.  Check if the current job listing meets the criteria for application. If so, click the apply button and go back to the search results page.
5.  Repeat steps 3-4 until all relevant jobs have been applied to.

Note
----

This script is for educational purposes only. Do not use this script to apply to jobs in an automated manner without prior approval from the job provider. Also, use this script at your own risk as it may violate the terms of service of the job search website.
