from pathlib import Path

p=Path()
# 这个确认文件夹是否存在是从Py的根目录开始检测的
# p.mkdir() 创建文件夹
# p.rmdir() 删除文件夹
# *.* 搜索当前目录的所有文件，而不是目录
# print(p.exists())

for file in p.glob("*"):
    print(file)