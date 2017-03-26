# coding=utf-8

years = ["2012","2013","2014","2015","2016"]

def getGoogleURL (search,year) :
    urlDir = r"https://www.google.com/search?q="
    content = r"&biw=1280&bih=631&source=lnt&tbs=cdr%3A1%2Ccd_min"
    endURL = r"&tbm=isch"
    startDay = "1"
    startMonth = "1"
    startYear = year
    endDay = "31"
    endMonth = "12"
    endYear = year

    tempurl = urlDir + search + content
    url = tempurl + r"%3A" + startMonth + r"%2F" + startDay + r"%2F" + startYear + r"%2Ccd_max"
    url = url + r"%3A" + endMonth + r"%2F" + endDay + r"%2F" + endYear + endURL

    return url