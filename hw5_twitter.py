from requests_oauthlib import OAuth1
import json
import sys
import requests
import secret_data # file that contains OAuth credentials
import nltk # uncomment line after you install nltk
from collections import Counter
from nltk.corpus import stopwords
import re

## SI 507 - HW
## Amy Newman
## COMMENT WITH:
## Your section day/time: Thursday 4PM
## Any names of people you worked with on this assignment:

#usage should be python3 hw5_twitter.py <username> <num_tweets>
username = sys.argv[1]
num_tweets = sys.argv[2]

consumer_key = secret_data.CONSUMER_KEY
consumer_secret = secret_data.CONSUMER_SECRET
access_token = secret_data.ACCESS_KEY
access_secret = secret_data.ACCESS_SECRET

#Code for OAuth starts
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)
requests.get(url, auth=auth)
#Code for OAuth ends

#Write your code below:
#Code for Part 3:Caching
#Finish parts 1 and 2 and then come back to this


### 1. Make a call to the API
###     a. fetch 25 tweets from Twitter
### 2. Create code that caches all of the tweets
### 3. filter through the analyzed tweets to find the most common 5 words
### 4. Sample output is below:
    # SAMPLE OUTPUT: mwnewman$ python3 hw5_twitter.py umsi 50 USER: umsi
    # TWEETS ANALYZED: 50 5 MOST FREQUENT WORDS: umsi(8) being(3) is(3) improve(2) Join(2)

#Code for Part 1:Get Tweets
def get_tweets_from_Twitter(username, num_tweets):
    base_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = {}
    params['screen_name'] = username
    params['count'] = num_tweets
    response_obj = requests.get(base_url, params, auth=auth)
    response_dict = json.loads(response_obj.text)
    # file_object = open('tweets.json', 'w')
    # file_object.write(json.dumps(response_dict, sort_keys=True, indent=2)) #dumps makes a json file
    # file_object.close()
    return response_dict

# print(response_obj)
# print(response_dict)

#print(len(get_tweets_from_Twitter('UMSI', 25))) #-- this gives me back 25 dictionary items of tweets, etc.

tweet_objects = get_tweets_from_Twitter('UMSI', 25)
tweets = [] #this will give a list of tweets that i can use to find the most common 5 words later
for tweet in tweet_objects:  #this will iterate over all of the tweet_objects and give back the username and text only
    tweets.append(tweet['text'])
#print(tweets)

tweet_list = ",".join(tweets).replace(':', '').replace('https', '').replace(',','') #this creates 1 string of all of the tweets that I can use to tokenize using nltk
# print(tweet_list)
# print(len(tweet_list))

tokens = nltk.word_tokenize(tweet_list) #this creates a list of tokens that can be used as input for Counter()
# print(tokens)

clean_lst = []
for token in tokens:
    alpha_only = re.sub(r"([^a-zA-Z])+", '', token)
    clean_http = re.sub(r"(['http'])", '', alpha_only)
    clean_https = re.sub(r"(['https'])", "", clean_http)
    clean_lst.append(clean_https)

tweet_freq_dict = Counter(clean_lst)
print(tweet_freq_dict)


## 1. join the lists into a string
##      a. tokenize using nltk
## 2. find the frequency of tokens


# combined_tweet_list = []
# for combined in tweets:
#     combined_tweet_list.extend(combined)
# print(combined_tweet_list)


#print(tweets)
#print(len(tweets)) #this is 25
# tweet_no_handle =[]
# for remove_handle in tweets:
#     tweet_no_handle.append(nltk.tokenize.casual.remove_handles(remove_handle))
# print(tweet_no_handle)





# create a json file for cache

# .......................................
# have to iterate through - printing out the most common words of each tweet
# .......................................
# ..............................
## is alpha function.............
# .......................................


#Code for Part 2:Analyze Tweets

# def get_tweets(section):
#     baseurl = 'https://api.nytimes.com/svc/topstories/v2/'
#     extendedurl = baseurl + section + '.json'
#     params={'api-key': nyt_key}
#     CACHE_FNAME = 'cache_file_name.json'
#     try:
#         cache_file = open(CACHE_FNAME, 'r')
#         cache_contents = cache_file.read()
#         CACHE_DICTION = json.loads(cache_contents)
#         cache_file.close()
#
#     # if there was no file, no worries. There will be soon!
#     except:
#         CACHE_DICTION = {}



### Write code here that gathers the 5 most common words that appear in the analyzed tweets


if __name__ == "__main__":
    if not consumer_key or not consumer_secret:
        print("You need to fill in client_key and client_secret in the secret_data.py file.")
        exit()
    if not access_token or not access_secret:
        print("You need to fill in this API's specific OAuth URLs in this file.")
        exit()
