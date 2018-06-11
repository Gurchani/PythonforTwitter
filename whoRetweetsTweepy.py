#Tells you who retweets a perticlar profile

import tweepy

ckey = ''
csecret = ''
atoken = ''
asecret = ''

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

firstTweet = api.user_timeline("MLP_officiel")[0]
print firstTweet.text
print firstTweet.id
results = api.retweets(firstTweet.id, 400) 
for i in results:
    print i.user.screen_name

for page in tweepy.Cursor(api.retweets(firstTweet.id)).pages():
    print page
