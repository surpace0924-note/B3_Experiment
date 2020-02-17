import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
from statistics import mean, median, variance, stdev

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

fig = plt.figure(figsize=(16/2.54, 5/2.54))
ax = fig.add_subplot(1, 1, 1)

# データの読み込み
x = np.linspace(0, 4*np.pi, 500)
v_1 = np.sqrt(2) * np.sin(x)
v_2 = np.sqrt(2) * np.sin(x+4*np.pi/3)
v_3 = np.sqrt(2) * np.sin(x+2*np.pi/3)

v_12 = v_1-v_2
v_13 = v_1-v_3
v_21 = v_2-v_1
v_23 = v_2-v_3
v_31 = v_3-v_1
v_32 = v_3-v_2

e_d = []
for i in range(len(v_12)):
    tmp = [v_12[i], v_13[i], v_21[i], v_23[i], v_31[i], v_32[i]]
    e_d.append(np.max(tmp))

# グラフにデータを追加
ax.plot(x, v_1, color=color_list[1], linewidth=1,
        label='$v_1$', linestyle="dashed")
ax.plot(x, v_2, color=color_list[2], linewidth=1,
        label='$v_2$', linestyle="dashed")
ax.plot(x, v_3, color=color_list[3], linewidth=1,
        label='$v_3$', linestyle="dashed")

ax.plot(x, v_12, color=color_list[1], linewidth=1, label='$v_{12}$')
ax.plot(x, v_13, color=color_list[2], linewidth=1, label='$v_{13}$')
ax.plot(x, v_21, color=color_list[3], linewidth=1, label='$v_{21}$')
ax.plot(x, v_23, color=color_list[4], linewidth=1, label='$v_{23}$')
ax.plot(x, v_31, color=color_list[5], linewidth=1, label='$v_{31}$')
ax.plot(x, v_32, color=color_list[6], linewidth=1, label='$v_{32}$')

ax.plot(x, e_d, color=color_list[0], linewidth=2, label='$e_d$')

# 目盛のスタイル
plt.setp(ax.get_xticklabels(), fontsize=10)
plt.setp(ax.get_yticklabels(), fontsize=10)
# ax.grid(ls="--")

# グラフタイトル
# plt.title('')

# グラフ範囲
# plt.xlim()
# plt.ylim(0.0, 0.7)

# 余白設定
plt.subplots_adjust(left=0.105, right=0.98, bottom=0.21, top=0.95)

# グラフの軸
plt.xlabel("Time [s]", fontsize=10)
# plt.ylabel("Differential value [m/s]", fontsize=10)

# グラフの凡例
ax.legend(fancybox=False, framealpha=1, edgecolor="#000000",
          loc='upper right', fontsize=9)

# 表示
plt.show()
