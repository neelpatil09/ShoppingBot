#!/usr/bin/env pypy
import time
import os
import sys
import urllib3
start_time = time.time()
from config import keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('chromedriver')
def op(xpathString):
    isAvail = False
    while isAvail == False:
        try:
            driver.find_element_by_xpath(xpathString).click()
            isAvail = True
        except NoSuchElementException:
            isAvail = False

def order(k):
    driver.get(k['walmart_product_url'])
    driver.maximize_window()
    #add to cart
    isAvail = False

    while isAvail == False:
        try:
            driver.find_element_by_xpath('//*[@id="add-on-atc-container"]/div[1]/section/div[1]/div[3]/button/span/span').click()
            isAvail = True
        except NoSuchElementException:
            time.sleep(3)
            ans = input("Y/N?")
            if ans == "Y":
                continue
            else:
                driver.refresh()
                isAvail = False

    #check out
    op('//*[@id="cart-root-container-content-skip"]/div[1]/div/div[2]/div/div/div/div/div[3]/div/div/div[2]/div[1]/div[2]/div/button[1]')
    
    #continue w/o account
    op('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[1]/div/div/div/div/div[3]/div/div[1]/div/section/section/div/button/span')

    #delivery option NEEDS REPEATING IF UNAVAIL
    op('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[2]/div/div[2]/div/div/div/div[3]/div/div/div[2]/button/span')
    
    #fills fields out
    isAvail = False
    while isAvail == False:
        try:
            driver.find_element_by_xpath('//*[@id="firstName"]').send_keys(k['firstname'])
            isAvail = True
        except NoSuchElementException:
            isAvail = False
    
    driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(k['lastname'])
    driver.find_element_by_xpath('//*[@id="phone"]').send_keys(k['phone'])
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(k['email'])
    driver.find_element_by_xpath('//*[@id="addressLineOne"]').send_keys(k['address'])
    driver.find_element_by_xpath('//*[@id="city"]').clear()
    driver.find_element_by_xpath('//*[@id="city"]').send_keys(k['city'])
    stateSelect = Select(driver.find_element_by_xpath('//*[@id="state"]'))
    stateSelect.select_by_visible_text(k['state'])
    driver.find_element_by_xpath('//*[@id="postalCode"]').clear()
    driver.find_element_by_xpath('//*[@id="postalCode"]').send_keys(k['zip'])
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div/form/div[2]/div[2]/button/span').click()
    
    #credit card NEEDS UNAVAIL 
    isAvail = False
    while isAvail == False:
        try:
            driver.find_element_by_id('creditCard').send_keys(k['cardnum'])
            isAvail = True
        except NoSuchElementException:
            isAvail = False
    
    expiryMonth = Select(driver.find_element_by_xpath('//*[@id="month-chooser"]'))
    expiryMonth.select_by_visible_text(k['month'])
    expiryYear = Select(driver.find_element_by_xpath('//*[@id="year-chooser"]'))
    expiryYear.select_by_visible_text(k['year'])
    driver.find_element_by_xpath('//*[@id="cvv"]').send_keys(k['cvv'])
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[3]/div/div/div/div[4]/div[1]/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[2]/div/div/div/form/div[3]/div/button/span').click()
    exectime = "--- %s seconds ---" % (time.time() - start_time)
    print(exectime)

    while(True):
        pass
order(keys)
