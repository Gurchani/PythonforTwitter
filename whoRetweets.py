#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-retweets
#  - print who has retweeted tweets from a given user's timeline
#-----------------------------------------------------------------------

from twitter import *

user = "MLP_officiel"

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

ckey = '3jlzFiMtjZgNP6mwpbjMtj8U2'
csecret = '5TNiXf8e4CAtorYWMw5oRi76JYCbn1HVvT3o90NHlQdrVMsc9M'
atoken = '275605019-eFkeyHZbRx2iGxV3DBoudOgH3uzpaeWep3bvBCSF'
asecret = 'eTjrgHLAsc5mXajRmfngajJojih8R2KXeBSOe3Jh5JCM0'



#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(atoken, asecret, ckey, csecret))

#-----------------------------------------------------------------------
# perform a basic search 
# twitter API docs: https://dev.twitter.com/rest/reference/get/statuses/user_timeline
#-----------------------------------------------------------------------
results = twitter.statuses.user_timeline(screen_name = user)

#-----------------------------------------------------------------------
# loop through each of my statuses, and print its content
#-----------------------------------------------------------------------
for status in results:
	print "@%s %s" % (user, status["text"])
	

	#-----------------------------------------------------------------------
	# do a new query: who has RT'd this tweet?
	#-----------------------------------------------------------------------
	retweets = twitter.statuses.retweets._id(_id = status["id"], count = "10", cursor = '0')
	for retweet in retweets:
		print " - retweeted by " + (retweet["user"]["screen_name"]) + " Follower count " + str(retweet["user"]["followers_count"]) 		
	break
		
                
