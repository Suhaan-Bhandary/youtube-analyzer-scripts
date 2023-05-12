from youtube_comments import fetchPostComments
from text_analyzer import analyzeText
from spam_detecter import isTextSpam

def main():
    youtube_video_url = 'https://www.youtube.com/watch?v=ZtzAwBzKE7c&ab_channel=SuhaanBhandary'

    dummy = ['you won a lottery send me money to claim a lottery']

    print(isTextSpam(dummy[0]))
    

    print("Running the main function")
    comments = fetchPostComments(youtube_video_url, 10, False)

    for comment in comments:
        print(1)
        print(comment["text"])
        if(isTextSpam(comment["text"][0])):
            print(analyzeText(comment["text"]))

if __name__ == "__main__":
    main()