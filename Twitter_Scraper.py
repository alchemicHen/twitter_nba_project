#Creates a scraper that searches and parses the 30 day twitter search of a query.

import tweepy

class TweetScraper(object):
    
    api = False
    bearer = 'AAAAAAAAAAAAAAAAAAAAAH6nYwEAAAAAK%2BezpbKj7NUWoAMW6SbFOfFruD4%3Dj134xtdV6I1kcGl4a1wnAaa7N2W0hQCA9avu7sDyvEEVWjIwmy'
    
    def __init__(self, token = bearer, api=api):
        
        auth = tweepy.OAuth2BearerHandler(token)
        api = tweepy.API(auth)
    
    def searchTweets(self, query = 'NBA'):
        data = []
        
        searchedTweets = self.api.search_30_day(query)
        
        for item in searchedTweets:
            mined = {
                    'tweet_id':        item.id,
                    'name':            item.user.name,
                    'screen_name':     item.user.screen_name,
                    'retweet_count':   item.retweet_count,
                    'text':            item.text,
                    'hashtags':        item.entities['hashtags'],
                    'location':        item.place,
                    'is_verified':     item.user.verified
            }
            try:
                    mined['retweet_text'] = item.retweeted_status.full_text
            except:
                    mined['retweet_text'] = 'None'
            try:
                    mined['quote_text'] = item.quoted_status.full_text
                    mined['quote_screen_name'] = status.quoted_status.user.screen_name
            except:
                    mined['quote_text'] = 'None'
                    mined['quote_screen_name'] = 'None'
            
            data.append(mined)
            
            return data