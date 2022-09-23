from selenium import webdriver
class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def login(self):
        self.driver.get('https://tinder.com')
        phone_log=self.driver.find_element_by_xpath('/html/body/div[2]/main/div/div[1]/div/div/div[3]/span/div[3]/button/span[2]')
        phone_log.click()
        #Switch to login window
        base_window=self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        phone_number=self.driver.find_element_by_xpath('/html/body/div[2]/main/div/div[1]/div/div[2]/div/input')
        phone_number.send_keys('9460202770')
        
    