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
from random import randint
import requests
import sys
import numpy as np

# DELETE ALL THE LETTER "bh" IF YOU WANT TO RUN THE PROGRAMMA AS INTENTED
class InstagrammBot:
    def __init__(self,username,password,usernameof,isitokk,des):
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
        self.usernameof=usernameof
        self.isitokk=isitokk
        self.driver=webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.namessss="aria"
        self.version='5'
        self.dd=True
        self.des=des
     #   self.victim=iut("ENTER THE VICTIM")


    def login(self):
        therann=True
        thearray=[["hi wassup are you ","so  i got an instagram account with 280K Followers @thesatisfyingtaste ","i am selling for 140$","i need to sell it ASAP because of shool and if interested MESSAGE me only at @thesatisfyingtaste  NOT here "],   ["jo ","i got a 286K Instagram Page i Sell ads here is username ","@thesatisfyingtaste","most ads get sales and most of my followers are from us dm me if interested "],["hei are you ","i thought you were interested in an ad i got a 280K Instagram page. followers are from us ","@thesatisfyingtaste","lemme know if interested in ad or stats or just message me there ???"],["Whazzup ","i got an offer that you may be interested in ","so i have an 280K ig Page most followers are from us i sell ads lemme know if interested","@thesatisfyingtaste so ??"],["Sup ","so i run an instagram page with over 280K followers  ","and i am selling ads on it most ads are succesful and get sales","Dm if interesed  @thesatisfyingtaste"]]
        
        def redo():
            input("it seems your numbers were smalles then 155555555:s")
            all=[]
            k="6"                                   
            try:                                         
                followingb=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div')

            except:                                      
                followingb=self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div')
                k="7"
            for i in range(44):
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop - arguments[0].offsetHeight;', followingb)
                sleep(5)
                                                                                                                                             
                names=self.driver.find_element_by_xpath('/html/body/div['+k+']/div/div/div[2]/div/div').find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")


                for i in names:
                    all.append(i.get_attribute("innerHTML"))
                print("j")


            print(len(all))

            namess = list(set(all))

            for i in namess:
                print(i)
            print(len(all))
            if len(all)<=20:
                redo()
            print(len(namess))




        def sendthemessage(usernamee):  
                print("sending message")
                theran=0
                # boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

                # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                

                # boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                # boo.send_keys('hei so i know this is a bit weird but i need an spare account fast are you intereseed in selling yours i will pay 35$ immidiently')
                # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                

                if therann==True :

                    sleep(1)                                
                    try:
                        try:                                               
                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            try:
                                boo.send_keys(thearray[theran][0]+ usernamee)
                                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
          
                            except:
                                pass
                            
                            sleep(2)

                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][1])
                            
                            sleep(1)
                            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
               
                            sleep(2)
                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][2])
                            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()


                            sleep(1)
                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][3])
                            sleep(1)                           
                            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                        except:
                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            try:
                                boo.send_keys(thearray[theran][0]+ usernamee)
                                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
          
                            except:
                                pass
                            
                            sleep(2)

                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][1])
                            
                            sleep(1)
                            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
               
                            sleep(2)
                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][2])
                            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()


                            sleep(1)
                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][3])
                            sleep(1)                           
                            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

                    except:

                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        try:
                            boo.send_keys(thearray[theran][0]+ usernamee)
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
      
                        except:
                            pass
                        
                        sleep(2)

                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        boo.send_keys(thearray[theran][1])
                        
                        sleep(1)                           
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
           
                        sleep(2)
                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        boo.send_keys(thearray[theran][2])
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()


                        sleep(1)
                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        boo.send_keys(thearray[theran][3])
                        sleep(1)                           
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

        try:
            self.driver.get('https://www.instagram.com/accounts/login/') 
        except:
            filename=r"C:\\Users\\amdin\\Documents\\asharin\\"+ self.des+".bat"
            os.system("start " + filename)
            self.driver.close()
            sys.exit()



        sleep(1)                            
        try:
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        except:  
            try:
                self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button[1]').click()
            except:
                pass
        sleep(3)
        print(self.username)
        print(self.usernameof)       
                         
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
    


        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        sleep(2)  
        try:
            button=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            button.click()                          
            sleep(3)
        except:
            filename=r"C:\\Users\\amdin\\Documents\\asharin\\"+ self.des+".bat"
            os.system("start " + filename)
            self.driver.close()
            sys.exit()



        try: 
            try:                                   
                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
            except:
                try:
                    self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
                except:
                    self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        except:
            try:
                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
            except:
                pass
        

        lagos=False

        try:
            print("3")                          
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div[1]/div/div[2]/button').click()
            lagos=True
            print("joker")
            okkk
        except:
            if lagos==True:
                self.driver.close()
                sys.exit()
            print("9")
            pass            



        try:
            try:  
                try: 

                    self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
                except:                                 

                    self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]/a").click()
            except:   

                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        except:
            self.driver.get("https://www.instagram.com/direct/inbox/")

        sleep(2)
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]").click()
        except:
            pass
        try:

    
            if(self.isitokk==False):
                ever.testing(self.driver,self.des)
        except :
            try:                                          
                newmsg=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[2]/a').get_attribute("aria-label")
            except:
                newmsg="k"               

            print("g")
            self.driver.close()
            sys.exit()
        else:
            try:                                
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()

                sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
            except:


                pass


            sleep(1)  
       # input("enter when ready:::::::::::::")

        all_names = np.load('data.npy')
        all_names= all_names.tolist()
        namess = [all_names.pop() for d in range(70)]#70
      #  input("enter to continie")
        np.save('data.npy', all_names) # save
        print("it has been saved")
        thenum=1
        secondnum=0
        sleep(1)
        newar=namess
        changenum=1
        for user in namess:

            #self.domainex(newar) # MUST BE REMOVED LATER BUT NOT NOWWWWW
            self.driver.get("https://www.instagram.com/direct/inbox/")

            sleep(4)                    
            # this writes the username in the searchbar and clicks it
            try:                                        
                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[1]/div/div[2]/input').send_keys(user)
            except:
                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[1]/div/div[2]/input').send_keys(user)
            sleep(1)
            password=True              

            
            newar.pop(0)
            try:                                                      
                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[1]/div/div[2]/div[3]/div/div[2]/div/div[1]/a').click()
            except:
 
                self.driver.get("https://www.instagram.com/"+user)
 
            sleep(1)
            #checks if the account is private or not
            try:                                   

               # try:                                    
               #     self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[2]/button').click()
               # except:  
               #     try:                               
                 #       self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[2]/button').click()
                #    except:
                #        sleep(3)                
               #         self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[3]/button") 

                # try:              # to be continued

                self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/div/article/div[1]/div/h2")
                try:                                   
                    self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
                except:    
                    self.driver.get("https://www.instagram.com/direct/inbox/")
            
                password=False


            except:          
               # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[2]/button')
                pass


 
            if password==True:     

                try:

                    self.retriver(user)
                except:
                    pass
                try:                                   
                    try: 
                            self.driver.find_element_by_css_selector("._acan._acap._acas").click()
                    except:                                    
                            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/button').click()
                except:   

                    self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button').click()
                sleep(1)


# here we add message to post to image



                try:
                    try:                                                    
                        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button').click()
                    except:         
                        try:                          
                                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button').click()
                        except:                                     
                                self.driver.find_element_by_css_selector("._acan._acap._acat").click()
                    sendthemessage(user)
                    thenum+=1
                    print('we got one')              
                except:                                     
                    try:
                        sleep(1)                                
                        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/button[1]').click()
                        self.domainex(newar)
                    except:
                        pass

                    try:                                                                    
                        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
                    except:
                        try:
                            try: 
                                
                                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[1]').click()
                            except:    
                                self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
                        except:
                            print("well there is  a chance that the account is temperoraly action blocked::.")
                            changenum+=1
                            self.driver.get("https://www.instagram.com/direct/inbox/")
                      


                    try:                                   
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
                        print("cor")                       
                    except:
                        try:
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
                        except:
                            pass
                    sleep(1)
                if changenum%8==0:
                    changenum+=1
                    print("PLAN B")
                    self.domainex(newar)
                    thenum+=1

                if thenum%5==0:
                    # self.pubish()
                    print(thenum)      

                    newmsg="9"
                    print('we are sleeping  (: '+ str(newmsg) )

                    nums=["0","1","2","3","4","5","6","7","8","9","10","11"]
                    for i in str(newmsg):
                        for n in nums:
                            if i ==n:
                                newmsg="Message:"+str(i)

                    sleep(1950)

        filename=r"C:\\Users\\amdin\\Documents\\asharin\\"+ self.des+".bat"
        os.system("start " + filename)
        self.driver.close()
        sys.exit()
    def mainst(self):
        print("ii")
        therann=True
        thearray=[["hi are u ","so  i got a instagram account with 280K Followers @thesatisfyingtaste ","i was thinking for 140$","i need to sell it ASAP MESSAGE me only at @thesatisfyingtaste  NOT here "],   ["jo ","i got a 286K Instagram Page i Sell ads here is username ","@thesatisfyingtaste","most ads get sales and most of my followers are from us dm me if interested "],["hei are you ","i thought you were interested in an ad i got a 280K Instagram page. followers are from us ","@thesatisfyingtaste","lemme know if interested in ad or stats or just message me there ???"],["Whazzup ","i got an offer that you may be interested in ","so i have an 280K ig Page most followers are from us i sell ads lemme know if interested","@thesatisfyingtaste so ??"],["Sup ","so i run an instagram page with over 280K followers  ","and i am selling ads on it most ads are succesful and get sales","Dm if interesed  @thesatisfyingtaste"]]
        
        def redo():
            input("it seems your numbers were smalles then 155555555:s")
            all=[]
            k="6"                                   
            try:                                         
                followingb=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div')

            except:                                      
                followingb=self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div')
                k="7"
            for i in range(44):
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop - arguments[0].offsetHeight;', followingb)
                sleep(5)
                                                                                                                                             
                names=self.driver.find_element_by_xpath('/html/body/div['+k+']/div/div/div[2]/div/div').find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")


                for i in names:
                    all.append(i.get_attribute("innerHTML"))
                print("j")


            print(len(all))

            namess = list(set(all))

            for i in namess:
                print(i)
            print(len(all))
            if len(all)<=20:
                redo()
            print(len(namess))




        def sendthemessage(usernamee):  
                print("sending message")
                theran=0
                # boo=self.driver.find_element_by_xpath('//*[@id="bat react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

                # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                

                # boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                # boo.send_keys('hei so i know this is a bit weird but i need an spare account fast are you intereseed in selling yours i will pay 35$ immidiently')
                # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                

                if therann==True :

                    sleep(1)                                
                    try:
                        try:
                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            try:
                                boo.send_keys(thearray[theran][0]+ usernamee)
                                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
          
                            except:
                                pass
                            
                            sleep(2)

                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][1])
                            
                            sleep(1)
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
               
                            sleep(2)
                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][2])
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()


                            sleep(1)
                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][3])
                            sleep(1)                           
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                        except:
                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            try:
                                boo.send_keys(thearray[theran][0]+ usernamee)
                                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
          
                            except:
                                pass
                            
                            sleep(2)

                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][1])
                            
                            sleep(1)
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
               
                            sleep(2)
                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][2])
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()


                            sleep(1)
                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][3])
                            sleep(1)                           
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

                    except:

                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        try:
                            boo.send_keys(thearray[theran][0]+ usernamee)
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
      
                        except:
                            pass
                        
                        sleep(2)

                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        boo.send_keys(thearray[theran][1])
                        
                        sleep(1)                           
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
           
                        sleep(2)
                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        boo.send_keys(thearray[theran][2])
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()


                        sleep(1)
                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        boo.send_keys(thearray[theran][3])
                        sleep(1)                           
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

        self.driver.get('https://www.instagram.com/accounts/login/') 

        sleep(1)                            
        try:
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        except:  
            try:
                self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button[1]').click()
            except:
                pass
        sleep(6)
        sleep(1)  
        print(self.username)
        print(self.usernameof)       
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)



        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        sleep(2)                                   
        button=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        button.click()                          
        sleep(3)
        
        try: 
            try:                                   
                self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
            except:
                try:
                    self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
                except:
                    self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        except:
            try:
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[2]').click()
            except:
                pass

        try:                                 
            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        except:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()

        sleep(2)



        sleep(1)                            
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()


        sleep(1)  


        try:                                   
            self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/section/div/div[1]/div/div[2]/input").send_keys(self.usernameof)
        except:                                
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[2]/input').send_keys(self.usernameof)
        sleep(3)                                                                                

        try:                                                      
            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[1]/div/div[2]/div[3]/div/div[2]/div/div[1]/a').click()
        except:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[2]/div[3]/div/div[2]/div/div/a').click()        



        try:
            print("fitd")
            sleep(1)                           
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()

        except:
            print("fitssss")
            try:
                print("ftttssssssss")
                sleep(2)                          
                self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[2]/a').click()
            
            except:
                print("ftssssssssssssssssssssss")
                sleep(2)
            
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
                
        wholelist=[]
        choice= input("ENTER x FOR FOLLOWERS OPTION ;ENTER NOTHING FOR LIKES OPTION : ")                    

        if choice=="x":
            try:                                               
                followingb=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')

                followingb=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')


                #input
                links=followingb.find_elements_by_tag_name('a')
                names=[name.text for name in links if name.text !=''] 
                namess=names[::-1]
                print(names )
                print(namess)
                print(len(names))

                followingb=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
                                                                     
            #         res.append(i)
                sleep(1)                          
                self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/button').click()
            except:

                followingb=self.driver.find_element_by_class_name('isgrP')

                followingb=self.driver.find_element_by_class_name('isgrP')


                #input
                links=followingb.find_elements_by_tag_name('a')
                names=[name.text for name in links if name.text !=''] 
                namess=names[::-1]
                print(names )
                print(namess)
                print(len(names))

                followingb=self.driver.find_element_by_class_name('isgrP')
                                                                     
            #         res.append(i)
                sleep(1)                            
                try:
                    self.driver.find_elements_by_class_name('wpO6b')[2].click()
                except:
                    self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
                sleep(1)                        
        else:

            all=[]
            k="6"     
            wholelot="/html/body/div[6]/div/div/div[2]/div/div"

            try:          
                try:                                 
                    followingb=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div')
                    wholelot="/html/body/div[6]/div/div/div[2]/div/div"
                except:
                    followingb=self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div[1]/div')
                    wholelot="/html/body/div[7]/div/div/div[2]/div[1]/div"                    
            except:     
                    followingb=self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div')
                    wholelot="/html/body/div[7]/div/div/div[2]/div/div"
                    try:
                        self.driver.find_element_by_xpath(wholelot).find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")
                    except:
                        
                        followingb=self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[3]/div')
                        wholelot="/html/body/div[7]/div/div/div[3]/div/div" 


            for i in range(304):
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop - arguments[0].offsetHeight;', followingb)
                sleep(5)
                                                                                                                                             
                names=self.driver.find_element_by_xpath(wholelot).find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")


                for i in names:
                    all.append(i.get_attribute("innerHTML"))
                print("j")


            print(len(all))


            s=[]
            for i in all:
               if i not in s:
                  s.append(i)

            namess=s[::-1]
            for i in namess:
                print(i)

        new_num_arr = np.load('data.npy') # loa<
        kk=new_num_arr.tolist()
        print(len(kk))

        for i in namess:
            kk.append(i)

        np.save('data.npy', kk)
        new_num_arr = np.load('data.npy') # loa<
   
        wholelist=[]
        choice= input("ENTER x FOR FOLLOWERS OPTION ;ENTER NOTHING FOR LIKES OPTION : ")                    

        if choice=="x":
            try:                                               
                followingb=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')

                followingb=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')


                #input
                links=followingb.find_elements_by_tag_name('a')
                names=[name.text for name in links if name.text !=''] 
                namess=names[::-1]
                print(names )
                print(namess)
                print(len(names))

                followingb=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
                                                                     
            #         res.append(i)
                sleep(1)                          
                self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/button').click()
            except:

                followingb=self.driver.find_element_by_class_name('isgrP')

                followingb=self.driver.find_element_by_class_name('isgrP')


                #input
                links=followingb.find_elements_by_tag_name('a')
                names=[name.text for name in links if name.text !=''] 
                namess=names[::-1]
                print(names )
                print(namess)
                print(len(names))

                followingb=self.driver.find_element_by_class_name('isgrP')
                                                                     
            #         res.append(i)
                sleep(1)                            
                try:
                    self.driver.find_elements_by_class_name('wpO6b')[2].click()
                except:
                    self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()
                sleep(1)                        
        else:

            all=[]
            k="6"   
            wholelot="/html/body/div[6]/div/div/div[2]/div/div"

            try:                                                        
                followingb=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div')
                wholelot="/html/body/div[6]/div/div/div[2]/div/div"
            except:     
                    followingb=self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div')
                    wholelot="/html/body/div[7]/div/div/div[2]/div/div"
                    try:
                        self.driver.find_element_by_xpath(wholelot).find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")
                    except:
                        
                        followingb=self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[3]/div')
                        wholelot="/html/body/div[7]/div/div/div[3]/div/div" 


            for i in range(304):
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop - arguments[0].offsetHeight;', followingb)
                sleep(2)
                                                                                                                                             
                names=self.driver.find_element_by_xpath(wholelot).find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")


                for i in names:
                    all.append(i.get_attribute("innerHTML"))
                print("j")


            print(len(all))


            s=[]
            for i in all:
               if i not in s:
                  s.append(i)

            namess=s[::-1]
            for i in namess:
                print(i)



        new_num_arr = np.load('data.npy') # loa<
        kk=new_num_arr.tolist()
        print(len(kk))

        for i in namess:
            kk.append(i)

        np.save('data.npy', kk)
        new_num_arr = np.load('data.npy') # loa<

        print(len(new_num_arr))


    def domainex(self,aww):


        thearray=[["hi are u ","so  i got a instagram account with 280K Followers @thesatisfyingtaste ","i was thinking for 140$","i need to sell it ASAP MESSAGE me only at @thesatisfyingtaste  NOT here "],   ["jo ","i got a 286K Instagram Page i Sell ads here is username ","@thesatisfyingtaste","most ads get sales and most of my followers are from us dm me if interested "],["hei are you ","i thought you were interested in an ad i got a 280K Instagram page. followers are from us ","@thesatisfyingtaste","lemme know if interested in ad or stats or just message me there ???"],["Whazzup ","i got an offer that you may be interested in ","so i have an 280K ig Page most followers are from us i sell ads lemme know if interested","@thesatisfyingtaste so ??"],["Sup ","so i run an instagram page with over 280K followers  ","and i am selling ads on it most ads are succesful and get sales","Dm if interesed  @thesatisfyingtaste"]]


        therann=True
        thearray=[["hi are u ","so  i got a instagram account with 280K Followers @thesatisfyingtaste ","i was thinking for 140$","i need to sell it ASAP MESSAGE me only at @thesatisfyingtaste  NOT here "],   ["jo ","i got a 286K Instagram Page i Sell ads here is username ","@thesatisfyingtaste","most ads get sales and most of my followers are from us dm me if interested "],["hei are you ","i thought you were interested in an ad i got a 280K Instagram page. followers are from us ","@thesatisfyingtaste","lemme know if interested in ad or stats or just message me there ???"],["Whazzup ","i got an offer that you may be interested in ","so i have an 280K ig Page most followers are from us i sell ads lemme know if interested","@thesatisfyingtaste so ??"],["Sup ","so i run an instagram page with over 280K followers  ","and i am selling ads on it most ads are succesful and get sales","Dm if interesed  @thesatisfyingtaste"]]

        def sendthemessage(usernamee):  
                print("sending message")
                theran=0
                # boo=self.driver.find_element_by_xpath('//*[@id="bat react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

                # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                

                # boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                # boo.send_keys('hei so i know this is a bit weird but i need an spare account fast are you intereseed in selling yours i will pay 35$ immidiently')
                # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                

                if therann==True :

                    sleep(1)                                
                    try:
                        try:
                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            try:
                                boo.send_keys(thearray[theran][0]+ usernamee)
                                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
          
                            except:
                                pass
                            
                            sleep(2)

                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][1])
                            
                            sleep(1)
                            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
               
                            sleep(2)
                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][2])
                            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()


                            sleep(1)
                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][3])
                            sleep(1)                           
                            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                        except:
                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            try:
                                boo.send_keys(thearray[theran][0]+ usernamee)
                                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
          
                            except:
                                pass
                            
                            sleep(2)

                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][1])
                            
                            sleep(1)
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
               
                            sleep(2)
                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][2])
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()


                            sleep(1)
                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][3])
                            sleep(1)                           
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

                    except:

                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        try:
                            boo.send_keys(thearray[theran][0]+ usernamee)
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
      
                        except:
                            pass
                        
                        sleep(2)

                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        boo.send_keys(thearray[theran][1])
                        
                        sleep(1)                           
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
           
                        sleep(2)
                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        boo.send_keys(thearray[theran][2])
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()


                        sleep(1)
                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        boo.send_keys(thearray[theran][3])
                        sleep(1)                           
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()


        sleep(40)
        try:
            try:

                  self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
            except:
                  try:                                
                        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
                  except:
                        self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        except:
            pass
        oj=0

        self.driver.get("https://www.instagram.com/direct/inbox/")

        for i in aww:
            oj+=1
            try:                                    
                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
            except:
                self.driver.find_element_by_css_selector("._abl-._abm2").find_element_by_tag_name("button").click()

            sleep(5)

            try:
                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)
                
            except :
                self.driver.find_element_by_css_selector('._aaie._aaid._aaiq').send_keys(i)
            sleep(5)

            try:

                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()                  
            except:                              
                el=self.driver.find_element_by_css_selector("._abl-").find_element_by_tag_name('button')
                self.driver.execute_script("arguments[0].click();", el)

            sleep(3)
            try:                                   
                try:
                    self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/button').click()
                except:
                    self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/button').click()
            except:
                self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
            sleep(3)    
            sendthemessage(i)
            if oj%10==0:
                sleep(1770)


    def login2(self):
        therann=True
        thearray=[["hi wassup are you ","so  i got an instagram account with 280K Followers @thesatisfyingtaste ","i am selling for 140$","i need to sell it ASAP because of shool and if interested MESSAGE me only at @thesatisfyingtaste  NOT here "],   ["jo ","i got a 286K Instagram Page i Sell ads here is username ","@thesatisfyingtaste","most ads get sales and most of my followers are from us dm me if interested "],["hei are you ","i thought you were interested in an ad i got a 280K Instagram page. followers are from us ","@thesatisfyingtaste","lemme know if interested in ad or stats or just message me there ???"],["Whazzup ","i got an offer that you may be interested in ","so i have an 280K ig Page most followers are from us i sell ads lemme know if interested","@thesatisfyingtaste so ??"],["Sup ","so i run an instagram page with over 280K followers  ","and i am selling ads on it most ads are succesful and get sales","Dm if interesed  @thesatisfyingtaste"]]
        
        def redo():
            input("it seems your numbers were smalles then 155555555:s")
            all=[]
            k="6"                                   
            try:                                         
                followingb=self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div')

            except:                                      
                followingb=self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div')
                k="7"
            for i in range(44):
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop - arguments[0].offsetHeight;', followingb)
                sleep(5)
                                                                                                                                             
                names=self.driver.find_element_by_xpath('/html/body/div['+k+']/div/div/div[2]/div/div').find_elements_by_css_selector("._7UhW9.xLCgt.qyrsm.KV-D4.se6yk.T0kll")


                for i in names:
                    all.append(i.get_attribute("innerHTML"))
                print("j")


            print(len(all))

            namess = list(set(all))

            for i in namess:
                print(i)
            print(len(all))
            if len(all)<=20:
                redo()
            print(len(namess))




        def sendthemessage(usernamee):  
                print("sending message")
                theran=0
                # boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')

                # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                

                # boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                # boo.send_keys('hei so i know this is a bit weird but i need an spare account fast are you intereseed in selling yours i will pay 35$ immidiently')
                # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                

                if therann==True :

                    sleep(1)                                
                    try:
                        try:
                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            try:
                                boo.send_keys(thearray[theran][0]+ usernamee)
                                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
          
                            except:
                                pass
                            
                            sleep(2)

                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][1])
                            
                            sleep(1)
                            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
               
                            sleep(2)
                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][2])
                            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()


                            sleep(1)
                            boo=self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][3])
                            sleep(1)                           
                            self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
                        except:
                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            try:
                                boo.send_keys(thearray[theran][0]+ usernamee)
                                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
          
                            except:
                                pass
                            
                            sleep(2)

                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][1])
                            
                            sleep(1)
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
               
                            sleep(2)
                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][2])
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()


                            sleep(1)
                            boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                            boo.send_keys(thearray[theran][3])
                            sleep(1)                           
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

                    except:

                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        try:
                            boo.send_keys(thearray[theran][0]+ usernamee)
                            self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
      
                        except:
                            pass
                        
                        sleep(2)

                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        boo.send_keys(thearray[theran][1])
                        
                        sleep(1)                           
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
           
                        sleep(2)
                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        boo.send_keys(thearray[theran][2])
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()


                        sleep(1)
                        boo=self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
                        boo.send_keys(thearray[theran][3])
                        sleep(1)                           
                        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

        try:
            self.driver.get('https://www.instagram.com/accounts/login/') 
        except:
            filename=r"C:\\Users\\amdin\\Documents\\asharin\\"+ self.des+".bat"
            os.system("start " + filename)
            self.driver.close()
            sys.exit()



        sleep(1)                            
        try:
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        except:  
            try:
                self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button[1]').click()
            except:
                pass
        sleep(3)
        print(self.username)
        print(self.usernameof)       
                         
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
    


        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        sleep(2)  
        try:
            button=self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            button.click()                          
            sleep(3)
        except:
            filename=r"C:\\Users\\amdin\\Documents\\asharin\\"+ self.des+".bat"
            os.system("start " + filename)
            self.driver.close()
            sys.exit()



        try: 
            try:                                   
                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
            except:
                try:
                    self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
                except:
                    self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        except:
            try:
                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()
            except:
                pass
        

        lagos=False

        try:
            print("3")                          
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div[1]/div/div[2]/button').click()
            lagos=True
            print("joker")
            okkk
        except:
            if lagos==True:
                self.driver.close()
                sys.exit()
            print("9")
            pass            




        try:
            try:  
                try: 

                    self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
                except:                                 

                    self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[4]/a").click()
            except:   
                                              
                self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        except:
            print("d")
            filename=r"C:\\Users\\amdin\\Documents\\asharin\\"+ self.des+".bat"
            os.system("start " + filename)
            self.driver.close()
            sys.exit()

        sleep(2)

        sleep(2)
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]").click()
        except:
            pass            


        try:

    
            if(self.isitokk==False):
                ever.testing(self.driver,self.des)
        except :
            try:                                          
                newmsg=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[2]/a').get_attribute("aria-label")
            except:
                newmsg="k"               

            print("g")
            self.driver.close()
            sys.exit()
            
        else:
            try:                                
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()

                sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
            except:


                pass


            sleep(1)  
       # input("enter when ready:::::::::::::")

        all_names = np.load('data.npy')
        all_names= all_names.tolist()
        namess = [all_names.pop() for d in range(70)]
      #  input("enter to continie")
        np.save('data.npy', all_names) # save
        print("it has been saved")
        thenum=1
        secondnum=0
        sleep(1)
        newar=namess
        changenum=1


        self.domainex(namess)

    def pubish(self):
        subreddits=["interestingasfuck","Damnthatsinteresting","mildlyinteresting","notinteresting","coolguides","GetMotivated","creepy","pics","Images","surrealmemes","nukedmemes","bonehurtingjuice","memes"]
        response = requests.get("https://meme-api.herokuapp.com/gimme/"+random.choice(subreddits)).json()

        text=response["title"]
        imagurl=response["url"]
        print(imagurl)

        r = requests.get(imagurl)
        if imagurl[-3:]=="gif" :
            name="memee.jpg"
        else:
            name="memee."+imagurl[-3:]

        with open(name,"wb") as f:
            f.write(r.content)
        

        print("C:\\Users\\User\\Documents\\makeedit\\"+name)


        print('C:\\Users\\User\\Documents\\instagrammbot\\asharin\\')

        self.driver.find_elements_by_css_selector(".wpO6b.ZQScA")[0].click()

        try:
            self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div/div[2]/div[1]/form/input').send_keys("C:\\Users\\User\\Documents\\makeedit\\"+name)
        except:
            self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div/div[2]/div[1]/form/input').send_keys(
                "C:\\Users\\User\\Documents\\makeedit\\"+name)

        # try:
        #     element = self.driver.find_element_by_xpath(
        #         '/html/body/div[7]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[4]/div/div[1]')
        # except:
        #     element = self.driver.find_element_by_xpath(
        #         '/html/body/div[7]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[4]/div/div[1]')
        sleep(3)                                                                                  
        self.driver.execute_script("arguments[0].click();",  self.driver.find_element_by_css_selector('.sqdOP.yWX7d.y3zKF'))
        # self.driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button').click()

        sleep(3)
        self.driver.execute_script("arguments[0].click();",  self.driver.find_element_by_css_selector('.sqdOP.yWX7d.y3zKF'))

        sleep(3)    

        self.driver.execute_script("arguments[0].click();",  self.driver.find_element_by_css_selector('.sqdOP.yWX7d.y3zKF'))
        sleep(3)                                                                              
        # self.driver.execute_script("arguments[0].click();",  self.driver.find_element_by_css_selector('.sqdOP.yWX7d.y3zKF'))
        try:
            self.driver.find_element_by_xpath("//textarea[@class='lFzco']").send_keys(text)
        except:
            pass
        sleep(4)
        print(3)
        try:
            self.driver.execute_script("arguments[0].click();",  self.driver.find_element_by_css_selector('.sqdOP.yWX7d.y3zKF'))
        except:
            pass
        sleep(3)
        self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/button').click()

    def retriver(self,nam): # THIS POSTS A COMMNET ON THERI RECENT POST

    #/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a
    #/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a
        if self.dd==True:
            #el3 = self.driver.find_element_by_css_selector(
            #    ".v1Nh3.kIKUG._bz0w").find_element_by_tag_name("a").click()

            el=self.driver.find_element_by_css_selector("._aabd._aa8k._aanf").find_element_by_tag_name('a').click()            
            sleep(3)

            try:
                #self.driver.find_element_by_css_selector("._15y0l").find_element_by_tag_name("button").click()
                try:                                        
                        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[2]/button").click()
                        sleep(1)
                        el3 = self.driver.find_element_by_css_selector("._ablz._aaoc").send_keys("hi @"+nam+"  pls check your hidden request messages i have to talk to u", Keys.ENTER)
                        try:
                            self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button").click()
                        except:
                            pass
                except:
                        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea").send_keys("hi  "+nam+" pls check your hidden request messages i have to talk to u", Keys.ENTER)
                        try:
                            self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button").click()
                        except:
                            pass

                self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/button[1]").click()               
                self.driver.get("https://www.instagram.com/"+nam)
                sleep(8)
                self.dd=False

            except:

                sleep(1)
                self.driver.get("https://www.instagram.com/"+ nam)
                sleep(4)
 
 
acc_names=["gpstephan","marktilbury","daniel_iles","foundblanc","nateobrienn","liamjameskay","quadrelljones","biaheza","sarfinance","sarahchrispy","robertoblake","thefinancialwolf","vdainora","sheldonevansx","nft.verse"]    
def nothingness(usernamee,passwordd,des,itis=False):  
    # input("ENTER;")  beastofecom  renelacad ecom quit basharjkatou kriskrohn noahkagan frankhatchett    kenmcelroyofficial marshallmalaba
    # print("randomaniter :"+ acc_names[random.randint(0,len(acc_names))])        
    ins_bot=InstagrammBot( usernamee, passwordd, acc_names[random.randint(0,len(acc_names) ) ],itis,des)
    if(itis==False):
        ins_bot.login()
    else:
        ins_bot.login2()
        # input("ENTER;")   exit

        # ins_bot=InstagrammBot("techlux.ga","apexlegend")     _robertbenjamin
    # input("ENTER;")


    # input("ENTER;")
    # ins_bot=InstagrammBot("logographicvibe ","logo2008")  execute_script
    # input("ENTER;")

    #  //*[@id="react-root"]/div/div/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a     humphreytalks

def no_follow_nothing(usernamee,passwordd):

    ins_bot=InstagrammBot( usernamee, passwordd, acc_names[random.randint(0,len(acc_names) ) ])

    ins_bot.login2()

def damain(username,passwordd):

    ins_bot=InstagrammBot( username, passwordd, acc_names[random.randint(0,len(acc_names) ) ],True,"run")
    ins_bot.mainst()


#
#
#
#
#
#
#
#
#
#
#