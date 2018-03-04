# PRAW_Scraping
This is a program used to pull reddit submissions form r/all.

I am using Python 3.6 for this script. This purpose is to pull textual data form reddit. Submission, Submission Author and Submission Body text. Currently I am writing it to a CSV on an external but I to move to an SQL database soon. 

you will need
#configparse, praw

You comment out the Configparse section if you wish to just hard code in your Client ID and Client Secret. 

The format of the rauth.ini file is as follows

[credentials]       
client_id=      
client_secret=      
r_username=     
r_password=     

make sure you do not add a space or ' ' or " " to the argurments of it will not work. 
