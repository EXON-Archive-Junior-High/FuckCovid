from bs4 import BeautifulSoup
import requests
import time
import os, sys

def convert2today(str): return str.split("(+ ")[1].split(")")[0]
def getNum(o): return o.select_one("button > span.num").get_text()
def getBefore(o): return o.select_one("button > span.before").get_text().replace("(", "").replace(")", "").replace("+", "")
def bs2dict(region): return { "num": getNum(region), "before": getBefore(region) }
def dict2json(o): return f"""{{"num": "{o["num"]}", "before":"{o["before"]}"}}"""
def jsonFor(o):
    string = ""
    for i in range(0, 18): string += f"{dict2json(o[i])},"
    return string[:-1]

def task():
    os.system("git pull origin main")
    webpage = requests.get("http://ncov.mohw.go.kr/")
    soup = BeautifulSoup(webpage.content, "html.parser")

    all_confirmed_person = soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(1) > span.num").get_text().split(")")[1]
    today_confirmed_person = convert2today(soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(1) > span.before").get_text())
    all_quarantine_release = soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(2) > span.num").get_text()
    today_quarantine_release = convert2today(soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(2) > span.before").get_text())
    all_cure = soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(3) > span.num").get_text()
    today_cure = convert2today(soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(3) > span.before").get_text())
    all_die = soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(4) > span.num").get_text()
    today_die = convert2today(soup.select_one("body > div > div.mainlive_container > div.container > div > div.liveboard_layout > div.liveNumOuter > div.liveNum > ul > li:nth-child(4) > span.before").get_text())
    
    old_regions = soup.select("#main_maplayout > button")
    new_regions = []
    for i in range(0, 18): new_regions.append(bs2dict(old_regions[i]))

    f = open("data.json", "w")
    f.write(f"""{{
        "all_confirmed_person" : "{all_confirmed_person}", "today_confirmed_person" : "{today_confirmed_person}",
        "all_quarantine_release" : "{all_quarantine_release}", "today_quarantine_release" : "{today_quarantine_release}",
        "all_cure" : "{all_cure}","today_cure" : "{today_cure}",
        "all_die" : "{all_die}", "today_die" : "{today_die}",
        "regions" : [{jsonFor(new_regions)}]
        }}""")
    f.close()

    os.system("git commit -am \"update\"")
    os.system("git push origin main")

while True:
    task()
    time.sleep(86400)