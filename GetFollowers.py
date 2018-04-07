# This file is primarily used to gather list of followers
import time
from tweepy import OAuthHandler
import tweepy
import random
import xlwt
import ssl
import pyping
import MySQLdb

ckey = '3jlzFiMtjZgNP6mwpbjMtj8U2'
csecret = '5TNiXf8e4CAtorYWMw5oRi76JYCbn1HVvT3o90NHlQdrVMsc9M'
atoken = '275605019-eFkeyHZbRx2iGxV3DBoudOgH3uzpaeWep3bvBCSF'
asecret = 'eTjrgHLAsc5mXajRmfngajJojih8R2KXeBSOe3Jh5JCM0'

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

subject = "JLMelenchon"
api = tweepy.API(auth)
fw = open(subject + 'Followers.txt','w')
#rF =  open('Random' + subject + 'Follower.txt' , 'w')

#Database
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="twitterapi",
                     use_unicode=True,
                     charset="utf8")        # name of the data base

cur = db.cursor()
##db.set_character_set('utf8')

##cur.execute('SET NAMES utf8;')
##cur.execute('SET CHARACTER SET utf8;')
##cur.execute('SET character_set_connection=utf8;')


##wb = xlwt.Workbook()
##ws = wb.add_sheet('A Test Sheet')



##ws.write(0, 0 , "Screen Name")
##ws.write(0, 1, "Followers Count")
##ws.write(0, 2, "Location")
##ws.write(0, 3, "Friends Count" )
##ws.write(0, 4, "Created At")
##ws.write(0, 5, "Status Count")
##ws.write(0, 6, "Time Zone")
##ws.write(0, 7, "Verified")
##ws.write(0, 8, "lang")
##ws.write(0, 9, "favourites_count")
##ws.write(0, 10, "description")


counter = 1


def internet_on():       

        r = pyping.ping('4.2.2.2')
        if r.ret_code == 0:
            print("Still Holding")
            return True
        else:
            print("Down goes Frazier")
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
        InsertQuery = ("INSERT INTO jlmelenchon "
               "(`id`, `screen_name`, `location`, `description`, `protected`, `verified`, `followers_count`, `friends_count`, `listed_count`, `favourites_count`, `statuses_count`, `created_at`, `time_zone`, `geo_enabled`, `lang`) "
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        for i in userDetails:                
                values = (str(i.id), i.screen_name.encode('ascii', 'ignore').decode('ascii'), i.location.encode('ascii', 'ignore').decode('ascii'), i.description.encode('ascii', 'ignore').decode('ascii'), str(i.protected), str(i.verified), i.followers_count, i.friends_count, i.listed_count, i.favourites_count, i.statuses_count, i.created_at, i.time_zone, i.geo_enabled, i.lang)
                cur.execute(InsertQuery, values)
        print "Saved"
##            ws.write(counter, 0, i.screen_name)
##            ws.write(counter, 1, i.followers_count)
##            ws.write(counter, 2, i.location)
##            ws.write(counter, 3, i.friends_count)
##            ws.write(counter, 4, i.created_at)
##            ws.write(counter, 5, i.statuses_count)
##            ws.write(counter, 6, i.time_zone)
##            ws.write(counter, 7, i.verified)
##            ws.write(counter, 8, i.lang)
##            ws.write(counter, 9, i.favourites_count)
##            ws.write(counter, 10, i.description)
##            global counter
##            counter = counter + 1
       
        
         
#ids = []

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



# userObjects = lookup_user_list(ids, api)


## Get Random Users and their details using the following method
##
##for i in range(0 , len(ids)/50):
##    num = random.randint(0 , len(ids))
##    rF.write(str(i) + " " + str(ids[num]) + "\n")
##    user = api.get_user(str(ids[num]))
##    ws.write(i, 0, user.screen_name)
##    ws.write(i, 1, user.followers_count)
##    ws.write(i, 2, user.location)
##    ws.write(i, 3, user.friends_count)
##    ws.write(i, 4, user.created_at)
##    ws.write(i, 5, user.statuses_count)
##    ws.write(i, 6, user.time_zone)
##    ws.write(i, 7, user.verified)
##    ws.write(i, 3, api.show_friendship(source_screen_name=user.screen_name , target_screen_name = subject))
##    print str(i) + "Screen Name: " + user.screen_name + "NumerOfFollowers " + str(user.followers_count) + "Location: " + str(user.location) + "FriendShip: " + str(api.show_friendship(source_screen_name=user.screen_name , target_screen_name = subject))
##    time.sleep(60)
##    retry = True
##    while retry:
##        if internet_on()== True:
##            print "Connected and Collecting User Details"
##            retry == False
##            break
##        else :
##            print "Connection Problems"
##            time.sleep(30)
## 
##wb.save('FollowerDetail.xls')                                                    
##rF.close()

#wb.save(subject + 'FollowerDetail.xls')

