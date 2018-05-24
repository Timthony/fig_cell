# -*- coding: utf-8 -*-   
#from matplotlib.font_manager import _rebuild
#_rebuild() #reload一下
import numpy as np
import matplotlib.pyplot as plt
import re
import collections
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
data = open('data5-21-2.txt')
datatxt = data.readlines()
#key = r"本次显示的特征点为12个"

p1 = r"本次显示的特征点为\d*个"
pattern1 = re.compile(p1)
p2 = r".*速度为\d*"
pattern2 = re.compile(p2)
p3 = r"当前为第\d*帧"
pattern3 = re.compile(p3)
nodeTempArray = [[]]                                       #二维数组用来存放每次的特征点的个数
frameList = []                                             #存放当前的帧数，和i对应
node_list = []
variance_list = []
#node = np.array()
i = -1
#进行正则匹配
for line in datatxt:
    #print(line)
    matcher1 = re.match(pattern1, line)
    matcher2 = re.match(pattern2, line)
    matcher3 = re.match(pattern3, line)
    if matcher3 and int(re.findall(r"(\W*[0-9]+)\W*", line)[0]) > 143:
        print(line)
        frameList.append(line)
    elif matcher1:
        print(matcher1.group())
        #取出匹配到内容数字，即本次显示的特征点有多少个
        k = int(re.findall(r"(\W*[0-9]+)\W*", line)[0])
        print(k)
        i = i + 1
        nodeTempArray.append([])
        #正则表达式匹配，该行下面的k行，进行数字提取，提取出速度
        #nodeTempArray = []                       # 存放每次用来画图的点
    elif matcher2:
        #print("222")
        nodeTemp0 = re.findall(r"(\W*[0-9]+)\W*", line)
        nodeTemp = float(str(nodeTemp0[0] + '.' + nodeTemp0[1]))
        # re.findall(pattern, string)返回与string中所有与pattern相匹配的全部字符串，返回形式为数组
        #nodeTemp = float(re.findall(r"(\W*^(-?\d+)(\.\d+)?$)\W*", line)[0])
        nodeTempArray[i].append(nodeTemp)
    else:
        continue
# =============================================================================
 #画图，所有的特征点的速度都保存在nodeTempArray中了
 #nodeTempArray存放了n组点的速度，frameList存放了n个当前为多少帧，一一对应
 #画出具有代表性的一些帧的图片，每一次取点，每隔10帧画一幅图，画五幅图为止
#x = np.arange(-5, 10)
#y = nodeTempArray[50]          #[0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1]
 

for i in range(1, len(nodeTempArray)-1):# 计算每一帧的均值和方差并且显示出来
    node = np.array(nodeTempArray[i])
    mean_value = node.mean()
    node_list.append(mean_value)         # 存放速度均值的列表
    variance = node.var()
    variance_list.append(variance)       # 存放速度方差的列表


    # # 画出每一帧的速度分布图
    # yTemp = collections.Counter(nodeTempArray[i])
    # xArray = []
    # yArray = []
    # for x in yTemp:
    #     xArray.append(x)
    #     yArray.append(yTemp[x])
    # plt.bar(xArray, yArray, width = 0.06, facecolor='#9999ff',edgecolor='white',)
    # a = zip(xArray, yArray)
    # # for x,y in a:
    # #     plt.text(x, y+0.1, '%d'%y, ha='center', va='bottom')
    # plt.xlabel("速度")
    # plt.ylabel("数量")
    # # 求xArray的中位数
    # xArray.sort()
    # half = int(len(xArray)/2)
    # halfNum = int((xArray[half] + xArray[~half])/2)
    # plt.xlim(halfNum - 5, halfNum + 5)
    # plt.ylim((0, 45))
    # plt.xticks(np.arange(halfNum - 5, halfNum + 5.5, 1))
    # plt.yticks(np.arange(0, 45, 5))
    # #设置x,y轴范围
    # titleTemp=str(frameList[i])
    # plt.title(titleTemp)
    # #plt.title("当前为第%d帧", frameList[i])
    #
    # plt.text(halfNum+3, 43, "均值：%f"%mean_value, fontsize = 12, verticalalignment = 'center', horizontalalignment = 'center')
    # plt.text(halfNum+3, 40, "方差：%f"%variance, fontsize = 12, verticalalignment = 'center', horizontalalignment = 'center')
    #
    # fig_name = str(titleTemp+'.jpg')
    # fig_save = str('/Users/arcstone_mems_108/PycharmProjects/tu1/save/' + fig_name)
    # plt.savefig(fig_save, format = 'png', dpi = 300)
    # plt.show()
    # plt.clf()
    # #画速度的均值和方差图像，

# =============================================================================
# 画出整个过程的速度，方差变化图
x = range(144, 178)
plt.figure(figsize=(7, 10))
print(len(node_list))
plt.subplot(2, 1, 1)
plt.title("速度变化图")
plt.xlabel("当前帧")
plt.ylabel("速度")
plt.plot(x, node_list)



plt.subplot(2, 1, 2)
plt.xlabel("当前帧")
plt.ylabel("方差")
plt.title("方差变化图")

plt.plot(x, variance_list)
plt.show()


# =============================================================================
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
