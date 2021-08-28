import os
import tweepy
import statsapi
from dotenv import load_dotenv

load_dotenv()

# Global variables for the Twitter API
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET_TOKEN = os.getenv('ACCESS_SECRET_TOKEN')

# Authenticating on Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
api = tweepy.API(auth)
