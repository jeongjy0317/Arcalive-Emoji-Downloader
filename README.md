[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
![GitHub last commit](https://img.shields.io/github/last-commit/jeongjy0317/Arcalive-Emoji-Downloader.svg)

# 아카라이브 이모티콘 다운로더
파라과이 외 여러 국가에 거주하시는 다양한 분들이 아카라이브에서 배포되는 다양한 이모티콘을 내려받아 소장하실 수 있도록 만든 이모티콘 다운로더입니다.

## 사용된 라이브러리들
- requests
    - 아카라이브로부터 사이트 데이터를 받아오기 위해 사용됩니다.
- BeautifulSoup (패키지 이름 : `bs4`)
    - 받아온 데이터를 처리하기 위해 사용됩니다.

## 사용법
1. 본 Git을 Clone합니다.
2. `pip`를 통해 위 라이브러리들을 설치합니다.
3. `Python 3` 이상 버전으로 `main.py`를 실행합니다.
4. 이후에는 프로그램에서 요구하는대로 진행하시면 됩니다.

## 컴퓨터 초보자를 위한 사용법
1. 본 사이트 상단 초록색 버튼 `Code`를 누르시고, `Download ZIP`을 눌러 코드를 내려받습니다.
2. 다운로드받은 `ZIP`파일의 압축을 해제하고, 해제한 디렉토리를 엽니다.
3. 해제한 디렉토리에서 `SHIFT`키를 누름과 동시에 오른쪽 클릭하고, `여기에 Powershell 창 열기`를 눌러 콘솔을 열어줍니다.
4. `python main.py`를 입력하여 실행합니다.
5. 이제부터는 프로그램의 요구에 따라 진행하시면 되는데, 반드시 숫자로 끝나는 링크를 입력하셔야 합니다.

## 유의사항
- Clone한 디렉토리를 Working Directory로 설정하고 코드를 실행하세요.
    - 아닐 경우, 예상치 못한 곳에 `downloads` 폴더 및 스티커 파일이 저장될 수 있습니다.
- 본 코드를 사용하여 발생한 모든 문제에 대해 코드 제작자는 그 어떤 책임을 지지 않으며, 모두 사용자의 책임임을 명시합니다.
