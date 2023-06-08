#
#
# import googleapiclient.discovery
# from konlpy.tag import Kkma
#
# import data
# import key
#
# kkma = Kkma()
#
#
# # 대충 수정된 부분
# def getData(videoID="", pageToken=""):
#     api_service_name = "youtube"
#     api_version = "v3"
#     DEVELOPER_KEY = key.YOUTUBE_API_KEY
#
#     youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)
#
#     request = youtube.commentThreads().list(
#         pageToken=pageToken,
#         part="snippet",
#         maxResults=100,
#         textFormat="plainText",
#         videoId=videoID
#     )
#     response = request.execute()
#
#     return response
#
#
# if __name__ == "__main__":
#     code = 200
#
#     link = input("유튜브 링크나 영상 id를 입력해주세요. : ")
#
#     if link.startswith("http"):
#         id = link.split("=")[1]
#     elif len(link) == 11:
#         id = link
#     else:
#         code = 400
#         raise ValueError
#
#     if code == 200:
#         print("입력된 영상 id: " + id)
#         word = input("단어를 입력하세요: ")
#         found_comments = []
#
#         for i in getData(videoID=id)["items"]:
#             comment = i["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
#
#             if word in comment:
#                 found_comments.append(comment)
#
#         if found_comments:
#             print("'%s' 단어가 포함된 댓글들:" % word)
#             for comment in found_comments:
#                 print(comment)
#         else:
#             print("'%s' 단어가 포함된 댓글이 없습니다." % word)
import googleapiclient.discovery
from konlpy.tag import Kkma

import data
import key

kkma = Kkma()


# 대충 수정된 부분
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


def getCommentLikes(comment_id):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = key.YOUTUBE_API_KEY

    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = youtube.comments().list(
        part="snippet",
        id=comment_id
    )
    response = request.execute()

    return response["items"][0]["snippet"]["likeCount"]


if __name__ == "__main__":
    code = 200

    link = input("유튜브 링크나 영상 id를 입력해주세요. : ")

    if link.startswith("http"):
        id = link.split("=")[1]
    elif len(link) == 11:
        id = link
    else:
        code = 400
        raise ValueError

    if code == 200:
        print("입력된 영상 id: " + id)
        word = input("단어를 입력하세요: ")
        found_comments = []

        for i in getData(videoID=id)["items"]:
            comment_id = i["snippet"]["topLevelComment"]["id"]
            comment = i["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
            likes = getCommentLikes(comment_id)

            if word in comment:
                found_comments.append((comment, likes))

        if found_comments:
            print("'%s' 단어가 포함된 댓글들 (좋아요 순):" % word)
            sorted_comments = sorted(found_comments, key=lambda x: x[1], reverse=True)
            for comment, likes in sorted_comments:
                print(f"좋아요: {likes}, 댓글: {comment}")
        else:
            print("'%s' 단어가 포함된 댓글이 없습니다." % word)
