import praw
import configparser
import csv
import time

config = configparser.ConfigParser()
config.read('rauth.ini')

client_id = config.get('credentials', 'client_id')
client_secret = config.get('credentials', 'client_secret')
r_username = config.get('credentials', 'r_username')
r_password = config.get('credentials', 'r_password')


reddit = praw.Reddit(client_id=client_id, 
					 client_secret=client_secret,
					 user_agent='test',
					 username=r_username,
					 password=r_password)

subreddit = reddit.subreddit('all')


with open('reddit_dataV1.1.csv', 'w', newline='') as csvfile:
	fieldnames = ['Title', 'Author', 'Body']
	write = csv.DictWriter(csvfile, fieldnames=fieldnames)
	write.writeheader()
	for submission in subreddit.hot(limit=5000):
		time.sleep(3)
		print(submission.title + ' ---- Was added to the repo')
		write.writerows([{'Title': submission.title, 'Author': submission.author,'Body': submission.selftext}])
		
csvfile.close()


# for submission in subreddit.hot(limit=1):
# 	print(submission.title)
# 	print(submission.author)
# 	print(submission.comments.list())
