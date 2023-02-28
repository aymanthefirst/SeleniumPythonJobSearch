from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

email = "***********"
password = "********"
job = "Java developer"
location = "London"
KEYWORDS_TO_AVOID = ["*****", "*****", "********"]

currentJobId = ""
previousJobId = ""
previousPreviousJobId = ""
originalURL = 'https://www.totaljobs.com/jobs/' + job + '/in-' + location + '?radius=30&salary=30000&salarytypeid=1&Sort=3'
currentURL = originalURL
pageNumber = 1

def doLogin():
    driver.get("https://www.totaljobs.com/account/signin")
    driver.find_element_by_id('Form_Email').send_keys(email)
    driver.find_element_by_id('Form_Password').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
    print("successfully logged in!!")

def getBodyText():
    return driver.find_element_by_tag_name('body').text

def getOrangeButtonText():
    orangeButtonText = driver.find_element_by_id('top-button-panel').text
    print(orangeButtonText)
    return orangeButtonText

def getSalaryText():
    return driver.find_element_by_xpath('/html/body/div[3]/div[5]/div[1]/div[1]/div/div/div[1]/div/div/div[1]/section/ul[1]/li[2]/div').text

def getJobId():
    return driver.find_element_by_class_name('brand-font').text

def clickFirstJob():
    driver.find_element_by_tag_name('h2').click()
    print("clicked first job")

def navigateToNextPage():
    print("Navigating to next page")
    global pageNumber
    pageNumber = pageNumber + 1
    currentURL = originalURL + "&page=" + str(pageNumber)
    driver.get(currentURL);

def clickNextJobTillNewJobAppears():
    print(getJobId() + " == " + currentJobId)
    print(getJobId() + " == " + previousJobId)
    while (getJobId() == currentJobId) or (getJobId() == previousJobId) or (getJobId() == previousPreviousJobId):
        clickNextJob()

def clickNextJob():
        driver.find_element_by_id('nextJobButton').click()
        print("Next job has been clicked")

def checkForKeyWords():
    print('checking keywords')
    return any(x not in getBodyText() for x in KEYWORDS_TO_AVOID)

def updateCurrentURL():
    global currentURL
    currentURL = driver.current_url
    print("url has been updated")


def clickApply():
    driver.find_element_by_xpath('//*[@id="JobToolsTop_AOLOptions_lnkApplyOnline"]').click()
    print('apply clicked')

def clickSendApplication():
    driver.find_element_by_xpath('//*[@id="top-button-panel"]/section/div[2]/div[2]/div/div[1]/a').click()
    print('send application clicked')


def goBackPage():
    driver.execute_script("window.history.go(-1)")
    print('go back page')

def closeAllTabsButOne():
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
        print('tab closed')

driver.implicitly_wait(30)
doLogin()
driver.get(currentURL)
clickFirstJob()
clickNextJobTillNewJobAppears()
for x in range(1000):
    previousPreviousJobId = previousJobId
    previousJobId = currentJobId
    currentJobId = getJobId()
    try:
        if "You applied for this job today" in getBodyText():
            print("already applied for this job")
            clickNextJobTillNewJobAppears()
        else:
            if checkForKeyWords():
                if "Send application" in getOrangeButtonText():
                    print('send application is in body')
                    clickSendApplication()
                    goBackPage()
                elif "Apply" in getOrangeButtonText():
                    print('Apply is in body')
                    clickApply()
                    goBackPage()
        closeAllTabsButOne()
        clickNextJobTillNewJobAppears()
    except Exception as e:
        print(e)
        driver.get(currentURL)
        navigateToNextPage()
        updateCurrentURL()
        clickFirstJob()
