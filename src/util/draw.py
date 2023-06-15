import matplotlib.pyplot as plt
from matplotlib import font_manager, rc



def drawCircleGraph(value):

    font_path = "C:/Windows/Fonts/NGULIM.TTF"
    font = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font)

    sizes = [value, 1 - value]
    labels = ['긍정', '부정']
    colors = ['#ffc000', '#d395d0']
    explode = [0, 0.05]

    plt.pie(sizes,labels=labels,  colors=colors, startangle=0, autopct='%1.1f%%', explode=explode)

    plt.axis('equal')
    plt.show()
