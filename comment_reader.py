import googleapiclient.discovery
import key
import re


def readComment(id, max_comment):
    data = getData(max_comment, videoID=id)

    sort_data = sorted(data, key=lambda x: x[1], reverse=True)
    print(sort_data, "\n\n")

    return data


def getData(max_comments, videoID="", pageToken=""):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = key.YOUTUBE_API_KEY
    comments = []

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)
    while len(comments) < max_comments:
        request = youtube.commentThreads().list(
            pageToken=pageToken,
            part="snippet,replies",
            maxResults=min(100, max_comments - len(comments)),
            textFormat="plainText",
            videoId=videoID
        )
        response = request.execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textOriginal']
            like_count = item['snippet']['topLevelComment']['snippet']['likeCount']

            comment = ' '.join(re.findall(r'[0-9\u3131-\u3163\uac00-\ud7a3]+', comment))
            comments.append((comment, like_count))

        if 'nextPageToken' in response:
            pageToken = response['nextPageToken']
        else:
            break

    return comments[:max_comments]
