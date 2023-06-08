import googleapiclient.discovery
from konlpy.tag._okt import Okt
import key
import re

okt = Okt()

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

def scoring_comments(data):
    okt = Okt()
    count = {}
    count_x_likes = {}

    for comment, likes in data:
        nouns = okt.nouns(comment)
        if likes >= 5:
            for noun in nouns:
                if len(noun) <= 1:
                    pass
                else:
                    if not count.keys().__contains__(noun):
                        count[noun] = 1
                    else:
                        count[noun] += 1
                    if not count_x_likes.keys().__contains__(noun):
                        count_x_likes[noun] = likes
                    else:
                        count_x_likes[noun] += likes



    return count, count_x_likes


if __name__ == "__main__":

    code = 200

    f = open("data/data.txt", 'w')
    f.close()

    with open("data/path.txt", "r") as f:
        links = [N.strip() for N in f.readlines()]
    f.close()

    for link in links:
        if link.startswith("http"):
            id = link.split("=")[1].split("&")[0]
        elif len(link) == 11:
            id = link
        else:
            print("에러")
            code = 400

        print(id)

        if code == 200:
            max_comments = 500
            max_comments = int(input("어느만큼 댓글을 수집하시겠습니까? : "))

            data = getData(max_comments, videoID=id)

            sort_data = sorted(data, key=lambda x: x[1], reverse=True)
            print(sort_data,"\n\n")

            count, count_x_likes = scoring_comments(data)

            sort_count = sorted(count.items(), key=lambda item: item[1], reverse=True)
            sort_count_x_likes = sorted(count_x_likes.items(), key=lambda item: item[1], reverse=True)

            print(sort_count, "\n\n", sort_count_x_likes, "\n\n\n")

            f = open("data/data.txt",'a')
            f.write(f"{id} \n\n {sort_count} \n\n {sort_count_x_likes} \n\n\n")
            f.close()