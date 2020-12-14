from bs4 import BeautifulSoup
import requests

webpage = requests.get("http://ncov.mohw.go.kr/")
soup = BeautifulSoup(webpage.content, "html.parser")

def convert2today(str): return str.split("(+ ")[1].split(")")[0]

# 누적 확진자 수
all_confirmed_person = soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(1) > span.num").get_text().split(")")[1]
# 일일 확진자 수
today_confirmed_person = convert2today(soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(1) > span.before").get_text())
# 누적 격리해제 수
all_quarantine_release = soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(2) > span.num").get_text()
# 일일 격리해제 수
today_quarantine_release = convert2today(soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(2) > span.before").get_text())
# 누적 치료 중
all_cure = soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(3) > span.num").get_text()
# 일일 치료 중
today_cure = convert2today(soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(3) > span.before").get_text())
# 누적 사망자
all_die = soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(4) > span.num").get_text()
# 일일 사망자
today_die = convert2today(soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(4) > span.before").get_text())


print("누적 확진: " + all_confirmed_person)
print("일일 확진: " + today_confirmed_person)
print("누적 격리해제: " + all_quarantine_release)
print("일일 격리해제: " + today_quarantine_release)
print("누적 치료 중: " + all_cure)
print("일일 치료 중: " + today_cure)
print("누적 사망자: " + all_die)
print("일일 사망자: " + today_die)
