#! /usr/bin/env python
from selenium import webdriver
import time
import inspect

def lineno():
    return inspect.currentframe().f_back.f_lineno

class Browser():
    def __init__(self):
        self.driver = webdriver.Firefox()

    def enter_url(self, url):
        try:
            self.driver.get(url)
            time.sleep(4)
        except:
            print "ERROR : ", lineno()
            #driver.quit()
            #exit()
            return

    def search_item(self, search_string):
        #Identify Search Box
        search_box = self.driver.find_element_by_xpath("//input[@type='text'][@placeholder='Was suchen Sie?']")
        time.sleep(1)
        print "Current Syntax : ", self.driver.execute_script("return arguments[0].outerHTML", search_box)
        search_box.click()

        #Send Search Keys
        search_box.send_keys(search_string)
        search_button = self.driver.find_element_by_xpath("//input[@type='submit'][@id='gh-btn'][@value='Finden']")
        print "Current Syntax : ", self.driver.execute_script("return arguments[0].outerHTML", search_button)

        #Click Search Button
        search_button.click()
        time.sleep(2)

    def tearDown(self):
        print "done"
        self.driver.quit()

if __name__ == '__main__':
    browser = Browser()
    browser.enter_url("https://www.ebay.de/")
    browser.search_item("Tasatur")
    time.sleep(10)
