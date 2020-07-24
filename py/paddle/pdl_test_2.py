import numpy
import paddle

# 定义输入数据占位符
a = paddle.nn.data(name="a", shape=[1], dtype='int64')
b = paddle.nn.data(name="b", shape=[1], dtype='int64')
# 组建网络（此处网络仅由一个操作构成，即elementwise_add）
result = paddle.elementwise_add(a, b)
# 准备运行网络
cpu = paddle.CPUPlace()  # 定义运算设备，这里选择在CPU下训练
exe = paddle.Executor(cpu)  # 创建执行器
# 创建输入数据
x = numpy.array([2])
y = numpy.array([3])
# 运行网络
outs = exe.run(
    feed={'a': x, 'b': y},  # 将输入数据x, y分别赋值给变量a，b
    fetch_list=[result]  # 通过fetch_list参数指定需要获取的变量结果
)
# 输出运行结果
print(outs)
# [array([5], dtype=int64)]

# end of file
