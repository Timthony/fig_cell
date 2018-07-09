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
data_7_5 = open('/Users/arcstone_mems_108/Desktop/keyan/githubproject/fig_cell/data7_5_2.txt')


#========================================【定义变量】======================================================
p1 = r"本次显示的特征点为\d*个"
pattern1 = re.compile(p1)
p2 = r".*速度为\d*"
pattern2 = re.compile(p2)
p3 = r"当前为第\d*帧"
pattern3 = re.compile(p3)
p4 = r"第\d*帧前段点的运动速度为.*"
pattern4 = re.compile(p4)
p5 = r"第\d*帧中段点的运动速度为.*"
pattern5 = re.compile(p5)
p6 = r"第\d*帧后段点的运动速度为.*"
pattern6 = re.compile(p6)
# 以下是哪个数组的组合即代表某一帧某一点的速度在前段中段后段
k_now = []                   # 存放当前的帧数
k_now_loc = []               # 存放当前帧的前中后，0代表前，1代表中，2代表后
k_now_v = []                 # 存放当前帧该点的速度

# ========================================【进行正则匹配】======================================================
# 07_05数据匹配
def v_rematch_1(datatxt):
    i = -1
    for line in datatxt:
        matcher1_0705 = re.match(pattern4, line)
        matcher2_0705 = re.match(pattern5, line)
        matcher3_0705 = re.match(pattern6, line)

        if matcher1_0705:
            #print(matcher1_0705.group())
            k1 = int(re.findall(r"(\W*[0-9]+)\W*", line)[0])          # 表示当前正在播放的帧数
            v1 = int(re.findall(r"(\W*[0-9]+)\W*", line)[1])
            v2 = int(re.findall(r"(\W*[0-9]+)\W*", line)[2])
            v_beg = str(v1) + '.' + str(v2)
            v_beg = float(v_beg)                                             # 表示当前帧，当前点的速度
            #print(v_beg)
            # 将所得数据存放到数组
            k_now.append(k1)
            k_now_loc.append(0)
            k_now_v.append(v_beg)
        if matcher2_0705:
            #print(matcher2_0705.group())
            k2 = int(re.findall(r"(\W*[0-9]+)\W*", line)[0])          # 表示当前正在播放的帧数
            v1 = int(re.findall(r"(\W*[0-9]+)\W*", line)[1])
            v2 = int(re.findall(r"(\W*[0-9]+)\W*", line)[2])
            v_mid = str(v1) + '.' + str(v2)
            v_mid = float(v_mid)                                             # 表示当前帧，当前点的速度
            #print(v_mid)
            # 将所得数据存放到数组
            k_now.append(k2)
            k_now_loc.append(1)
            k_now_v.append(v_mid)
        if matcher3_0705:
            #print(matcher3_0705.group())
            k3 = int(re.findall(r"(\W*[0-9]+)\W*", line)[0])          # 表示当前正在播放的帧数
            v1 = int(re.findall(r"(\W*[0-9]+)\W*", line)[1])
            v2 = int(re.findall(r"(\W*[0-9]+)\W*", line)[2])
            v_end = str(v1) + '.' + str(v2)
            v_end = float(v_end)                                             # 表示当前帧，当前点的速度
            #print(v_end)
            # 将所得数据存放到数组
            k_now.append(k3)
            k_now_loc.append(2)
            k_now_v.append(v_end)

v_rematch_1(data_7_5)           # 进行数据提取

# 对提取得到的数据进行处理

# 画出前中后三段，每一帧三幅图，横轴都是速度，纵轴都是占比，另外方差和平均速度也都在图中
k_v = []  # 当前所有前中后段的速度和


v_temp_beg_all = [[]]             # 存放每一帧前段点的集合的二维数组
v_temp_mid_all = [[]]

v_temp_end_all = [[]]

# k表示当前的帧数
k_all = k_now[-1] - k_now[0]                  # 总帧数
for k in range(1, k_all):                     # 最后一帧的帧数为k_now[-1],第一帧k_now[0]
    v_temp_beg = []  # 临时数组，每次存放当前帧所有前段点的集合
    v_temp_mid = []
    v_temp_end = []
    for i in range(1, len(k_now)):
        k_curr = k_now[0] + k               # 表示当前帧
        if(k_now[i] == k_curr):
            if(k_now_loc[i] == 0):
                v_temp_beg.append(k_now_v[i])
            elif(k_now_loc[i] == 1):
                v_temp_mid.append(k_now_v[i])
            elif(k_now_loc[i] == 2):
                v_temp_end.append(k_now_v[i])
    v_temp_beg_all.append(v_temp_beg)
    v_temp_mid_all.append(v_temp_mid)
    v_temp_end_all.append(v_temp_end)


# 画图，画出每一帧的前段、中段、后段速度分布图


# 遍历每一帧
for i in range(1, k_all):
    v_col_beg = collections.Counter(v_temp_beg_all[i])
    v_col_mid = collections.Counter(v_temp_mid_all[i])
    v_col_end = collections.Counter(v_temp_end_all[i])
    x_arr_beg = []                 # 存放速度是多少
    y_arr_beg = []                 # 对应存放当前的速度有多少像素点
    x_arr_mid = []
    y_arr_mid = []
    x_arr_end = []
    y_arr_end = []
    y_arr_beg_scale = []           # 比例
    y_arr_mid_scale = []
    y_arr_end_scale = []
    # 画前段点的函数
    for v_x_beg in v_col_beg:
        x_arr_beg.append(v_x_beg)
        y_arr_beg.append(v_col_beg[v_x_beg])

        y_arr_beg_scale.append(v_col_beg[v_x_beg]/len(v_temp_beg_all[i]))
    plt.subplot(1,3,1)
    plt.bar(x_arr_beg, y_arr_beg_scale,  width = 0.06, facecolor='#9999ff',edgecolor='white')
    title_beg = k_now[0] + i           # 当前帧
    title_beg_str = "第" + str(title_beg) + "帧前段"
    plt.title(title_beg_str)
    # 计算前段的均值、方差
    v_avg_beg = sum(v_temp_beg_all[i])/len(v_temp_beg_all[i])        # 均值
    v_var_beg = np.array(v_temp_beg_all[i]).var()                    # 方差
    plt.text(max(x_arr_beg)*0.9, max(y_arr_beg_scale), "均值：%.2f" % v_avg_beg,
             fontsize=12, verticalalignment='center', horizontalalignment='center')
    plt.text(max(x_arr_beg)*0.9, max(y_arr_beg_scale)*0.9, "方差：%.2f" % v_var_beg,
             fontsize=12, verticalalignment='center', horizontalalignment='center')
    plt.xlabel("速度")
    plt.ylabel("占比")
    #plt.show()
    #print(title_beg_str + "均值为：", v_avg_beg)
    #print(title_beg_str + "方差为: ", v_var_beg)


    # 画中段点的函数
    for v_x_mid in v_col_mid:
        x_arr_mid.append(v_x_mid)
        y_arr_mid.append(v_col_mid[v_x_mid])
        y_arr_mid_scale.append(v_col_mid[v_x_mid]/len(v_temp_mid_all[i]))
    plt.subplot(1, 3, 2)
    plt.bar(x_arr_mid, y_arr_mid_scale, width = 0.06, facecolor='#9999ff',edgecolor='white')
    title_mid = k_now[0] + i           # 当前帧
    title_mid_str = "第" + str(title_mid) + "帧中段"
    plt.title(title_mid_str)
    # 计算中段的均值、方差
    v_avg_mid = sum(v_temp_mid_all[i])/len(v_temp_mid_all[i])        # 均值
    v_var_mid = np.array(v_temp_mid_all[i]).var()                    # 方差
    plt.text(max(x_arr_mid) * 0.9, max(y_arr_mid_scale), "均值：%.2f" % v_avg_mid,
             fontsize=12, verticalalignment='center', horizontalalignment='center')
    plt.text(max(x_arr_mid) * 0.9, max(y_arr_mid_scale) * 0.9, "方差：%.2f" % v_var_mid,
             fontsize=12,verticalalignment='center', horizontalalignment='center')
    plt.xlabel("速度")
    plt.ylabel("占比")
    #plt.show()
    #print(title_mid_str + "均值为：", v_avg_mid)
    #print(title_mid_str + "方差为: ", v_var_mid)

    # 画后段点的函数
    for v_x_end in v_col_end:
        x_arr_end.append(v_x_end)
        y_arr_end.append(v_col_mid[v_x_end])
        y_arr_end_scale.append(v_col_end[v_x_end] / len(v_temp_end_all[i]))
    plt.subplot(1,3,3)
    plt.bar(x_arr_end, y_arr_end_scale, width = 0.06, facecolor='#9999ff',edgecolor='white')
    title_end = k_now[0] + i           # 当前帧
    title_end_str = "第" + str(title_end) + "帧后段"
    plt.title(title_end_str)
    # 计算后段的均值、方差
    v_avg_end = sum(v_temp_end_all[i])/len(v_temp_end_all[i])        # 均值
    v_var_end = np.array(v_temp_end_all[i]).var()                    # 方差
    plt.text(max(x_arr_end) * 0.9, max(y_arr_end_scale), "均值：%.2f" % v_avg_end,
             fontsize=12, verticalalignment='center', horizontalalignment='center')
    plt.text(max(x_arr_end) * 0.9, max(y_arr_end_scale) * 0.9, "方差：%.2f" % v_var_end,
             fontsize=12,verticalalignment='center', horizontalalignment='center')
    plt.xlabel("速度")
    plt.ylabel("占比")

    fig_name = str(str(k_now[i]) + '.jpg')
    fig_save = str('/Users/arcstone_mems_108/Desktop/result/cell_fig/' + fig_name)
    plt.savefig(fig_save, format = 'png', dpi = 300)
    #print(title_end_str + "均值为：", v_avg_end)
    #print(title_end_str + "方差为: ", v_var_end)

    #plt.show()
    



# 画图，横轴为时间，纵轴为方差
v_var_k_all_beg = []        # 存放每一帧的方差
v_avg_k_all_beg = []        # 存放每一帧的平均速度
v_var_k_all_mid = []        # 存放每一帧的方差
v_avg_k_all_mid = []        # 存放每一帧的平均速度
v_var_k_all_end = []        # 存放每一帧的方差
v_avg_k_all_end = []        # 存放每一帧的平均速度
k_now_i = []
for i in range(1, k_all):
    k_now_i.append(k_now[0] + i)
    v_temp_beg_now = np.array(v_temp_beg_all[i])
    v_temp_mid_now = np.array(v_temp_mid_all[i])
    v_temp_end_now = np.array(v_temp_end_all[i])
    v_var_k_all_beg.append(v_temp_beg_now.var())
    v_avg_k_all_beg.append(v_temp_beg_now.sum()/len(v_temp_beg_all[i]))
    v_var_k_all_mid.append(v_temp_mid_now.var())
    v_avg_k_all_mid.append(v_temp_mid_now.sum()/len(v_temp_mid_all[i]))
    v_var_k_all_end.append(v_temp_end_now.var())
    v_avg_k_all_end.append(v_temp_end_now.sum()/len(v_temp_end_all[i]))




plt.subplot(1,2,1)
plt.xlabel("时间")
plt.ylabel("方差")
plt.plot(k_now_i, v_var_k_all_beg, label='前段', color = 'b', marker='+')
plt.plot(k_now_i, v_var_k_all_mid, label='中段', color = 'g', marker='>')
plt.plot(k_now_i, v_var_k_all_end, label='后段', color = 'r', marker='o')



plt.subplot(1,2,2)
plt.xlabel("时间")
plt.ylabel("平均速度")
plt.plot(k_now_i, v_avg_k_all_beg, label='前段', color = 'b', marker='+')
plt.plot(k_now_i, v_avg_k_all_mid, label='中段', color = 'g', marker='>')
plt.plot(k_now_i, v_avg_k_all_end, label='后段', color = 'r', marker='o')



plt.show()



















# 画图，横轴为时间，纵轴为平均速度



























# k_v_sum = 0
# k_num = 0
# v_var = []
# k = []
# for j in range(0, 200):
#     k_v = []
#     for i in range(0, len(k_now)):
#         if (k_now[i] == k_now[0] + j):
#             k_v.append(k_now_v[i])             # 当前帧所有点的速度集合
#     if (k_now[0]+j > k_now[-1]):
#         break
#     k_v = np.array(k_v)
#     k_v_var = np.var(k_v)
#     v_var.append(k_v_var)
#     k.append(k_now[0]+j)
#
# # 画出每一帧所对应的速度的方差
#
# plt.xlabel("当前帧")
# plt.ylabel("方差")
#
# plt.plot(k[:-1], v_var[:-1])
#
# plt.show()

        













