from instagrapi import Client
import time

# Set your Instagram username and password
username = "your_username"
password = "your_password"

# Set up the Instagrapi client
client = Client()
client.login(username, password)

# Get the user input for the target username
target_username = input("Enter the target username: ")

# Get the user ID of the target user
target_id = client.user_id_from_username(target_username)

# Get the follower count of the target user
target_user_info = client.user_info_by_username(target_username)
follower_count = target_user_info.follower_count

# Iterate through all the followers of the target user and print their usernames
batch_size = 15
end_cursor = None
while True:
    followers_chunk, end_cursor = client.user_followers_gql_chunk(target_id, max_amount=batch_size, end_cursor=end_cursor)
    for follower in followers_chunk:
        print(follower.username)
    time.sleep(5)
    if not end_cursor:
        break

# Log out of Instagram
client.logout()
