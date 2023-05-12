from itertools import islice
from youtube_comment_downloader import *

def fetchPostComments(youtube_video_url, total_comment_count, sort_by_most_popular=False):
    downloader = YoutubeCommentDownloader()

    # Whether to download popular (0) or recent comments (1). Defaults to 1
    sort_by = 0 if sort_by_most_popular else 1

    # Fetch the comments
    comments_iterator = downloader.get_comments_from_url(youtube_video_url, sort_by=sort_by)

    # Comments array
    comments = []

    # Show the comments
    for comment in islice(comments_iterator, total_comment_count):
        comments.append(comment)

    return comments

