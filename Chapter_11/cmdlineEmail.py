#! /usr/bin/python3
#cmdlineEmail.py - takes a command line input of an email address and string of text then opens a web browser, logs in, and sends email to email address. 

import requests, os, bs4, webbrowser
from selenium import webdriver

#TODO: Get input from command line

#TODO: grab email address from command line
#TODO: Get message 
#TODO: Open webbeowser

#naigate to email account homepage
browser = webdriver.Firefox()   #Open firefox browser
browser.get('https://gmail.com')    #navigate to Gmail

#Log in to my account
emailElem = browser.find_element_by_id('identifierId') #Select the usename field
emailElem.send_keys('promethian.industries@gmail.com')  #input email address
linkElem = browser.find_element_by_class_name('VfPpkd-RLmnJb')
linkElem.click()                                    #submit email address
passwordElem = browser.find_element_by_name('password')  #Select the password field
passwordElem.send_keys('j16MQVaJhBXw')
linkElem = browser.find_element_by_class_name('VfPpkd-RLmnJb')
linkElem.click() 

#TODO: Start new message
emailElem = browser.find_element_by_name('Compose')
emailElem.click()


#TODO: Fill in recipient email address


#TODO: Paste messge

#TODO: Send email

#TODO: Close browser


