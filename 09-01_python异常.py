# 捕获所有异常
# 异常具有传递性
try:
    f = open("./123.txt", "r", encoding="UTF-8")
except Exception as e:
    print(e)




# 清华镜像源安装第三方包
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy 