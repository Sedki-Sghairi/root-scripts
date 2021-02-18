import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

jokes = ["love you <#","big kiss mmmmmuah"]

options = Options()
options.add_argument("--user-data-dir=chrome-data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe', options=options)
driver.maximize_window()
driver.get('https://web.whatsapp.com')  # Already authenticated

time.sleep(20)

##################### Provide Recepient Name Here ###############################
driver.find_element_by_xpath("//*[@title='Amelie Beaulne']").click()

for joke in jokes:
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(joke)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span').click()
    time.sleep(2)

time.sleep(30)
driver.close()