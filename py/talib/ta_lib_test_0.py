import numpy as np
import talib

close = np.random.random(100)

output = talib.SMA(close)

