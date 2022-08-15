#!/usr/bin/env pypy
import time
import os
import sys
start_time = time.time()
from config import keys
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('chromedriver')
def op(xpathString):
    isAvail = False
    while isAvail == False:
        try:
            driver.find_element_by_xpath(xpathString).click()
            isAvail = True
        except:
            print("failed")
            isAvail = False

def order(k):
    driver.get(k['gamestop_product_url'])
    driver.maximize_window()
    #add to cart
    isAvail = False
    while isAvail == False:
        try:
            driver.find_element_by_xpath('//*[@id="primary-details"]/div[4]/div[13]/div[3]/div/div[1]/button').click()
            isAvail = True
        except NoSuchElementException:
            time.sleep(3)
            reloadOrNot = input("Do you have to complete a captcha? Y for Yes or any key for No")
            if reloadOrNot == "Y":
                break
            else:
                print("fail one")
                driver.refresh()
                isAvail = False
    time.sleep(0.5)
    #go to cart
    op('//*[@id="addedToCartModal"]/div/div/div[2]/div[2]/a')
    
    #proceed to checkout
    op('/html/body/div[6]/div[6]/div[1]/div[2]/div[5]/div[2]/div/a')
    
    #continue w/o account
    op('//*[@id="ae-main-content"]/div[2]/div[3]/div/a')
    
    #fills fields out
    
    isAvail = False
    while isAvail == False:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            #driver.find_element_by_xpath('//*[@id="ae-main-content"]/div/div').click()
            driver.find_element_by_id('shipping-email').send_keys(k['email'])
            isAvail = True
        except NoSuchElementException:
            isAvail = False
    
    driver.find_element_by_xpath('//*[@id="shippingFirstName"]').send_keys(k['firstname'])
    driver.find_element_by_xpath('//*[@id="shippingLastName"]').send_keys(k['lastname'])
    driver.find_element_by_xpath('//*[@id="shippingAddressOne"]').send_keys(k['address'])
    driver.find_element_by_xpath('//*[@id="city"]').clear()
    driver.find_element_by_xpath('//*[@id="shippingAddressCity"]').send_keys(k['city'])
    stateSelect = Select(driver.find_element_by_xpath('//*[@id="shippingState"]'))
    stateSelect.select_by_visible_text(k['state'])
    driver.find_element_by_xpath('//*[@id="shippingZipCode"]').clear()
    driver.find_element_by_xpath('//*[@id="shippingZipCode"]').send_keys(k['zip'])
    driver.find_element_by_xpath('//*[@id="shippingPhoneNumber"]').send_keys(k['phone'])
    driver.find_element_by_xpath('//*[@id="checkout-main"]/div[2]/div/div/div/button[1]').click()
    
    #credit card NEEDS UNAVAIL 
    isAvail = False
    while isAvail == False:
        try:
            driver.find_element_by_xpath('//*[@id="cardNumber"]').send_keys(k['cardnum'])
            isAvail = True
        except NoSuchElementException:
            isAvail = False
    
    expiryMonth = Select(driver.find_element_by_xpath('//*[@id="expirationMonth"]'))
    expiryMonth.select_by_visible_text(k['month'])
    expiryYear = Select(driver.find_element_by_xpath('//*[@id="expirationYear"]'))
    year = "20"+k['year']
    expiryYear.select_by_visible_text(year)
    driver.find_element_by_xpath('//*[@id="securityCode"]').send_keys(k['cvv'])
    driver.find_element_by_xpath('//*[@id="checkout-main"]/div[1]/div[1]/div[7]/div/div/div/div[11]/button[2]').click()
    print("--- %s seconds ---" % (time.time() - start_time))
    while(True):
        pass
order(keys)