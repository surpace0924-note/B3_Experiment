import cmath
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
plt.rcParams['font.size'] = 7           # フォントの大きさ
plt.rcParams['axes.linewidth'] = 0.7    # 軸の線幅edge linewidth。囲みの太さ

fig = plt.figure(figsize=(7/2.54, 7/2.54))
ax = fig.add_subplot(1, 1, 1)

# データの読み込み
x = np.linspace(10e+01, 10e+03, 500)

# Rf = 18e+03
# Rg = 10e+03
# R1 = 30.0e+03
# R2 = R1
# C1 = 5.1e-09
# C2 = C1
# K = 1+Rf/Rg

# #  回路のQ値の計算
# Q = 1/(np.sqrt((C2*R2)/(C1*R1))+np.sqrt((C2*R1)/(C1*R2)) +
#        np.sqrt((C1*R1)/(C2*R2))*(1-K))

# #  中心周波数
# omega_0 = 1 / np.sqrt(C1 * C2 * R1 * R2)

Q = 8.4
f_0 = 1000
omega_0 = 2 * np.pi * f_0
K = 3 - (1 / Q)

s = 2 * np.pi * x * (0+1j)

#  伝達関数の計算（s = jw）
gain = (K * omega_0 * omega_0) / (s*s + (omega_0 / Q)*s + omega_0*omega_0)

# 振幅の計算
mag = 20 * np.log10(abs(gain))

# 位相の計算
pha = []
for g in gain:
    pha.append(math.degrees(cmath.phase(g)))

# グラフにデータを追加
ax.set_xscale('log')
ax.plot(x, mag, color=color_list[1], linewidth=1)
# ax.plot(x, pha, color=color_list[1], linewidth=1)

# 目盛のスタイル
plt.setp(ax.get_xticklabels(), fontsize=7)
plt.setp(ax.get_yticklabels(), fontsize=7)
# ax.grid(ls="--")

# グラフタイトル
# plt.title('')

# グラフ範囲
# plt.xlim()
# plt.ylim(0.0, 0.7)

# 余白設定
plt.subplots_adjust(left=0.22, right=0.98, bottom=0.21, top=0.95)

# グラフの軸
plt.xlabel("$f$ [Hz]", fontsize=9)
plt.ylabel("$|T_{LP}|$ [dB]", fontsize=9)
# plt.ylabel("arg($T_{LP}$) [deg]", fontsize=9)

# グラフの凡例
# ax.legend(fancybox=False, framealpha=1, edgecolor="#000000",
#           loc='upper right', fontsize=9)

# 表示
plt.show()
