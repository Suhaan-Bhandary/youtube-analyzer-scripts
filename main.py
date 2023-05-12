import json
from youtube_comments import getCommentsFiltered
from review import getVideoStatistics


def main():
    youtube_video_url = "https://www.youtube.com/watch?v=n9XX_zz3bi8"

    comments = getCommentsFiltered(youtube_video_url, 10, True)
    positive_comments_count = len(comments["positive_comments"])
    negative_comments_count = len(comments["negative_comments"])

    video_statistics = getVideoStatistics(youtube_video_url)

    data = {
        "comments": comments,
        "isVideoGood": (video_statistics["likes"] >= video_statistics["views"] / 1000) and positive_comments_count > negative_comments_count,
        "message": "Successful"
    }

    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
