import comment_reader
import comment_sorting
import comment_analyze

if __name__ == "__main__":

    code = 200

    file = open("data/path.txt", "r")
    links = [N.strip() for N in file.readlines()]
    file.close()

    file = open("data/data.txt", "w")
    file.close()

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

            max_comments = int(input("어느만큼 댓글을 수집하시겠습니까? : "))
            like = int(input("좋아요 얼마 이상 댓글을 수집하시겠습니까? : "))

            data = comment_reader.readComment(id, max_comments)

            data = comment_analyze.analyze_comment(data)

            result = comment_sorting.sortComment(data, like)

            f = open("data/data.txt", 'a')
            f.write(f"{id}\n{result}\n\n")
            f.close()
