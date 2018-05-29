# -*- coding: utf-8 -*-   
#from matplotlib.font_manager import _rebuild
#_rebuild() #reload一下
import numpy as np
import matplotlib.pyplot as plt
import re
import collections
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#==========================================【数据读入模块】=========================================
data1_1 = open('/Users/arcstone_mems_108/Desktop/keyan/githubproject/fig_cell/datatxt/data1_1.txt')
datatxt1_1 = data1_1.readlines()
data1_2 = open('/Users/arcstone_mems_108/Desktop/keyan/githubproject/fig_cell/datatxt/data1_2.txt')
datatxt1_2 = data1_2.readlines()
data1_3 = open('/Users/arcstone_mems_108/Desktop/keyan/githubproject/fig_cell/datatxt/data1_3.txt')
datatxt1_3 = data1_3.readlines()
data1_4 = open('/Users/arcstone_mems_108/Desktop/keyan/githubproject/fig_cell/datatxt/data1_4.txt')
datatxt1_4 = data1_4.readlines()
data1_5 = open('/Users/arcstone_mems_108/Desktop/keyan/githubproject/fig_cell/datatxt/data1_5.txt')
datatxt1_5 = data1_5.readlines()
data1_6 = open('/Users/arcstone_mems_108/Desktop/keyan/githubproject/fig_cell/datatxt/data1_6.txt')
datatxt1_6 = data1_6.readlines()
data1_7 = open('/Users/arcstone_mems_108/Desktop/keyan/githubproject/fig_cell/datatxt/data1_7.txt')
datatxt1_7 = data1_7.readlines()
# data1_8 = open('/Users/arcstone_mems_108/Desktop/keyan/githubproject/fig_cell/datatxt/data2_8.txt')
# datatxt1_8 = data1_8.readlines()
# data1_9 = open('/Users/arcstone_mems_108/Desktop/keyan/githubproject/fig_cell/datatxt/data2_9.txt')
# datatxt1_9 = data1_9.readlines()
data1_10 = open('/Users/arcstone_mems_108/Desktop/keyan/githubproject/fig_cell/datatxt/data1_10.txt')
datatxt1_10 = data1_10.readlines()
#========================================【定义变量】======================================================
p1 = r"本次显示的特征点为\d*个"
pattern1 = re.compile(p1)
p2 = r".*速度为\d*"
pattern2 = re.compile(p2)
p3 = r"当前为第\d*帧"
pattern3 = re.compile(p3)
nodeTempArray = [[]]  # 二维数组用来存放每次的特征点的个数
frameList = []  # 存放当前的帧数，和i对应
node_list = []

variance_list = []
#node = np.array()

#========================================【进行正则匹配】======================================================
def v_rematch(datatxt):
    i = -1
    for line in datatxt:
        #print(line)
        matcher1 = re.match(pattern1, line)
        matcher2 = re.match(pattern2, line)
        matcher3 = re.match(pattern3, line)
        # if matcher3 and int(re.findall(r"(\W*[0-9]+)\W*", line)[0]) > 143:
        #     print(line)
        #     frameList.append(line)
        if matcher1:
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

#======================【对数据进行分析】=========================================
# 统计出一个列表每个速度都有多少个点,
# 每个列表都包含nodeTempArray.size组的数据，需要统计每个nodeTempArray里边的速度分布，放到数组中
# 实例化一个Counter类,存放各组速度的统计累加情况
v_data1_sum = collections.Counter()
v_data1_1 = collections.Counter()
v_data1_2 = collections.Counter()
v_data1_3 = collections.Counter()
v_data1_4 = collections.Counter()
v_data1_5 = collections.Counter()
v_data1_6 = collections.Counter()
v_data1_7 = collections.Counter()
v_data1_8 = collections.Counter()
v_data1_9 = collections.Counter()
v_data1_10 = collections.Counter()
#=================================【进行各组数据的速度统计】==============================
v_rematch(datatxt1_1)
for i in range(1, len(nodeTempArray)-1):
    # i代表一小组数据
    v_data1_1.update(nodeTempArray[i])
nodeTempArray.clear()

v_rematch(datatxt1_2)
for i in range(1, len(nodeTempArray)-1):
    # i代表一小组数据
    v_data1_2.update(nodeTempArray[i])
nodeTempArray.clear()

v_rematch(datatxt1_3)
for i in range(1, len(nodeTempArray)-1):
    # i代表一小组数据
    v_data1_3.update(nodeTempArray[i])
nodeTempArray.clear()

v_rematch(datatxt1_4)
for i in range(1, len(nodeTempArray)-1):
    # i代表一小组数据
    v_data1_4.update(nodeTempArray[i])
nodeTempArray.clear()

v_rematch(datatxt1_5)
for i in range(1, len(nodeTempArray)-1):
    # i代表一小组数据
    v_data1_5.update(nodeTempArray[i])
nodeTempArray.clear()
v_rematch(datatxt1_6)
for i in range(1, len(nodeTempArray)-1):
    # i代表一小组数据
    v_data1_6.update(nodeTempArray[i])
nodeTempArray.clear()
v_rematch(datatxt1_7)
for i in range(1, len(nodeTempArray)-1):
    # i代表一小组数据
    v_data1_7.update(nodeTempArray[i])
nodeTempArray.clear()
# v_rematch(datatxt1_8)
# for i in range(1, len(nodeTempArray)-1):
#     # i代表一小组数据
#     v_data1_8.update(nodeTempArray[i])
# nodeTempArray.clear()
# v_rematch(datatxt1_9)
# for i in range(1, len(nodeTempArray)-1):
#     # i代表一小组数据
#     v_data1_9.update(nodeTempArray[i])
# nodeTempArray.clear()
v_rematch(datatxt1_10)
for i in range(1, len(nodeTempArray)-1):
    # i代表一小组数据
    v_data1_10.update(nodeTempArray[i])
nodeTempArray.clear()

v_data1_sum.update(v_data1_1)
v_data1_sum.update(v_data1_2)
v_data1_sum.update(v_data1_3)
v_data1_sum.update(v_data1_4)
v_data1_sum.update(v_data1_5)
v_data1_sum.update(v_data1_6)
v_data1_sum.update(v_data1_7)
#v_data1_sum.update(v_data1_8)
#v_data1_sum.update(v_data1_9)
v_data1_sum.update(v_data1_10)

xArray = []             # 存放速度的值
yArray = []             # 存放对应值速度的个数

for x in v_data1_sum:
    xArray.append(x)
    yArray.append(v_data1_sum[x])

yArray_sum = sum(yArray)

for i in range(0, len(yArray)):
    yArray[i] = float(yArray[i])/float(yArray_sum)
    #yArray = '%.2f' % (float(yArray[i])/yArray_sum)

#plt.xlim(-6, 20)
#plt.ylim(0, 0.025)
# plt.xticks(-5, 18, 1)
# plt.yticks(0, 0.024, 0.005)
plt.bar(xArray, yArray, width = 0.1 ,facecolor='#9999ff', edgecolor='white')
plt.xlabel("速度")
plt.ylabel("比例")
plt.title("次靠前速度分布图")
plt.show()
# for i in range(1, len(nodeTempArray)-1):# 计算每一帧的均值和方差并且显示出来
#     node = np.array(nodeTempArray[i])
#     mean_value = node.mean()
#     node_list.append(mean_value)         # 存放速度均值的列表
#     variance = node.var()
#     variance_list.append(variance)       # 存放速度方差的列表


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
# x = range(144, 178)
# plt.figure(figsize=(7, 10))
# print(len(node_list))
# plt.subplot(2, 1, 1)
# plt.title("速度变化图")
# plt.xlabel("当前帧")
# plt.ylabel("速度")
# plt.plot(x, node_list)
#
#
#
# plt.subplot(2, 1, 2)
# plt.xlabel("当前帧")
# plt.ylabel("方差")
# plt.title("方差变化图")
#
# plt.plot(x, variance_list)
# plt.show()
#

# =============================================================================
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
