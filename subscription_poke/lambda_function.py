import pickle
import boto3
import subscription_poke

# バケット名, オブジェクトキー
BUCKET_NAME = "pokewebforjun"
KEY = "latest.pkl"

# PokemonサイトURL, LINEトークン
URL = "https://www.pokemon.co.jp/info/cat_game/"
TOKEN = "YOUR_TOKEN"

# 取得するCSSセレクタ
SELECTOR = "div.news-list__element"

s3 = boto3.resource("s3")
obj = s3.Object(BUCKET_NAME, KEY)


def lambda_handler(event, context):
    latest = pickle.loads(obj.get()["Body"].read())

    results = subscription_poke.crawl(SELECTOR, URL)
    if latest == results:
        print("最新情報の更新なし")
        return
    else:
        obj.delete()
        difs = list(set(results) - set(latest))
        difs.reverse()
        for dif in difs:
            subscription_poke.send_message(TOKEN, dif)
        obj.put(Body=pickle.dumps(results))
        return
