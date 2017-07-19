import time

import random

from selenium import webdriver

chrome_path = r"C:\Selenium\chromedriver.exe"

number_of_signups = 0

def gen_rand_un():
    un = "16JE00"
    un += str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
    return un

while 1:
        un = gen_rand_un()

        driver = webdriver.Chrome(chrome_path)
        url = r"http://myshoutbox.ml/signup.php"
        driver.get(url)
        
        fname = driver.find_element_by_id("fname1")
        fname.send_keys("Hacker")

        lname = driver.find_element_by_id("lname1")
        lname.send_keys("Bro")

        username = driver.find_element_by_id("username1")
        username.send_keys(un)

        password = driver.find_element_by_id("password1")
        password.send_keys("Hello@123")

        re_password = driver.find_element_by_id("repass1")
        re_password.send_keys("Hello@123")

        email = driver.find_element_by_id("email1")
        email.send_keys("hacker" + un + "@gmail.com")

        outside = driver.find_element_by_id("log")
        outside.click()
        
        btn = driver.find_element_by_name("submit")
        btn.click()

        #Waiting to get registered:
        time.sleep(5)

        driver.quit()
        
        number_of_signups += 1
        print("No. of Signups so far: {}".format(number_of_signups))
        

        
