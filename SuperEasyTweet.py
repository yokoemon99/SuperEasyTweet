import tweepy
import webbrowser
import tkinter as tk

def get_user():
    global user_access_token
    global user_access_token_secret
    global username
    global consumer_key
    global consumer_secret

    consumer_key = '8vFdOkz0BOwwKCpkmB8kw8Dvz'
    consumer_secret = '88Y9wKk9LaiweHoEacF4V8wswYfMbqSMd1UMzFBIN0IAmw31BY'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback='oob')
    auth_url = auth.get_authorization_url()
    webbrowser.open(auth_url)
    verifier = input('PIN: ').strip()
    auth.get_access_token(verifier)
    print(auth.access_token)
    user_access_token = auth.access_token
    print(auth.access_token_secret)
    user_access_token_secret = auth.access_token_secret

    auth.set_access_token(auth.access_token, auth.access_token_secret)
    api = tweepy.API(auth)
    username = api.me().name
    print(str(username))

def tweet():
    global user_access_token
    global user_access_token_secret
    global username
    global consumer_key
    global consumer_secret

    user_tweepy = tweepy.OAuthHandler(consumer_key, consumer_secret)
    user_tweepy.set_access_token(user_access_token, user_access_token_secret)
    user_tweet = tweepy.API(user_tweepy)
    user_tweet.update_status("うんち！")

root = tk.Tk()
root.title("SuperEasyTweet")
root.geometry("480x360+-1000+10")
get_user()
tweet()
root.mainloop()