from youtube_comments import fetchPostComments
from text_analyzer import analyzeText
from spam_detecter import isTextSpam

def printPretty(lines):
    print("---------------------------------------------------------------")
    for line in lines:
        print(line)
        print()
    print("---------------------------------------------------------------\n")


def main():
    youtube_video_url = 'https://www.youtube.com/watch?v=ZtzAwBzKE7c&ab_channel=SuhaanBhandary'    
    comments = fetchPostComments(youtube_video_url, 10, False)

    for comment in comments:
        if(isTextSpam(comment["text"])):
            printPretty([comment["text"], analyzeText(comment["text"])])

if __name__ == "__main__":
    main()