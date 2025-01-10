from etls.reddit_etl import connect_reddit
from utils.constants import CLIENT_ID, SECRET

instance = connect_reddit(CLIENT_ID, SECRET, 'Test Agent')
print("Connection successful!")

# Output: 
# Version 7.7.1 of praw is outdated. Version 7.8.1 was released Friday October 25, 2024.
# connected to reddit!
# Connection successful!