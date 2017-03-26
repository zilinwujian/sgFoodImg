# #coding:utf-8
import os


# def fileRead(filePath):
#     fileList = list()
#     with open(filePath,"r") as f:
#
#         # for line in f.readline():
#         #     line = line.strip()  # 去掉每行头尾空白
#         #     print line
#         #     if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
#         #         continue  # 是的话，跳过不处理
#         #     fileList.append(line)  # 保存
#     return fileList

# 读取文件
def fileRead(filePath):
    f = open(filePath, 'r')  # 以读方式打开文件
    result = list()
    for line in f.readlines():  # 依次读取每行
        line = line.strip()  # 去掉每行头尾空白
        result.append(line)  # 保存
    f.close()
    return result

# 写入文件
def fileWrite(filePath,contents):
    f =open(filePath,'a+')
    f.write(contents)
    f.close()
    return

# 创建目录
def makeDir(fileDir):
    if not os.path.exists(fileDir):
        # print(fileDir, " not exist")
        os.makedirs(fileDir)
        # print("make directory successfully")
    else:
        print(fileDir, "exist")