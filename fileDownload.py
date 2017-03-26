import urllib
import random
import requests
from agents import AGENTS

fileDir = r"/Users/liuxingyu/sgfoodImage2/";

# def downImageByURL(filePath,imgURL):
#     data = urllib.urlopen(imgURL).read()
#     f = file(filePath, "wb")
#     f.write(data)
#     f.close()
#     return


def downImageByURL(filePath,imgURL):
    agents = random.choice(AGENTS)
    headers = {'user-agent': agents}
    response = requests.get(imgURL, stream=True, headers=headers)
    with open(filePath, 'wb') as f:
        f.write(response.content)