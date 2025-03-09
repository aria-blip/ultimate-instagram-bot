import time
from time import sleep
from random import randrange
import random


def testing(driver):    
      print("run")     
      sleep(2)                                                    
      driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
      sleep(2)                      
      driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
      sleep(2)    
      driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
      sleep(2)
      sleep(2)                           
      alll=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']                          
      driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(alll[random.randint(0,len(alll))]+alll[random.randint(0,len(alll))]+alll[random.randint(0,len(alll))]+alll[random.randint(0,len(alll))])
      sleep(2)                            
      driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
      sleep(2)
      driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
      sleep(2)
      driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys("hei")
      sleep(1)
