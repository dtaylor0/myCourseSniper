#!/usr/bin/env python
#webregBot.py - automatically registers you for sections on webreg when they open
import time,sys, credentials
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
def main():
    registerUrl='https://sims.rutgers.edu/webreg/editSchedule.htm?login=cas&semesterSelection=12019&indexList='
    if len(sys.argv)<2 or len(sys.argv)>11:
        print 'Error: wrong # of args, use format -> ./webregBot.py 01234 12345 23456'
        sys.exit()
    argvLength=len(sys.argv)
    i=1
    while i<argvLength:
        if i==argvLength-1:
            registerUrl+=sys.argv[i]
            break
        else:
            registerUrl+=sys.argv[i]+','
    browser=webdriver.Firefox()
    browser.get(registerUrl)
    usernameBox=browser.find_element_by_id('username')
    usernameBox.send_keys(credentials.login['username'])
    passwordBox=browser.find_element_by_id('password')
    passwordBox.send_keys(credentials.login['password'])
    submitButton=browser.find_element_by_name('submit')
    submitButton.click()

if __name__=='__main__':
    main()
