from instabot import Bot
bot = Bot()

username = input(str("enter your username: "))
password = input(str("enter your password: "))

bot.login(username=username,password=password)

print("""you can use this robot for:
      1-follow user
      2-send a post
      3-unfollow user
      4-send message
      5-give information for followers some user
      6-give information for following some user
      """)
kod = input("enter your number of choice: ")

def follow():
    page = input("enter your target page: ")
    bot.follow(page)
    
def post():   
    caption = input("enter your caption for this post: ")
    path = input("enter your picture address in pc: ")
    bot.upload_photo(path,caption=caption)
    
def unfollow():
    page = input("enter your target page: ")
    bot.unfollow(page)
    
def send_message():    
    message = input("enter your message: ")
    contact = input('enter your contact: ')
    bot.send_message(message,[contact])
    
def give_followers_information():
    target = input("enter your taget: ")
    followers = bot.get_user_followers(target)
    for follower in followers:
        print(bot.get_user_info(follower))
        
def give_following_information():
    target = input("enter your taget: ")
    following = bot.get_user_following(target)
    for user in following:
        print(bot.get_user_info(user))
    
def aval(kod):
    if kod == 1:
        follow()
    elif kod == 2:
        post()
    elif kod == 3:
        unfollow()
    elif kod == 4:
        send_message()
    elif kod == 5:
        give_followers_information()
    elif kod == 6:
        give_following_information()
        

    