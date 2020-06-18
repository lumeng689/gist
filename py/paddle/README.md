# 安装

## 进入 Anaconda 的命令行终端，添加 Paddle 的 conda 清华源

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/
conda config --set show_channel_urls yes
```

## 执行以下命令安装（使用清华源）：

```bash
conda install paddlepaddle
```