from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from secrets import username,password
import instaloader

# Global Variables

user_followers = []
user_followees = []
count_followers = 0
count_followees = 0
ghosts = []

class InstaUnfollow:
    def __init__(self):
        # Create instance
        self.browser = webdriver.Chrome()
        self.browser.get("https://instagram.com")
        sleep(2)

        # Fill in user details
        self.browser.find_element_by_name("username").send_keys(username)
        self.browser.find_element_by_name("password").send_keys(password)
        sleep(2)

        # Find login button and log in
        submit = self.browser.find_element_by_tag_name('form')
        submit.submit()
        sleep(2)

        # Bypass prompts
        # Save info prompt
        buttons1 = self.browser.find_elements_by_tag_name("button")
        bypass1 = buttons1[-1]
        bypass1.click()
        sleep(5)

        # Notificaitons prompt
        buttons2 = self.browser.find_elements_by_tag_name("button")
        bypass2 = buttons2[-1]
        bypass2.click()
        sleep(5)

        # Unfollow each user in ghosts
        for user in ghosts:
            print("Unfollowing " + user)
            # Find user through search bar by username (guarantees first result)
            search_bar = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
            search_bar.send_keys(user)
            sleep(2)

            search_bar.send_keys(Keys.ENTER)
            sleep(2)
            search_bar.send_keys(Keys.ENTER)
            sleep(5)

            # Find and click unfollow button
            buttons3 = self.browser.find_elements_by_tag_name("button")
            unfollow_button = buttons3[1]
            unfollow_button.click()
            sleep(5)

            # Click through unfollow prompt
            buttons4 = self.browser.find_elements_by_tag_name("button")
            unfollow_button1 = buttons4[-2]
            unfollow_button1.click()
            sleep(5)

        print("Job done... Thank you for using InstaGhostBusters")

class InstaLoad:
    def __init__(self):
        # Create instance
        loader = instaloader.Instaloader()
        loader.login(username, password)
        user = instaloader.Profile.from_username(loader.context, username)

        # Get followers 
        followers = list(set(user.get_followers()))
        for item in followers:
            temp = str(item)
            x = temp.index(" ")
            temp = temp[x+1:]
            y = temp.index(" ")
            temp = temp[:y]
            user_followers.append(temp)
        count_followers = len(user_followers)
        
        # Get followees
        followees = list(set(user.get_followees()))
        for item in followees:
            temp = str(item)
            x = temp.index(" ")
            temp = temp[x+1:]
            y = temp.index(" ")
            temp = temp[:y]
            user_followees.append(temp)
        count_followees = len(user_followees)
        
        # Followees that don't follow back 
        global ghosts 
        ghosts = list(set(user_followees).difference(user_followers))
        print("Gathering list of ghost followers...")
        InstaUnfollow()

InstaLoad()


