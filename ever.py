import time
from time import sleep
from random import randrange
import random
import os
import sys

def testing(driver,num):    
      print("run")     
      try:  

            try:
                  driver.refresh()              
                  driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
            except:
                  try:                                 
                        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
                  except:
                        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
      except:


            pass


 

      print("p1")

 
      try:                                
            sleep(2)                      
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
      except:
            driver.refresh()
            sleep(1)                      
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()

      sleep(2)
      alll=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']                          
     # driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(alll[random.randint(0,24)]+alll[random.randint(0,24)]+alll[random.randint(0,24)]+alll[random.randint(0,24)])
      try:                                 
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/input').send_keys(alll[random.randint(0,24)]+alll[random.randint(0,24)]+alll[random.randint(0,24)]+alll[random.randint(0,24)])
      except:
            sleep(1)                      
            try:                                 
                  driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/input').send_keys(alll[random.randint(0,24)]+alll[random.randint(0,24)]+alll[random.randint(0,24)]+alll[random.randint(0,24)])
            except:                             
                  driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(alll[random.randint(0,24)]+alll[random.randint(0,24)]+alll[random.randint(0,24)]+alll[random.randint(0,24)])
              
      print("p2")

      sleep(2)  
      try:
                             
            driver.find_elements_by_class_name("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[3]/button").click()
      except:           
            try:                           
                  sleep(1)                                          
                  el=driver.find_element_by_css_selector("._ab8w._ab94._ab97._ab9h._ab9k._ab9p._abb0").find_element_by_tag_name('button')
                  driver.execute_script("arguments[0].click();", el)
            except:                              
                  try:                               
                        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()                  
                  except:               
                        driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
                     
      print("p3")


#      sleep(2)                                   qF0y9          Igw0E   rBNOH          YBx95   ybXk5    _4EzTm                      soMvl                                                                                        
      try:
            try:                                 
                  driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/button').click()
            except:
                  driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/button').click()
      except:                             
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
      sleep(2)    
      try:                                
                                          
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys("hei")
      except:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys("ji")      



def testing2(driver):    
      print("run")     
      sleep(2)                 
      try:                               
            driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
      except:
            driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
      sleep(2) 
      try:                 
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
      except:
            pass
      sleep(2)         
      try:
            driver.find_element_by_xpath(' //*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
      except:
            driver.find_element_by_xpath(' //*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()

      sleep(2)
      sleep(2)                           
      alll=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']                          
     # driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(alll[random.randint(0,24)]+alll[random.randint(0,24)]+alll[random.randint(0,24)]+alll[random.randint(0,24)])
      try:
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(alll[random.randint(0,24)]+alll[random.randint(0,24)]+alll[random.randint(0,24)]+alll[random.randint(0,24)])
      except:
            sleep(1)
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(alll[random.randint(0,24)]+alll[random.randint(0,24)]+alll[random.randint(0,24)]+alll[random.randint(0,24)])
           


      sleep(2)  



      driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
      sleep(2)
      driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
      sleep(2)
      driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys('ffe')




