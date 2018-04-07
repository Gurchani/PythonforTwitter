import tweepy

ckey = '3jlzFiMtjZgNP6mwpbjMtj8U2'
csecret = '5TNiXf8e4CAtorYWMw5oRi76JYCbn1HVvT3o90NHlQdrVMsc9M'
atoken = '275605019-eFkeyHZbRx2iGxV3DBoudOgH3uzpaeWep3bvBCSF'
asecret = 'eTjrgHLAsc5mXajRmfngajJojih8R2KXeBSOe3Jh5JCM0'

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
