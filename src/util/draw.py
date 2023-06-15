import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


def drawCircleGraph(value):
    font_path = "./data/Maplestory Bold.ttf"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font, size=20)

    sizes = [value, 1 - value]
    labels = ['긍정', '부정']
    colors = ['#ffc000', '#d395d0']
    explode = [0, 0.05]

    plt.pie(sizes, labels=labels, colors=colors, startangle=0, autopct='%1.1f%%', explode=explode)
    plt.axis('equal')
    plt.show()


def drawCircleGraphAndTable(percent, positive, negative, ps, ns):
    fig, ax = plt.subplots(figsize=(6, 9))

    font_path = "./data/Maplestory Bold.ttf"
    font = font_manager.FontProperties(fname=font_path)
    font.set_size(25)
    rc('font', family=font.get_name(), size=20)
    
    sizes = [percent, 1 - percent]
    labels = ['긍정', '부정']
    colors = ['#ffc000', '#d395d0']
    explode = [0, 0.05]

    ax.pie(sizes, labels=labels, colors=colors, startangle=0, autopct='%1.1f%%', explode=explode)
    ax.axis('off')
    ax.set_title("영상 정보",fontproperties=font)

    table = ax.table(cellText=[positive, ps,negative,ns], rowLabels=["긍정","점수","부정","점수"], fontsize=10, colWidths=[0.2, 0.2, 0.2],rowLoc="center")
    table.scale(1, 2.3)
    for key, cell in table.get_celld().items():
        cell.set_linewidth(0)

    plt.show()
