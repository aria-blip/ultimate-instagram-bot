from selenium import webdriver
import os
import time
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions


import ever

class InstagrammBot:
    def __init__(self,username,password,nameofig):
        """
            ARGS:
                username=username of instagramm
                password=password of the iser name in instagramm
            Attributes:
                driver=that wich controlls chrome action
            BotMethods:
                login:to login into instagramm


        """
        self.username=username
        self.password=password
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(20)
        self.namessss="aria"
        self.login()
        self.nameofig=nameofig
        self.version="5"

    
    def login(self):

        self.driver.get('https://www.instagram.com/accounts/login/') 
        sleep(1)                            
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button[1]').click()
        sleep(2)
        sleep(1)                                    
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        button=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        sleep(1)
        button.click()   

    def message_followers(self):
        try:
          #  self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        #    self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
            ever.mainn(self.driver,self.nameofig,self.version)


        except:
            self.driver.quit()
            
    def _get_following(self):     

        sleep(3)
        #following=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/div/a')

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        #following.click()//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[4]5/a 5
        sleep(3)                                    
        followingb= self.driver.find_element_by_xpath('/html/body/div['+self.version+']/div/div/div[2]')
        scroll = 0                                     
        last_ht,ht=0,1
        sleep(5)
        while last_ht!=ht:
            last_ht=ht                                                                                                                                 
            
            sleep(4)
            self.driver.execute_script("""arguments[0].scrollTo(0,967);
            return arguments[0].scrollHeight;""",followingb)
            sleep(3)
            self.driver.execute_script("""arguments[0].scrollTo(0,967);
            return arguments[0].scrollHeight;""",followingb)
           
        links=followingb.find_elements_by_tag_name('a')
        names=[name.text for name in links if name.text !=''] 
        print("here are the followers nunmbers"+str(len(names)))
                                                    
        element = self.driver.find_element_by_xpath("/html/body/div["+self.version+"]/div/div/div[1]/div/div[2]/button")
        
        element.click()

        return names





if __name__=='__main__':
   # ins_bot=InstagrammBot('techlux.ga','techlux') 

        
    #ins_bot=InstagrammBot('stevebrook223','aria2005','stevebrook223')

    #ins_bot=InstagrammBot('successletters','aria2005','successletters')
    ins_bot=InstagrammBot('goerogemike1001','aria2005','goerogemike1001')
    #ins_bot=InstagrammBot("techlux.ga","apexlegend","techlux.ga")
 
   # ins_bot=InstagrammBot('successletters','aria2005','successletters')

    ins_bot.message_followers()    






        

#
#
#Vintage
#
#
#
#Stylish
#InstaStyle
        








        

#
#
#Vintage
#
#
#
#Stylish
#InstaStyle
        
        





 

# PAYPAL 300$  satisfyingvibes2005@gmail.com  Aria2005






        

#
#
#Vintage
#
#
#
#Stylish
#InstaStyle
        
        





 

# PAYPAL 300$  satisfyingvibes2005@gmail.com  Aria2005