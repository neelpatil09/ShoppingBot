#!/usr/bin/env pypy
import time
import os
import sys
start_time = time.time()
from config import keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('chromedriver')
def op(xpathString):
    isAvail = False
    while isAvail == False:
        try:
            driver.find_element_by_xpath(xpathString).click()
            isAvail = True
        except NoSuchElementException:
            print("no")
            isAvail = False

def order(k):
    driver.get(k['bestbuy_product_url'])
    driver.maximize_window()
    #add to cart
    isAvail = False
    while isAvail == False:
        try:
            driver.execute_script("window.scrollTo(0, 500)")
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="fulfillment-add-to-cart-button-61bcfa7a-a6a0-4ab2-8e03-99722922e07a"]/div/div/div/button').click()
            isAvail = True
        except NoSuchElementException:
            time.sleep(3)
            isAvail = False
            driver.refresh()
    time.sleep(2.5)
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])

    driver.find_element_by_class_name('go-to-cart-button').click()

    driver.switch_to_default_content()
    """#go to cart
    op('//*[@id="shop-attach-modal-72251603-modal"]/div/div[1]/div/div/div/div/div[1]/div[3]/a')
    """
    #checkout
    op('//*[@id="cartApp"]/div[2]/div[1]/div/div/span/div/div[2]/div[1]/section[2]/div/div/div[3]/div[1]/div[1]/button')

    #guest continue
    op('/html/body/div[1]/div/section/main/div[4]/div/div[2]/button')
    
    #fills fields out
    isAvail = False
    while isAvail == False:
        try:
            driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.firstName"]').send_keys(k['firstname'])
            isAvail = True
        except NoSuchElementException:
            isAvail = False
    
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.lastName"]').send_keys(k['lastname'])
    
    driver.find_element_by_xpath('//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[1]/div/div/section/div[2]/div[1]/section/section/div[3]/label/div[2]/div/button').click()
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.street"]').send_keys(k['address'])
    
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.city"]').send_keys(k['city'])
    stateSelect = Select(driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.state"]'))
    stateSelect.select_by_visible_text(k['bestbuy_state'])
    driver.find_element_by_xpath('//*[@id="consolidatedAddresses.ui_address_2.zipcode"]').send_keys(k['zip'])
    driver.find_element_by_xpath('//*[@id="user.phone"]').send_keys(k['phone'])
    driver.find_element_by_xpath('//*[@id="user.emailAddress"]').send_keys(k['email'])
    
    driver.find_element_by_xpath('//*[@id="checkoutApp"]/div[2]/div[1]/div[1]/main/div[2]/div[2]/form/section/div/div[2]/div/div/button').click()
    
    #credit card NEEDS UNAVAIL 
    isAvail = False
    while isAvail == False:
        try:
            driver.find_element_by_xpath('//*[@id="optimized-cc-card-number"]').send_keys(k['cardnum'])
            isAvail = True
        except NoSuchElementException:
            isAvail = False
    
    expiryMonth = Select(driver.find_element_by_xpath('//*[@id="credit-card-expiration-month"]/div/div/select'))
    expiryMonth.select_by_visible_text(k['month'])
    expiryYear = Select(driver.find_element_by_xpath('//*[@id="credit-card-expiration-year"]/div/div/select'))
    year = "20"+k['year']
    expiryYear.select_by_visible_text(year)
    
    driver.find_element_by_xpath('//*[@id="credit-card-cvv"]').send_keys(k['cvv'])
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("--- %s seconds ---" % (time.time() - start_time))
    while(True):
        pass
order(keys)