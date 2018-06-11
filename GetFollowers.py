# This file is primarily used to gather list of twitter 
# followers of "Subject" and puts them in mysql database.

import time
from tweepy import OAuthHandler
import tweepy
import random
import xlwt
import ssl
import pyping
import MySQLdb

ckey = ''
csecret = ''
atoken = ''
asecret = ''

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

subject = "JLMelenchon"
api = tweepy.API(auth)
fw = open(subject + 'Followers.txt','w')


#Database
db = MySQLdb.connect(host="",    # your host, usually localhost
                     user="",         # your username
                     passwd="",  # your password
                     db="",
                     use_unicode=True,
                     charset="utf8")        # name of the data base

cur = db.cursor()



counter = 1


def internet_on():       

        r = pyping.ping('4.2.2.2')
        if r.ret_code == 0:
            print("Internet is alright")
            return True
        else:
            print("Internet is messed up")
            return False


def lookup_user_list(followers_id, api):    
    full_users = []
    users_count = len(followers_id)
    while True:
         try:
             for i in range((users_count / 100) + 1):
                 full_users.extend(api.lookup_users(user_ids=followers_id[i*100:min((i+1)*100, users_count)]))
                 print  ('getting users batch:' + str(i))
                 #Code to Make sure Internet is Connected
                 retry = True    
                 while retry:
                    if internet_on()== True:
                        print ("Connected")
                        retry == False
                        break
                    else :
                        print ("Connection Problems")
                        time.sleep(90)
                 #code to check internet ends here
         except tweepy.TweepError as e:
             print ('Something went wrong, quitting...', e)             
         return full_users

##def saveInNoteBook(idNumbers):
##        for i in range(0 , len(idNumbers)):    
##        fw.write(str(ids[i]) + "\n" )

       
def saveDetails(userDetails):
##        fw.write(str(userDetails) + "\n" )
##        print "Saved"
        InsertQuery = ("") #Put in your Mysql Query
        for i in userDetails:                
                values = (str(i.id), i.screen_name.encode('ascii', 'ignore').decode('ascii'), i.location.encode('ascii', 'ignore').decode('ascii'), i.description.encode('ascii', 'ignore').decode('ascii'), str(i.protected), str(i.verified), i.followers_count, i.friends_count, i.listed_count, i.favourites_count, i.statuses_count, i.created_at, i.time_zone, i.geo_enabled, i.lang)
                cur.execute(InsertQuery, values)
        print "Saved"

       
        
         userObjects = []

for page in tweepy.Cursor(api.followers_ids, screen_name=subject).pages():            
    print ("ids Collected")
    #ids.extend(page)

    userObjects = lookup_user_list(page, api)
    saveDetails(userObjects)
    retry = True    
    while retry:
        if internet_on()== True:
            print ("Connected")
            retry == False
            break
        else :
            print ("Connection Problems")
            time.sleep(90)

print ("Process Complete")


fw.close()
db.close()
