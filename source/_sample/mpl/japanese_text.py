#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""japanese_text.py: Demonstrate how to draw Japanese text.
"""
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

FONT_PROP = FontProperties(fname=r'C:\WINDOWS\Fonts\HGRME.TTC')

plt.text(0, 0, '御無礼\n一発です',
         fontproperties=FONT_PROP, fontsize=60)
plt.show()
