# coding=utf-8

import random
import urllib
import requests
import time
import re
from lxml import html
import generateURL
import fileDownload
import fileHandle
from agents import AGENTS

def fillNum(num):
    totalNum = 4
    numString = str(num)
    length = len(numString)
    while length < totalNum :
        numString = "0" + numString
        length +=1
    return numString


def download(url,sortNum,fileNum,food):
    tree = list()
    print ("now is downloading url:   " , url)

    agents = random.choice(AGENTS)
    headers = {'user-agent': agents}
    page = requests.get(url, headers=headers)           # html页面内容
    tree = html.fromstring(page.content)                # 格式转换
    contentList = tree.xpath('//div[@class="rg_meta"]/text()')  # 描述图片文字的集合
    ouPattern = re.compile(r'"ou":"(.*?)"', re.S)       # ou,图片高清地址
    ptPattern = re.compile(r'"pt":"(.*?)"', re.S)       # pt,图片描述标题
    ruPattern = re.compile(r'"ru":"(.*?)"', re.S)       # ru,图片来源地址
    sPattern = re.compile(r'"s":"(.*?)"', re.S)         # s, 图片描述正文
    stPattern = re.compile(r'"st":"(.*?)"', re.S)       # st,图片描述副标题

    print("now is downloading image:")
    fileDir = fileDownload.fileDir + "image/" + food + "/"       # 图片根目录
    fileHandle.makeDir(fileDir)
    contextDir = fileDownload.fileDir + "context/" + food + "/"  # 文件根目录
    fileHandle.makeDir(contextDir)

    for imgText in contentList:
        fileName = fillNum(sortNum) + fillNum(fileNum)
        fileNum = fileNum + 1
        print (fileName)
        contextPath = contextDir + fileName + r".txt"

        ouResult = re.findall(ouPattern, imgText)
        ptResult = re.findall(ptPattern, imgText)
        ruResult = re.findall(ruPattern, imgText)
        sResult  = re.findall(sPattern , imgText)
        stResult = re.findall(stPattern, imgText)


        if len(ouResult) != 0 :
            filePath = fileDir + fileName + r".jpg"
            isSuccess=fileDownload.downImageByURL(filePath,ouResult[0])
            if not isSuccess:
                continue
            fileHandle.fileWrite(contextPath, "ou:" + ouResult[0] + "\n")

            if len(ptResult) == 0:
                fileHandle.fileWrite(contextPath, "pt:null" + "\n")
            else:
                fileHandle.fileWrite(contextPath, "pt:" + ptResult[0] + "\n")

            if len(ruResult) == 0:
                fileHandle.fileWrite(contextPath, "ru:null" + "\n")
            else:
                fileHandle.fileWrite(contextPath, "ru:" + ruResult[0] + "\n")

            if len(sResult) == 0:
                fileHandle.fileWrite(contextPath, "s:null" + "\n")
            else:
                fileHandle.fileWrite(contextPath, "s:" + sResult[0] + "\n")

            if len(stResult) == 0:
                fileHandle.fileWrite(contextPath, "st:null" + "\n")
            else:
                fileHandle.fileWrite(contextPath, "st:" + stResult[0] + "\n")


    return fileNum




if __name__ == "__main__":
    fileName = "sgFoodList.txt"
    foodList = fileHandle.fileRead(fileName)
    sortNum = 1                                        # 文件种类数目
    for food in foodList:
        if sortNum < 181:                               #从中断食物处重新运行，数字是中断数字的编号
            sortNum += 1
            continue
        if sortNum > 181:                               #终止的编号
            break
        fileNum = 1                                    # 该类下文件的个数
        for year in generateURL.years:
            time.sleep(1)                              #每个url休眠一秒
            url = generateURL.getGoogleURL(food,year)
            fileNum=download(url,sortNum,fileNum,food)

        sortNum += 1


