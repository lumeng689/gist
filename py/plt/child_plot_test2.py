import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

left, bottom, width, height = .1, .1, .8, .8
ax1 = fig.add_axes([left, bottom, width, height])

ax1.plot(y, x, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title1')

plt.plot(x, y)
plt.show()
