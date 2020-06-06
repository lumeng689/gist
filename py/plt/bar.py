import matplotlib.pyplot as plt
import numpy as np

n = 12

x = np.arange(n)
y1 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)
y2 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)

for x, y in zip(x, y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(x, y2):
    plt.text(x + 0.4, y - 0.05, '%.2f' % y, ha='center', va='bottom')

plt.xlim(-.5, n)
# plt.xticks(())
plt.ylim(-1.25, 1.25)
# plt.yticks(())

plt.bar(x, y1, facecolor='#9999FF', edgecolor='white')
plt.bar(x, -y2, facecolor='#FF9999', edgecolor='white')

plt.show()
