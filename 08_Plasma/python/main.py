import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from statistics import mean, median, variance, stdev


def reg1dim(x, y):
    n = len(x)
    a = ((np.dot(x, y) - y.sum() * x.sum()/n) /
         ((x ** 2).sum() - x.sum()**2 / n))
    b = (y.sum() - a * x.sum())/n
    return a, b


# 配色リスト[黒，青，赤，緑，黄，紫，水色]
color_list = ["#000000", "#296fbc", "#cb360d",
              "#3d9435", "#e1aa13", "#a54675", "#138bae"]

# x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['xtick.direction'] = 'in'
# y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.width'] = 1.0  # x軸主目盛り線の線幅
plt.rcParams['ytick.major.width'] = 1.0  # y軸主目盛り線の線幅
plt.rcParams['font.size'] = 9           # フォントの大きさ
plt.rcParams['axes.linewidth'] = 0.7    # 軸の線幅edge linewidth。囲みの太さ

fig = plt.figure(figsize=(13.5/2.54, 7/2.54))
ax = fig.add_subplot(1, 1, 1)

# データの読み込み
file_name = "probedata.csv"
p2 = np.genfromtxt(file_name, delimiter=',', filling_values=0)
vp = p2[0:, 0]
ip = p2[0:, 1]

# 傾きが緩やかな部分だけを抽出
vp_sub = vp[:6]
ip_sub = ip[:6]
a, b = reg1dim(vp_sub, ip_sub)
iis = abs(b)
ie = ip - iis
ie = np.log(ie)
vp_sub_2 = vp[35:39]
ie_sub_2 = ie[35:39]
a2, b2 = reg1dim(vp_sub_2, ie_sub_2)

# 1
# ax.plot(vp, ip, color=color_list[1], linewidth=1)
# plt.xlabel("$V_p$ [V]", fontsize=10)
# plt.ylabel("$I_p$ [mA]", fontsize=10)

# 2
# ax.plot(vp, ip, color=color_list[1], linewidth=2)
# ax.plot([0, vp_sub.min()], [b, a * vp_sub.min() + b],
#         color=color_list[2], linewidth=1, linestyle="dashed")
# plt.xlabel("$V_p$ [V]", fontsize=10)
# plt.ylabel("$I_p$ [mA]", fontsize=10)
# plt.setp(ax.get_xticklabels(), fontsize=10)
# plt.setp(ax.get_yticklabels(), fontsize=10)
# print("iis:" + str(iis))
# ax.grid(ls="--")

# 3
# ax.plot(vp, ie, color=color_list[1], linewidth=1)
# plt.xlabel("$V_p$ [V]", fontsize=10)
# plt.ylabel("$I_e$ [mA]", fontsize=10)
# plt.setp(ax.get_xticklabels(), fontsize=10)
# plt.setp(ax.get_yticklabels(), fontsize=10)
# ax.grid(ls="--")


# 4
ax.plot(vp, ie, color=color_list[1], linewidth=2)
ax.plot([0, vp_sub_2.min()], [b2, a2 * vp_sub_2.min() + b2],
        color=color_list[2], linewidth=1, linestyle="dashed")
plt.xlabel("$V_p$ [V]", fontsize=10)
plt.ylabel("$\ln(I_e)$ [mA]", fontsize=10)
plt.setp(ax.get_xticklabels(), fontsize=10)
plt.setp(ax.get_yticklabels(), fontsize=10)
print(a2)
ax.grid(ls="--")


# グラフタイトル
# plt.title('')

# グラフ範囲
# plt.xlim()
# plt.ylim(0.0, 0.7)

# 余白設定
plt.subplots_adjust(left=0.105, right=0.98, bottom=0.21, top=0.95)

# グラフの凡例
# ax.legend(fancybox=False, framealpha=1, edgecolor="#000000",
#   loc = 'upper right', fontsize = 9)

# 表示
plt.show()
