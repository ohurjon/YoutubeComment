import googleapiclient.discovery
from konlpy.tag import Kkma

import data
import key

kkma = Kkma()


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

    f = open("data/data.txt", 'w')
    f.close()

    # path = input("유튜브 링크나 영상 id가 적힌 TXT 파일의 경로를 입력해주세요. : ")

    with open("data/path.txt", "r") as f:
        links = [N.strip() for N in f.readlines()]
    f.close()

    for link in links:
        if link.startswith("http"):
            id = link.split("=")[1]
        elif len(link) == 11:
            id = link
        else:
            code = 400
            raise ValueError

        if code == 200:
            print("입력된 영상 id : " + id)
            nouns = {}

            for i in getData(videoID=id)["items"]:
                comment = i["snippet"]["topLevelComment"]["snippet"]["textOriginal"]

                for noun in kkma.nouns(comment):

                    if len(noun) >= 2:
                        if not nouns.keys().__contains__(noun):
                            nouns[noun] = 1
                        else:
                            nouns[noun] += 1
            for i in list(nouns.keys()):
                if i in data.abuse:
                    del nouns[i]
            sorted_data = sorted(nouns.items(), key=lambda item: item[1], reverse=True)
            print(sorted_data)
            f = open("data/data.txt", 'a')
            f.write(f"{id} \n {sorted_data} \n")
            f.close()
