from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
class InstaBot:

    def __init__(self):
        self.username="" #your username
        self.id="" #your login id maybe username or gmail
        self.password="" #your password

        chromeOptions=Options()
        chromeOptions.add_experimental_option("prefs",{"download.default_directory":"/home/akshay/Desktop/python/Instagram_boot/images_videos"})

        self.driver=webdriver.Chrome(executable_path="/home/akshay/Desktop/python/Instagram_boot/chromedriver",chrome_options= chromeOptions)


    # LOGIN SECTION
    def login_section(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]").click()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(self.username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(self.password)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
        self.driver.implicitly_wait(4)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div/div/button").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        time.sleep(3)
    def close_section(self):
        self.driver.close()

    # FUN GIVE NO. OF FOLLOWERS,POSTS,AND FOLLOWING OF PROFILE
    def get_no_of_followers_posts_following(self):
        self.driver.get(f"https://www.instagram.com/{self.username}")


        posts=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[1]/span").get_attribute('innerHTML')
        beautify_posts = BeautifulSoup(posts, 'html.parser')
        beautify_posts.prettify()
        print(beautify_posts.text)

        followers=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").get_attribute('innerHTML')
        self.beautify_followers=BeautifulSoup(followers,'html.parser')
        self.beautify_followers.prettify()
        print(self.beautify_followers.text)

        following=self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").get_attribute('innerHTML')
        self.beautify_following=BeautifulSoup(following,'html.parser')
        self.beautify_following.prettify()
        print(self.beautify_following.text)

        time.sleep(4)

    # GET FOLLOWERS LIST OF YOUR PROFILE

    def get_followers_list(self):
        instaobj.get_no_of_followers_posts_following()
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        scroll_list=self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        for i in range(int(self.beautify_followers.text.split(" ")[0])+100):
            self.driver.execute_script(f'arguments[0].scrollTop = arguments[0].scrollHeight/{str((int(self.beautify_followers.text.split(" ")[0])+101)-i)}', scroll_list)

        for i in range(int(self.beautify_followers.text.split(" ")[0])+100):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',scroll_list)
        followers=self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div")
        beautify_Details=BeautifulSoup(followers.get_attribute('innerHTML'),'html.parser')
        self.follower_list=[]
        for i in beautify_Details.findAll('li',{'class':'wo9IH'}):
            for j in i.findAll('a',{'class':'FPmhX notranslate _0imsa'}):
                self.follower_list.append(j.text)
        self.driver.get(f"https://www.instagram.com/{self.username}")

        return self.follower_list

    # GET FOLLOWING LIST OF YOUR PROFILE
    def get_following_list(self):
        instaobj.get_no_of_followers_posts_following()
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()

        scroll_list=self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")

        for i in range(int(self.beautify_following.text.split(" ")[0])+100):
            self.driver.execute_script(f'arguments[0].scrollTop = arguments[0].scrollHeight/{str((int(self.beautify_following.text.split(" ")[0])+101)-i)}', scroll_list)

        for i in range(int(self.beautify_following.text.split(" ")[0])+100):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',scroll_list)

        following=self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div")
        beautify_Details=BeautifulSoup(following.get_attribute('innerHTML'),'html.parser')
        self.following_list=[]
        for i in beautify_Details.findAll('li',{'class':'wo9IH'}):
            for j in i.findAll('a',{'class':'FPmhX notranslate _0imsa'}):
                self.following_list.append(j.text)
        self.driver.get(f"https://www.instagram.com/{self.username}")

        return self.following_list




    # LIKE NO. OF PICS OF GIVEN HASHTAGS
    def like_pics_of_particlar_hastags(self,hashtags,no_of_pics):

        self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag_name}")
        time.sleep(1)
        self.driver.find_element_by_class_name("v1Nh3").click()

        count=1
        while count<=no_of_pics:
            time.sleep(1)
            self.driver.find_element_by_class_name("fr66n").click()
            self.driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
            count+=1
        self.driver.get(f"https://www.instagram.com/{self.username}")
        time.sleep(3)


    # LIKES PICS OF PAGE WHICH IS NOT PRIVATE
    def like_pics_of_particlar_page(self,page_name,no_of_pics):

        self.driver.get(f"https://www.instagram.com/{page_name}")
        time.sleep(1)
        try:
            privacy = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/article/div[1]/div/h2").get_attribute('innerHTML')
            if privacy=="This Account is Private":
                print("Account is private follow to like photos")
                return
        except Exception as e:
            pass

        self.driver.find_element_by_class_name("v1Nh3").click()

        count = 1
        while count <= no_of_pics:
            time.sleep(1)
            self.driver.find_element_by_class_name("fr66n").click()
            self.driver.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
            count += 1
        self.driver.get(f"https://www.instagram.com/{self.username}")
        time.sleep(3)

    #TO DOWNLOAD IMAGES OF INSTAGRAM
    def down_pics_insta(self,url):
        self.driver.get("https://gramdown.net/")
        self.driver.find_element_by_xpath("//*[@id='link']").send_keys(url)
        self.driver.find_element_by_xpath("//*[@id='submit']").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("/html/body/div/div[3]/div/div[1]/div/a[2]").click()

    #FUNCTION TO CHECK FRIENDS WHOM YOU FOLLOW BUT THEY DO NOT FOLLOW YOU
    def whofollowbackyou(self):
        followerlist=instaobj.get_followers_list()
        followinglist=instaobj.get_following_list()
        for item in followinglist:
            if item not in followerlist:
                print(item)

    def check_followers_of_page_or_person(self,page_name):
        self.driver.get(f"https://www.instagram.com/{page_name}")

        followers = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").get_attribute('innerHTML')
        self.beautify_followers_person = BeautifulSoup(followers, 'html.parser')
        self.beautify_followers_person.prettify()
        print(self.beautify_followers_person.text)

        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        scroll_list = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        for i in range(int(self.beautify_followers_person.text.split(" ")[0]) + 100):
            self.driver.execute_script(
                f'arguments[0].scrollTop = arguments[0].scrollHeight/{str((int(self.beautify_followers_person.text.split(" ")[0]) + 101) - i)}',
                scroll_list)

        for i in range(int(self.beautify_followers_person.text.split(" ")[0]) + 100):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll_list)
        followers = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/ul/div")
        beautify_Details = BeautifulSoup(followers.get_attribute('innerHTML'), 'html.parser')
        self.follower_list = []
        for i in beautify_Details.findAll('li', {'class': 'wo9IH'}):
            for j in i.findAll('a', {'class': 'FPmhX notranslate _0imsa'}):
                self.follower_list.append(j.text)
        self.driver.get(f"https://www.instagram.com/{page_name}")
        return self.follower_list


if __name__ == '__main__':
    print("Hello Welcome to instagram Bot By Akshay::")
    print()
    print("1) Login to my account")
    print("2) Give no. of followers,following and posts of my account")
    print("3) Retrieve Followers list")
    print("4) Retrieve Following list")
    print("5) Check in your following list.if  someone  dont follow you")
    print("6) Like Photos by giving hashtags and no. of posts")
    print("7) Like Photos by giving profile exact username and no. of posts one conition here is that account must be public")
    print("8) Check Followers of page or person")
    print("9) Exit\n")
    choice=int(input("Please select operation do u want to perform \n"))
    instaobj=InstaBot()


    if choice==1:
        instaobj.login_section()
        time.sleep(4)
        instaobj.close_section()
    elif choice==2:
        instaobj.login_section()
        instaobj.get_no_of_followers_posts_following()
        instaobj.close_section()
    elif choice ==3:
        instaobj.login_section()
        print("Followers list is\n")
        print(instaobj.get_followers_list())
        instaobj.close_section()
    elif choice==4:
        instaobj.login_section()
        print("Following list is\n")
        print(instaobj.get_following_list())
        instaobj.close_section()
    elif choice ==5:
        instaobj.login_section()
        print("List of people who dont follow you\n")
        instaobj.whofollowbackyou()
        instaobj.close_section()
    elif choice==6:
        hashtag_name = input("Which Hashtags do You want to like?\n")
        no_of_pics = int(input("How many pics do you want to likes?\n"))
        instaobj.login_section()
        instaobj.like_pics_of_particlar_hastags(hashtag_name,no_of_pics)
        instaobj.close_section()
    elif choice ==7:
        page_name = input("Give name of insta page whose posts do you want to likes?\n")
        no_of_pics = int(input("How many pics do you want to likes?\n"))

        instaobj.login_section()
        instaobj.like_pics_of_particlar_page(page_name,no_of_pics)
        instaobj.close_section()
    elif choice==8:
        page_name = input("Give name of insta page whose followers do you want to see?\n")
        instaobj.login_section()
        print(instaobj.check_followers_of_page_or_person(page_name))
        instaobj.close_section()
    elif choice ==9:
        instaobj.close_section()
        exit()
    else:
        print("Invalid Option")

