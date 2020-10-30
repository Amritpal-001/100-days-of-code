import tweepy
import time
# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.
from keys import *
import random

# NOTE: flush=True is just for running this script
# with PythonAnywhere's always-on task.
# More info: https://help.pythonanywhere.com/pages/AlwaysOnTasks/
print('this is my twitter bot', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def conditiontoreply(Replyhashtag , MyReply , mentions):
    if Replyhashtag in mention.full_text.lower():
            print('found' , Replyhashtag , flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +  Replyhashtag + MyReply , mention.id)

def conditiontoreply2(Replyhashtag , SpecificWords , MyReply , mentions):
    if Replyhashtag in mention.full_text.lower():
        if SpecificWords in mention.full_text.lower():
            print('found' , Replyhashtag , flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name + Replyhashtag + MyReply , mention.id)

def randomreply(filename):
    b = []
    with open(filename , 'r') as f:
        for a in f:
            b.append(a)
    random_reply = ' ' + random.choice(b)
    #print(random_reply)
    return(random_reply)
#print(randomreply("scripts/COVID.txt"))

Tagname = '#amrit_bot'

def reply_to_tweets():
    print('Retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')

    #print(randomreply("scripts/COVID.txt"))

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)

        if Tagname in mention.full_text.lower():
             if 'COVID' in mention.full_text.lower():
                print('found' , Tagname ,         'responding back...', flush=True)
                api.update_status(('@' + mention.user.screen_name  + randomreply("scripts/COVID.txt")), mention.id)
                print("replied")
        if Tagname in mention.full_text.lower():
            if 'MAMC' in mention.full_text.lower():
                print('found' , Tagname ,         'responding back...', flush=True)
                api.update_status(('@' + mention.user.screen_name + randomreply("scripts/MAMC.txt")) , mention.id)
                print("replied")
        if Tagname in mention.full_text.lower():
            if 'MAMC' not in mention.full_text.lower():
                if 'COVID'  not in mention.full_text.lower():
                    print('found' , Tagname ,         'responding back...', flush=True)
                    api.update_status( ('@' + mention.user.screen_name  + randomreply("scripts/DidntUnderstand.txt")) , mention.id)
                    print("replied")


print('Bot runnning and up')
while True:
    reply_to_tweets()
    time.sleep(20)




