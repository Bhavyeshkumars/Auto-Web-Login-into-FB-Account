from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


#usr=input('Enter Email Id:')
#pwd=input('Enter Password:')

usr="XXXXXXXXXXXXXXXX@gmail.com"
pwd="XXXXXXXXXXXXX"

driver = webdriver.Chrome(" Path to be mentioned for chromedriver/chromedriver.exe")
driver.get("https://www.facebook.com/")

print ("Opened facebook Account")
sleep(1)

username_box = driver.find_element_by_id('email') 
username_box.send_keys(usr) 
print ("Email Id entered") 
sleep(1) 
  
password_box = driver.find_element_by_id('pass') 
password_box.send_keys(pwd) 
print ("Password entered") 
  
login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 


print ("Completed") 
driver.save_screenshot('screenshot_FB_ID.png')
input('Press anything to key quit') 
driver.quit() 
print("Web Login successfully Finished")

