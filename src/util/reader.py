from googleapiclient.discovery import build
from src.data import key
import re

youtube = build("youtube", "v3", developerKey=key.YOUTUBE_API_KEY)


def getIDListFromFile(path):
    links = []
    file = open(path, "r")

    for link in file.readlines():
        links.append(linkToId(link))

    file.close()

    return links


def linkToId(link):
    if link.startswith("http"):
        link = link.split("=")[1].split("&")[0]
    else:
        raise ValueError

    return link


def readComment(videoID, maxComments, lineLike):
    comments = []
    pageToken = ""

    while len(comments) < maxComments:
        request = youtube.commentThreads().list(
            pageToken=pageToken,
            part="snippet,replies",
            maxResults=min(100, maxComments - len(comments)),
            textFormat="plainText",
            videoId=videoID
        )
        response = request.execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
            like_count = item['snippet']['topLevelComment']['snippet']['likeCount']

            if like_count > lineLike:
                comment = ' '.join(re.findall(r'[0-9\u3131-\u3163\uac00-\ud7a3]+', comment))
                comments.append((comment, like_count))

        if 'nextPageToken' in response:
            pageToken = response['nextPageToken']
        else:
            break

    return comments
