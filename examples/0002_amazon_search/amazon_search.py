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
            time.sleep(2)
        except:
            print "ERROR : ", lineno()
            #driver.quit()
            #exit()
            return

    def locate_search_box(self):
        #Identify Search Box
        try:
            self.search_box = self.driver.find_element_by_xpath("//input[@type='text'][@id='twotabsearchtextbox'][@class='nav-input']")
            time.sleep(1)
            print "Current Syntax : ", self.driver.execute_script("return arguments[0].outerHTML", self.search_box)
        except:
            print "ERROR : ", lineno()
            #driver.quit()
            #exit()
            return

        try:
            self.search_box.click()
        except:
            print "ERROR : ", lineno()
            #driver.quit()
            #exit()
            return

    def enter_search_string(self, search_string):
        #Send Search Keys
        try:
            self.search_box.send_keys(search_string)
        except:
            print "ERROR : ", lineno()
            #driver.quit()
            #exit()
            return

    def locate_search_button(self):
        try:
            self.search_button = self.driver.find_element_by_xpath("//input[@type='submit'][@class='nav-input']")
            print "Current Syntax : ", self.driver.execute_script("return arguments[0].outerHTML", self.search_button)
        except:
            print "ERROR : ", lineno()
            #driver.quit()
            #exit()
            return

    def click_search_button(self):
        try:
            #Click Search Button
            self.search_button.click()
            time.sleep(2)
        except:
            print "ERROR : ", lineno()
            #driver.quit()
            #exit()
            return


    def tearDown(self):
        print "done"
        self.driver.quit()

if __name__ == '__main__':
    browser = Browser()
    browser.enter_url("https://www.amazon.de/")
    browser.locate_search_box()
    browser.enter_search_string("Tasatur")
    browser.locate_search_button()
    browser.click_search_button()
    time.sleep(4)
