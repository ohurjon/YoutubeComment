import googleapiclient.discovery
from konlpy.tag import Kkma
import key


def getData(videoID="", pageToken=""):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = key.YOUTUBE_API_KEY

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        pageToken=pageToken,
        part="snippet",
        maxResults=100,
        textFormat="plainText",
        videoId=videoID
    )
    response = request.execute()

    return response


if __name__ == "__main__":

    code = 200

    link = input("유튜브 링크나 영상 id를 입력해주세요. : ")

    if link.startswith("http"):
        id = link.split("=")[1]
    elif len(link) == 11:
        id = link
    else:
        print("에러")
        code = 400

    print(id)

    if code == 200:
        data = {}

        for i in getData(videoID=id)["items"]:
            comment = i["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
            kkma = Kkma()
            for noun in kkma.nouns(comment):
                if not data.keys().__contains__(noun):
                    data[noun] = 1
                else:
                    data[noun] += 1
        print(sorted(data.items(), key=lambda item: item[1], reverse=True))


