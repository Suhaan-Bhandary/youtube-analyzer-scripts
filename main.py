import json
from youtube_comments import fetchPostComments
from text_analyzer import analyzeText
from spam_detecter import isTextSpam
from review import views as review_views
from review import likes as review_likes

global positive_comments_count
global negative_comments_count

positive_comments_count = 0
negative_comments_count = 0

def printPretty(lines):
    print("---------------------------------------------------------------")
    for line in lines:
        print(line)
        print()
    print("---------------------------------------------------------------\n")


def getCommentsFiltered(youtube_video_url, count, sort_by_most_popular):
    global positive_comments_count
    global negative_comments_count
    
    comments = fetchPostComments(youtube_video_url, count, sort_by_most_popular)

    spam_comments = []
    positive_comments = []
    negative_comments = []
    neutral_comments = []

    for comment in comments:
        comment_text = comment["text"]
        comment_analyze_data = analyzeText(comment_text)

        if isTextSpam(comment_text):
            spam_comments.append({
                "comment": comment,
                "analytics": comment_analyze_data
            })
            continue

        if comment_analyze_data["sentiment"] > 0:
            positive_comments_count+=1
            positive_comments.append({
                "comment": comment,
                "analytics": comment_analyze_data
            })

        elif comment_analyze_data["sentiment"] < 0:
            negative_comments.append({
                "comment": comment,
                "analytics": comment_analyze_data
            })
            negative_comments_count+=1
        else:
            neutral_comments.append({
                "comment": comment,
                "analytics": comment_analyze_data
            })

    return {
        "spam_comments": spam_comments,
        "positive_comments": positive_comments,
        "negative_comments": negative_comments,
        "neutral_comments": neutral_comments,
    }

def main():
    global positive_comments_count
    global negative_comments_count
    
    youtube_video_url = 'https://www.youtube.com/watch?v=1u08QZyjguo'
    comments = getCommentsFiltered(youtube_video_url, 10, True)
    print(json.dumps({"comments": comments, "message": "Successful"}, indent=2))

    if review_likes>=10000 and review_views>=500000 and positive_comments_count>negative_comments_count:
        print("video is good")
    else: 
        print("video is bad")


if __name__ == "__main__":
    main()
