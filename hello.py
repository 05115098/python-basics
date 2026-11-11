print("Hello,Python!")

a=10
b=20
print("a+b", a+b)

import sys
import numpy as np

print("当前 Python 路径：", sys.executable)
print("NumPy 版本：", np.__version__)

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("计算结果：", a + b)