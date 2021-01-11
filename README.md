# Instagram-unfollower
A bot that gathers the user's Instagram followers and followees and unfollows those who don't follow the user back.

Keep in mind, Instagram servers may ignore some unfollow requests if there are too many. If this happens, some of the ghosts (people who don't follow the user back) may not have been unfollowed. No worries! Just run the bot again until all ghosts have been busted, or if the user wants to manually do some busting.

Requirements: Python 3 or later, chromedriver, selenium

Link to download chromedriver: https://chromedriver.chromium.org/

To connect chromdriver with the bot, simply edit line 21 (self.browser = webdriver.Chrome()) to include the path of where chromedriver.exe is located. For example, webdriver.Chrome("path here"). Alternatively, can move/download chromedriver.exe directly to where the bot is located, eliminating the requirement of including the path.

Put instagram username and password into a secrets.py file and import it directly to InstaGhostBuster.py

Install selenium package 
