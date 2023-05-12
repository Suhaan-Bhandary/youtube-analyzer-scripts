import json
from youtube_comments import fetchPostComments
from text_analyzer import analyzeText
from spam_detecter import isTextSpam


def printPretty(lines):
    print("---------------------------------------------------------------")
    for line in lines:
        print(line)
        print()
    print("---------------------------------------------------------------\n")


def getCommentsFiltered(youtube_video_url, count, sort_by_most_popular):
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
            positive_comments.append({
                "comment": comment,
                "analytics": comment_analyze_data
            })
        elif comment_analyze_data["sentiment"] < 0:
            negative_comments.append({
                "comment": comment,
                "analytics": comment_analyze_data
            })
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
    youtube_video_url = 'https://www.youtube.com/watch?v=1u08QZyjguo'
    comments = getCommentsFiltered(youtube_video_url, 10, True)
    print(json.dumps({"comments": comments, "message": "Successful"}, indent=2))


if __name__ == "__main__":
    main()
