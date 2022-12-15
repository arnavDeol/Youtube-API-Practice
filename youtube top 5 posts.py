import requests

# Replace the value of the `api_key` variable with your own YouTube API key
api_key = "<api_key>"

# Replace the value of the `channel_id` variable with the ID of the channel
# whose top posts you want to retrieve
channel_id = "<channel_id>"

# Set the number of posts you want to retrieve
number_of_posts = 5

# Construct the URL for the API request
request_url = (
    f"https://www.googleapis.com/youtube/v3/search?"
    f"key={api_key}"
    f"&channelId={channel_id}"
    f"&part=snippet"
    f"&maxResults={number_of_posts}"
    f"&order=date"
    f"&type=video"
)

# Send the API request and store the response
response = requests.get(request_url)
print(response.status_code)

# Print the title of each post
if response.status_code == 200:
    for post in response.json()["items"]:
        print(post["snippet"]["title"])
else:
    print("An error occurred")
