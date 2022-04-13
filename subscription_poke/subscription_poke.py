import requests
import scraping
from bs4 import BeautifulSoup


def parse_html(selector, url):
    driver = scraping.scrape(selector, url)
    return BeautifulSoup(driver.page_source, "html.parser")


def crawl(selector, url):
    soup = parse_html(selector, url)

    # 最新情報
    news_list = soup.find_all("div", class_="news-list__element")
    print(news_list)

    results = []

    for news in news_list:
        link = "https://www.pokemon.co.jp" + news.find("a", class_="news-list__links")["href"]
        img = news.find("img")["src"]
        title = news.find("div", class_="news-list__title").text
        results.append((link, img, title))

    return results


def send_message(token, tpl):

    headers = {
        # 各自発行したトークンを記述
        "Authorization": "Bearer "
        + token
    }

    icon_image = tpl[1]

    text = "よーがポケモン最新情報の更新をお知らせします！" + "\n" + tpl[2] + "\n" + "詳細はこちら↓\n" + tpl[0]
    files = {
        "message": (None, text),
        "imageFullsize": (None, icon_image),
        "imageThumbnail": (None, icon_image),
    }

    requests.post("https://notify-api.line.me/api/notify", headers=headers, files=files)
