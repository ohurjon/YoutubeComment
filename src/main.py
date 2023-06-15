from util.reader import readComment, getIDListFromFile
from util.sorter import sortComment, labellingComments, addDataInFile
from util.analyzer import analyzeTendencyComment

if __name__ == "__main__":

    idList = getIDListFromFile("src/data/path.txt")

    print("입력된 영상 리스트\n", idList)

    max_comments = int(input("어느 만큼의 댓글을 수집하시겠습니까? : "))
    like = int(input("좋아요 얼마 이상의 댓글을 수집하시겠습니까? : "))

    for videoId in idList:
        data = readComment(videoId, max_comments, like)
        print("가져온 댓글 입니다\n", data)

        percent, data = analyzeTendencyComment(data)
        print("긍 부정 퍼센트\n", percent)
        print("긍 부정이 발린 댓글\n", data)

        data = labellingComments(data)
        print("라벨링 된 댓글\n", data)

        data = sortComment(data)
        print("정렬 된 댓글\n", data)

        addDataInFile(videoId, {"percent": percent, "nouns": data})
