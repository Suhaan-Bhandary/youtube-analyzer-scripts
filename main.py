from youtube_comments import fetchPostComments
from text_analyzer import analyzeText

def main():
    youtube_video_url = 'https://www.youtube.com/watch?v=5eKSQT5mV-c'

    print("Running the main function")
    comments = fetchPostComments(youtube_video_url, 5, True)

    for comment in comments:
        print(comment["text"])
        print(analyzeText(comment["text"]))
        print()

if __name__ == "__main__":
    main()