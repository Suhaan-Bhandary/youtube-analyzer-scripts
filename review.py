from googleapiclient.discovery import build

# Define the YouTube API client
api_key = 'AIzaSyDLzoqpEmFqttF3HDprXGR5eXphBUX5lo4'
youtube = build('youtube', 'v3', developerKey=api_key)

# Define the video ID for the video you want to analyze
video_link = "https://www.youtube.com/watch?v=n9XX_zz3bi8"

#good link ZyKwNDV_9M4
#bad link n9XX_zz3bi8
video_id = video_link.split('=')[1]

# Use the YouTube API to retrieve the video statistics
video_response = youtube.videos().list(
    part='statistics',
    id=video_id
).execute()

# Get the number of views and likes for the video
views = int(video_response['items'][0]['statistics']['viewCount'])
likes = int(video_response['items'][0]['statistics']['likeCount'])

# # Determine if the video is good or bad based on the number of likes
# if likes >= 10000 and views >= 50000:
#     print('The video is good.')
# else:
#     print('The video is bad.')
