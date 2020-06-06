import matplotlib.pyplot as plt
import numpy as np

n = 1024

x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
# 颜色
t = np.arctan2(y, x)

plt.scatter(x, y, s=75, c=t, alpha=0.5)

plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

# 隐藏x,y轴的 刻度线
plt.xticks(())
plt.yticks(())
plt.show()
