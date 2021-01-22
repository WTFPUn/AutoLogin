from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time 
url = input("paste your url : ")
def Chottomatte(usernamess2,urls):
    browser =  webdriver.Chrome('chromedriver.exe')
    browser.get(urls)
    username = browser.find_element_by_id('user-name')
    password = browser.find_element_by_id('user-password')
    submit = browser.find_element_by_name('submit')

    username.send_keys(usernamess2)
    password.send_keys(f'Debsirin{usernamess2}')
    submit.click()

    profile = browser.find_element_by_class_name('round')
    #logout  = browser.find_element_by_partial_link_text('https://checkin.debsirin.online/authentication-module/logout.php')
    # profile.click()
    # logout.click()
    time.sleep(3)
    
    browser.close()
user = ['46048','46068','46357','46013','46020','46036','46012','46060','46218','46081','46216','46053','46025','46041','46064','46061']
for i in user:
    Chottomatte(i,url)