from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome()

driver.get('https://www.ulife.com.br/login.aspx')
sleep(1)
login_info = 'your_ra'
sleep(1)
pass_info = 'your_password'
sleep(1)
field_login = driver.find_element_by_id('txtLogin')
sleep(1)
field_password = driver.find_element_by_id('txtPassword')
sleep(1)

field_login.send_keys(login_info)
sleep(1)
field_password.send_keys(pass_info)
sleep(1)

button_login= driver.find_element_by_id('imbLogin')
sleep(1)

button_login.click()
sleep(2)

driver.find_element_by_xpath('//*[@id="studentCalendar"]/div/div[3]/div/ul/li[2]/ul/li/a').click()

sleep(3)

driver.find_element_by_xpath('//*[@id="conpass-tag"]/div/div[2]/div[1]').click()

driver.quit()