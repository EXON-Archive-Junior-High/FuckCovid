from bs4 import BeautifulSoup
import requests
import schedule
import time
import os, sys

def convert2today(str): return str.split("(+ ")[1].split(")")[0]
def getNum(o): return o.select_one("button > span.num").get_text()
def getBefore(o): return o.select_one("button > span.before").get_text()
def bs2dict(region): return { "num": getNum(region), "before": getBefore(region) }

def task():
    webpage = requests.get("http://ncov.mohw.go.kr/")
    soup = BeautifulSoup(webpage.content, "html.parser")

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
    
    regions = soup.select("#main_maplayout > button")
    for i in range(0, len(regions)): regions[i] = bs2dict(regions[i])

    print("누적 확진: " + all_confirmed_person)
    print("일일 확진: " + today_confirmed_person)
    print("누적 격리해제: " + all_quarantine_release)
    print("일일 격리해제: " + today_quarantine_release)
    print("누적 치료 중: " + all_cure)
    print("일일 치료 중: " + today_cure)
    print("누적 사망자: " + all_die)
    print("일일 사망자: " + today_die)

    f = open("data.json", "w")
    f.write(f"""{{"all_confirmed_person\" : \"{all_confirmed_person}\", \"today_confirmed_person\" : \"{today_confirmed_person}\",
        \"all_quarantine_release\" : \"{all_quarantine_release}\", \"today_quarantine_release\" : \"{today_quarantine_release}\",
        \"all_cure\" : \"{all_cure}\",\"today_cure\" : \"{today_cure}\",
        \"all_die\" : \"{all_die}\", \"today_die\" : \"{today_die}\",
        [
            {{"num": \"{regions[0]}\", ""}}
        ]}}""")
    f.close()

    os.system("git commit -am \"update\"")
    os.system("git push -u origin main")

task()

while True:
    schedule.every().day.do(task)