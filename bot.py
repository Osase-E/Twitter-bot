from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import random
from datetime import datetime
import datetime
import pyperclip
import time
from PythonMagick import Image

global recommendation
global total_liked
global total_tweets
total_liked = 0

total_tweets = 0
# recommendation is a list of pretyped responses you would like the bot to tweet about
# the list is populatesd with an external textfile to make the code easier to manage
recommendation = []
f = open("tweets.txt", "r", encoding="utf8")
for x in f:
    recommendation.append(x)
f.close()

class twitter_bot:
    def __init__(self):
        # Enter twitter username/email
        self.username="" 
        # Enter twitter password
        self.password=""
        self.bot=webdriver.Chrome()

    def login(self):
        bot=self.bot
        bot.get("https://twitter.com/login")
        time.sleep(10)
        email=bot.find_element_by_name('text')
        email.clear()
        email.send_keys(self.username)
        email.send_keys(Keys.RETURN)
        time.sleep(5)
        password=bot.find_element_by_name('password')
        password.clear()
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)

    def like_tweet(self, entry3):
        global total_liked
        check_if_bottom = set()
        like_counter = 0
        already_liked_counter = 0
        counter = 0
        bot = self.bot
        bot.get("https://twitter.com/search?q=" + str(
            entry3) + "&src=typed_query&f=live")

        time.sleep(random.randint(1, 6))
        while True:
            # Check for already liked posts
            al_liked = pyautogui.locateCenterOnScreen('like.png',
                                                      grayscale=True,
                                                      confidence=0.95)
            if not isinstance(al_liked, type(None)):
                already_liked_counter += 1

            heart = pyautogui.locateCenterOnScreen('hart.png', grayscale=True,
                                                   confidence=0.7)
            print(heart)
            while not isinstance(heart, type(None)):
                # Check for ads
                ad = pyautogui.locateCenterOnScreen('ad.png', grayscale=True,
                                                    confidence=0.8)
                while not isinstance(ad, type(None)):
                    if (ad.x > heart.x):
                        break
                    if ((ad.y - heart.y) <= 70) and (ad.x < heart.x):
                        print(ad.y, heart.y)
                        scroll_value = random.randint(100, 200)
                        bot.execute_script(
                            'window.scrollBy(0,%d)' % (scroll_value))
                        time.sleep(random.randint(1, 3))
                        continue

                heartx = heart.x + (random.randint(-2, 2))
                hearty = heart.y + (random.randint(-2, 2))
                pyautogui.click(heartx, hearty)
                like_counter += 1
                time.sleep(random.randint(0, 2))
                vary_rt = random.randint(0, 3)
                if not random.randint(0, vary_rt):
                    retweet = pyautogui.locateCenterOnScreen('rt.png',
                                                             grayscale=True,
                                                             confidence=0.9)
                    if not isinstance(retweet, type(None)):
                        rtx = retweet.x + (random.randint(-3, 3))
                        rty = retweet.y + (random.randint(-3, 3))
                        pyautogui.click(rtx, rty)
                        time.sleep(random.randint(1, 3))
                        rtx = retweet.x + (random.randint(-5, 0))
                        rty = retweet.y + (random.randint(-3, 2))
                        pyautogui.click(rtx, rty)
                time.sleep(random.randint(0, 7))
                heart = pyautogui.locateCenterOnScreen('hart.png',
                                                       grayscale=True,
                                                       confidence=0.8)

            scroll_value = random.randint(100, 500)
            bot.execute_script('window.scrollBy(0,%d)' % (scroll_value))
            time.sleep(random.randint(1, 6))
            check_if_bottom.add(
                bot.execute_script("return document.body.scrollHeight"))
            counter += 1
            print(counter, like_counter, already_liked_counter)
            if len(check_if_bottom) > 1:
                check_if_bottom.clear()
                counter = 0
            if counter > 10:
                bot.refresh()
                bot.get("https://twitter.com/search?q=" + str(
                    entry3) + "&src=typed_query&f=live")
                time.sleep(random.randint(1, 6))
                counter = 0
                already_liked_counter = 0
                like_counter = 0
                check_if_bottom.clear()
            if like_counter > random.randint(20, 37):
                total_liked += like_counter
                hm = random.randint(10, 22)
                print("Waiting for: %d minutes" % hm)
                now = datetime.datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                print("Started at: ", dt_string)
                return now, hm * 60
            if already_liked_counter > 10:
                hm = random.randint(10, 360)
                print("Waiting for: %d minutes" % hm)
                now = datetime.datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                print("Started at: ", dt_string)
                return now, hm * 60

    def tweet(self, entry3):
        global total_tweets
        check_if_bottom = set()
        like_counter = 0
        already_liked_counter = 0
        counter = 0
        bot = self.bot
        bot.get("https://twitter.com/search?q=" + str(
            entry3) + "&src=typed_query")

        time.sleep(random.randint(1, 6))
        while True:
            # Check for already liked posts
            al_liked = pyautogui.locateCenterOnScreen('like.png',
                                                      grayscale=True,
                                                      confidence=0.95)
            if not isinstance(al_liked, type(None)):
                already_liked_counter += 1

            heart = pyautogui.locateCenterOnScreen('hart.png', grayscale=True,
                                                   confidence=0.7)
            while not isinstance(heart, type(None)):
                # Check for ads
                ad = pyautogui.locateCenterOnScreen('ad.png', grayscale=True,
                                                    confidence=0.8)
                while not isinstance(ad, type(None)):
                    if (ad.x > heart.x):
                        break
                    if ((ad.y - heart.y) <= 70) and (ad.x < heart.x):
                        print(ad.y, heart.y)
                        scroll_value = random.randint(20,100)
                        bot.execute_script(
                            'window.scrollBy(0,%d)' % (scroll_value))
                        time.sleep(random.randint(1, 3))
                        continue

                reply = pyautogui.locateCenterOnScreen('reply.png',
                                                       grayscale=True,
                                                       confidence=0.7)

                if abs(reply.y - heart.y) <= 10:
                    heartx = heart.x + (random.randint(-2, 2))
                    hearty = heart.y + (random.randint(-2, 2))
                    pyautogui.click(heartx, hearty)
                    like_counter += 1
                    already_liked_counter = 0
                    time.sleep(random.randint(0, 7))
                    rpx = reply.x + (random.randint(-2, 2))
                    rpy = reply.y + (random.randint(-2, 2))
                    pyautogui.click(rpx, rpy)
                    time.sleep(random.randint(2,5))
                    pyperclip.copy(recommendation[random.randint(0,len(recommendation)-1)])
                    pyautogui.hotkey("ctrl", "v")
                    time.sleep(random.randint(1,3))
                    if random.randint(0,2):
                        Image("peach.gif").write("clipboard:") # replace peach.gif with an image you would like to upload with the reply
                        pyautogui.hotkey("ctrl", "v")
                        time.sleep(random.randint(1, 3))
                        pyautogui.move(120, 0)
                    scroll_value = random.randint(500, 1000)
                    pyautogui.scroll(scroll_value*-1)
                    time.sleep(random.randint(10,20))

                    #pyautogui.screenshot("wedww.png")
                    rp = pyautogui.locateCenterOnScreen('rp.png', grayscale=True,
                                                        confidence=0.9)
                    rpx = rp.x + (random.randint(-2, 2))
                    rpy = rp.y + (random.randint(-2, 2))
                    pyautogui.click(rpx, rpy)
                    print(like_counter)
                    time.sleep(random.randint(10,400))
                scroll_value = random.randint(73, 154)
                bot.execute_script('window.scrollBy(0,%d)' % (scroll_value))
                heart = pyautogui.locateCenterOnScreen('hart.png',
                                                       grayscale=True,
                                                       confidence=0.7)

            scroll_value = random.randint(73, 154)
            bot.execute_script('window.scrollBy(0,%d)' % (scroll_value))
            time.sleep(random.randint(1, 6))
            check_if_bottom.add(
                bot.execute_script("return document.body.scrollHeight"))
            counter += 1
            #print(counter, like_counter, already_liked_counter)
            if len(check_if_bottom) > 1:
                check_if_bottom.clear()
                counter = 0
            if counter > 10:
                bot.refresh()
                bot.get("https://twitter.com/search?q=" + str(
                    entry3) + "&src=typed_query&f=live")
                time.sleep(random.randint(1, 6))
                counter = 0
                already_liked_counter = 0
                like_counter = 0
                check_if_bottom.clear()
            if like_counter > random.randint(3, 8):
                total_tweets+=like_counter
                hm = random.randint(20, 38)
                print("Waiting for: %d minutes" % hm)
                now = datetime.datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                print("Started at: ", dt_string)
                return now, hm * 60
            if already_liked_counter > 10:
                hm = random.randint(20, 50)
                print("Waiting for: %d minutes" % hm)
                now = datetime.datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                print("Started at: ", dt_string)
                return now, hm * 60
                

def execute():
    log=twitter_bot()
    log.login()
    likes = 0
    like_time = 0
    tweets = 0
    tweet_time = 0
    while True:
        which = random.randint(0,1)
        if which == 0:
            # limiter to make sure the bot doesn't go over twitter limits
            if like_time != 0:
                if (datetime.datetime.now()-like_time).seconds < likes:
                    continue
            like_time, likes = log.like_tweet("") # the hashtag you would like to bot to go over and like
        else:
            if tweet_time != 0:
                if (datetime.datetime.now()-tweet_time).seconds < tweets:
                    continue
                return
            hashtag = random.randint(0, 4) # random number to pick which of the hashtags to go through
            latest_bool = random.randint(0, 1) # boolean to determine if the bot goes through live feed or not
            latest = "&f=live"
            choose = []  # list of hashtags you'd like the bot to go through
            search_string = choose[hashtag]
            if latest_bool:
                search_string = search_string + latest
            tweet_time, tweets = log.tweet(search_string)
                



while True:
    execute()
