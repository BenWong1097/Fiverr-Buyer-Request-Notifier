import unittest
import time
import winsound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configparser import ConfigParser

interval = 60
bad_interval = 60
number_fail = 0
iteration = 0
count = None
count2 = None
username = ""
driver_path = ""
password = ""
window_x = 0
window_y = 0
def read_config():
    global driver_path, username, password, interval, bad_interval, window_x, window_y
    config = ConfigParser()
    config.read('config.ini')
    driver_path = config.get('main', 'chrome webdriver location')
    username = config.get('main', 'username')
    password = config.get('main', 'password')
    interval = config.getint('settings', 'time interval')
    bad_interval = config.getint('settings', 'fail time interval')
    window_x = config.getint('settings', 'window x-position')
    window_y = config.getint('settings', 'window y-position')

#Emit sound if event occurs
def notify(mode = 1):
    #New notification
    if mode == 1:
        winsound.Beep(300, 250)
        winsound.Beep(600, 125)
        winsound.Beep(600, 125)
    #Bot-detected notification
    elif mode == 2:
        winsound.Beep(300, 200)
    
class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        read_config()
        
    #Log in
    def login_fiverr(self):
        driver = self.driver
        driver.implicitly_wait(10)
        driver.get("http://www.fiverr.com/login")
        username_el = driver.find_element_by_xpath("//input[@placeholder='Email / Username']")
        username_el.send_keys(username)
        password_el = driver.find_element_by_xpath("//input[@placeholder='Password']")
        password_el.send_keys(password)
        submit = driver.find_element_by_xpath("//input[@id='login-btn']").click()
        
    #[Helper - check_active] Gets the # of buyer requests
    def get_count(self):
        global count, number_fail
        try:
            driver = self.driver
            count_el = driver.find_element_by_xpath("//a[@data-gtm-label='all requests']")
            count_local = count_el.get_attribute("data-count")
            return count_local
        except:
            notify(2)
            time.sleep(bad_interval)
            driver.quit()
            number_fail = number_fail + 1
            return count

    #Goes to requests page to grab # of buyer requests
    def check_active(self):
        self.driver = webdriver.Chrome(driver_path)
        driver = self.driver
        driver.set_window_position(window_x, window_y)
        self.login_fiverr()
        time.sleep(1)
        driver.get("https://www.fiverr.com/users/"+username+"/requests")
        count = self.get_count()
        time.sleep(interval)
        driver.quit()
        return count

    #Loop until the number of requests increases
    def test_fiverr(self):
        global count, count2, iteration
        #Initialize starting #
        count = self.check_active()
        count2 = count
        iteration = 0
        while count >= count2:
            count = count2
            iteration = iteration + 1
            time.sleep(5)
            try:
                count2 = self.check_active()
            except:
                notify(2)
                self.driver.quit()                
                time.sleep(5)
                continue
            #Prints the current number of active requests
            print(str(iteration) + ": " + str(count2))
            
    def tearDown(self):
        notify()
        #   Displays what # of requests changed from and to
        #print(str(count) + " -> " + str(count2))
        #   Displays # of times bot page has been shown.
        #print("Test fail rate: " + str(number_fail) + "/" + str(iteration) )
        try:
        #   Shut down the driver if it's still up for some reason
            self.driver.close()
        except:
            return

if __name__ == "__main__":
    unittest.main()
