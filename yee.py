  
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time 

def Chottomatte():
    browser =  webdriver.Chrome('chromedriver.exe')
    browser.get("https://www.bootcampdemy.com/content/734-%E0%B8%9A%E0%B8%97%E0%B8%99%E0%B9%8D%E0%B8%B2-%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%A7%E0%B8%B1%E0%B8%94-%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%84%E0%B8%A5%E0%B8%B2%E0%B8%94%E0%B9%80%E0%B8%84%E0%B8%A5%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%99-%E0%B9%80%E0%B8%A7%E0%B8%81%E0%B9%80%E0%B8%95%E0%B8%AD%E0%B8%A3%E0%B9%8C-1")
    login = browser.find_element_by_css_selector("a.nav-link.nav-login-btn")
    
    #time.sleep(5)

    
    login.click()
    username = browser.find_element_by_name("email").send_keys("s46081@debsirin.ac.th")
    password = browser.find_element_by_name("password").send_keys("s46081")
    click = browser.find_elements_by_css_selector("button.btn-brand.btn.btn-wide.m-t-20")
    click[0].click()

    
    #profile = browser.find_element_by_class_name('round')
    #logout  = browser.find_element_by_partial_link_text('https://checkin.debsirin.online/authentication-module/logout.php')
    # profile.click()
    # logout.click()
    time.sleep(3)
    browser.close()
i = 0
while i < 10: 
    Chottomatte()
    i = i + 1 