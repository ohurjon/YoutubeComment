from konlpy.tag import Okt


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


def sortComment(data):

    count, count_x_likes = scoring_comments(data)

    sort_count = sorted(count.items(), key=lambda item: item[1], reverse=True)
    sort_count_x_likes = sorted(count_x_likes.items(), key=lambda item: item[1], reverse=True)

    print(sort_count, "\n\n", sort_count_x_likes, "\n\n\n")