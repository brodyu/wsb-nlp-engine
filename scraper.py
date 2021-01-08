import praw
from praw.models import MoreComments
import matplotlib.pyplot as plt

# Creates a set of stock tickers in NASDAQ
def nasdaq_tickers():
    fin = open("nasdaqtraded.txt", 'r')
    tickers = set()
    fin.readline()
    for line in fin.readlines():
        line = line[2:]
        tickers.add(line[:line.index("|")])
    return tickers

# Iterates through only head comments 
def iter_top_level(comments):
    for top_level_comment in comments:
        if isinstance(top_level_comment, MoreComments):
            yield from iter_top_level(top_level_comment.comments())
        else:
            yield top_level_comment

def ticker_count():
    reddit = praw.Reddit(client_id = "wdBkk26fOdnn8A", client_secret = "vZM36gyWG2txWPCzujGN54WSRVkbWg", user_agent = "windows:com.example.myredditapp:v0.0.1 (by u/Exciting-Cat-8314")
    counter = 0
    # People may use use words that happen to be real ticker names
    flagged_words = ["YOLO", "PUMP", "RH", "EOD", "IPO", "ATH", "ARE", "OR", "OUT", "IT", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", 
        "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    ticker_set = nasdaq_tickers()
    tickers = {}
    # Enter the url of daily discussion post
    url = "https://www.reddit.com/r/wallstreetbets/comments/ksmmx6/what_are_your_moves_tomorrow_january_08_2021/"
    submission = reddit.submission(url=url)
    print(submission.title)
    for comment in iter_top_level(submission.comments): 
        # set how many comments you want to search
        if counter == 1000:
            return tickers
        for word in comment.body.split():
            if word == word.upper() and word in ticker_set and word not in flagged_words:
                if word not in tickers:
                    tickers[word] = 1
                else:
                    tickers[word] += 1
        counter += 1
        counter += 1
    return tickers

def popularTickers():
    result = ticker_count()
    x = []
    y = []
    for a, b in result.items():
        # Can change value to see choose the threshold stock mention count 
        if b > 0:
            x.append(a)
            y.append(b)
    # Uncomment to see a pie graph 
    fig1, ax1 = plt.subplots()
    ax1.pie(y, labels=x, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()
    return x, y
print(popularTickers)