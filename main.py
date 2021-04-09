import os
import requests
from bs4 import BeautifulSoup

defaultURL = "https://arca.live/"
placeHolder = {
    "emoji": "body > div > div.content-wrapper.clearfix > article > div > div.article-wrapper > div.article-body",
    "info": "body > div > div.content-wrapper.clearfix > article > div > div.article-wrapper > div.article-head"
}
downloadDirectory = "./downloads"
counter = 0
returnFormat = {
    "name": "",
    "author": "",
    "sold": "",
    "submitted": "",
    "emojis": []
}


def requestData(startsWith, numericOnly=False):
    data = input(f"\n입력 예시 : %se/1234\n다운로드받을 이모티콘의 URL을 입력해주세요 > " % defaultURL)
    if not data.startswith(startsWith):
        print("❌ 잘못된 입력입니다.")
        return False
    elif numericOnly and data.isdigit():
        print("❌ 형식이 잘못되었습니다.")
        return False
    else:
        return data.replace(startsWith, "")


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


print("[아카라이브 이모티콘 다운로더]\n소장하고 싶은 이모티콘을 다운받아 저장하세요.\n❗본 프로그램의 사용으로 인해 발생하는 모든 문제에 대해 제작자는 아무런 책임을 지지 않습니다.", end="\n\n")

# Create download folder if not exists
if os.path.isdir(downloadDirectory):
    print(f"✅ 다운로드받을 디렉토리(%s) 확인 완료" % downloadDirectory)
else:
    print(f"❌ 다운로드받을 디렉토리(%s)가 존재하지 않아 생성하였습니다." % downloadDirectory)
    createFolder(downloadDirectory)

# Get emoji ID
while True:
    emojiID = requestData(defaultURL + "e/")
    if str(type(emojiID)) == "<class 'str'>" and len(emojiID) >= 1:
        print(f"✅ 대상 이모티콘 ID: %s" % emojiID)
        break

GETdata = requests.get(f"%se/%s" % (defaultURL, emojiID))
if GETdata.status_code == 200:
    EmojiShopHTML = GETdata.text
    soup = BeautifulSoup(EmojiShopHTML, 'html.parser')
    EmojiData = soup.select_one(placeHolder['emoji'])
    EmojiInfo = soup.select_one(placeHolder['info'])
else:
    print(f"❌ HTTP ERROR %s\n서버에 연결할 수 없거나 접근할 수 없는 이모티콘입니다." % GETdata.status_code)
    quit()

# Data processing
try:
    returnFormat["name"] = EmojiInfo.findAll("div")[1].text.replace("\n", "")
    returnFormat["author"] = EmojiInfo.findAll("div")[3].text.replace("\n", "")
    returnFormat["sold"] = EmojiInfo.findAll("div")[4].findAll("span")[1].text.replace("\n", "")
    returnFormat["submitted"] = EmojiInfo.findAll("div")[4].findAll("span")[2].findAll("span")[2].text.replace("\n", "")
    for piece in EmojiData.findAll('img'):
        returnFormat["emojis"].append(piece["src"].replace("//", "https://"))
    print("\n✅ 이모티콘 정보를 성공적으로 불러왔습니다.")
    print(f" - 이름 : %s" % returnFormat["name"])
    print(f" - 갯수 : %s개" % len(returnFormat["emojis"]))
    print(f" - 제작자 : %s" % returnFormat["author"])
    print(f" - 판매수 : %s회" % returnFormat["sold"])
    print(f" - 등록일 : %s" % returnFormat["submitted"])
except:
    print("❌ 내려받을 수 없는 이모티콘입니다.")
    quit()

# Download
try:
    saveDirectory = f"%s/%s-%s-%s/" % (downloadDirectory, emojiID, returnFormat["name"], returnFormat["author"])
    if os.path.isdir(saveDirectory):
        print(f"\n❌ 최종 다운로드 디렉토리가 이미 존재합니다.\n다음 디렉토리를 삭제한 후 다시 시도해주세요 : %s" % saveDirectory)
        quit()
    else:
        createFolder(saveDirectory)
        print("\n✅ 다운로드 받을 폴더를 생성하였습니다.")
    for imageURL in returnFormat["emojis"]:
        link = imageURL.split("/")
        currentFile = {
            "name": link[len(link)-1].split(".")[0],
            "ext": link[len(link)-1].split(".")[1]
        }
        print(f" > %d 개중 %d 번째 항목을 내려받고 있습니다." % (len(returnFormat["emojis"]), counter + 1))

        fileFromURL = requests.get(imageURL)
        openedFile = open(f"%s%d.%s" % (saveDirectory, counter, currentFile["ext"]), "wb")
        openedFile.write(fileFromURL.content)
        openedFile.close()
        counter = counter + 1

    print("\n✅ 다운로드가 완료되었습니다.")

except:
    print("\n오류가 발생했습니다.")