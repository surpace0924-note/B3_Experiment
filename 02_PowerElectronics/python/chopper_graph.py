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
x_1 = np.linspace(0, 5, 500)
v_F = []
for i in range(len(x_1)):
    if int(x_1[i]) % 2 == 0:
        v_F.append(1)
    else:
        v_F.append(0)
v_F[0] = 0

x_2 = [0, 1, 2, 3, 4, 5]
v_d = [0.4, 0.6, 0.4, 0.6, 0.4, 0.6]

x_3 = [0, 5]
V_d = [0.5, 0.5]

# グラフにデータを追加
ax.plot(x_1, v_F, color=color_list[1], linewidth=1, label='$v_F$')
ax.plot(x_2, v_d, color=color_list[3], linewidth=2, label='$i_d$')
# ax.plot(x_3, V_d, color=color_list[0], linewidth=2, label='$V_d$')

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
