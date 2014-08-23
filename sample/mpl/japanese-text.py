# -*- coding: utf-8 -*-
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname=r'C:\WINDOWS\Fonts\HGRME.ttc') # HG 明朝系
plt.text(0, 0, '御無礼\n一発です', fontproperties=fp, fontsize=60)
plt.show()
