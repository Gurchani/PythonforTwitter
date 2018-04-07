import oauth2 as oauth
import json

CONSUMER_KEY = '3jlzFiMtjZgNP6mwpbjMtj8U2'
CONSUMER_SECRET = '5TNiXf8e4CAtorYWMw5oRi76JYCbn1HVvT3o90NHlQdrVMsc9M'
ACCESS_KEY = '275605019-eFkeyHZbRx2iGxV3DBoudOgH3uzpaeWep3bvBCSF'
ACCESS_SECRET = 'eTjrgHLAsc5mXajRmfngajJojih8R2KXeBSOe3Jh5JCM0'

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)

#This will get 3200 most recent tweets of a user
recentTweets = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=mlp_officiel&count=3200"
response2, data2 = client.request(recentTweets)

tweets = json.loads(data2)
print len(tweets)
for i in tweets:    
    print i["text"]
    print i["id"]


#This will give the list of 100 people who retweet the user
retweets = "https://api.twitter.com/1.1/statuses/retweeters/ids.json?id=849813577770778624&count=10000&cursor=-1"
response, data = client.request(retweets)

retweets = json.loads(data)

print len(retweets["ids"])
print retweets["next_cursor"]


    
    
