from requests_oauthlib import OAuth1Session
import json
import deepl
import os

# 各種認証情報の読み込み
consumer_key = "your app key"
consumer_secret = "your app secret"
resource_owner_key = "your account key"
resource_owner_secret = "your account securet"
deepl_auth_key = "your api key"


def repost_tweet(request):
    # リクエストの分解
    data = request.get_json()
    tweet_text = data.get('text')

    # 入力した文字列を翻訳
    translator = deepl.Translator(deepl_auth_key)
    result = translator.translate_text(tweet_text, target_lang="EN-US")
    payload = {"text": result.text}

    # セッション作成
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret,
    )

    # リクエスト作成
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )

    if response.status_code != 201:
        print("Request returned an error: {} {}".format(
            response.status_code, response.text))
        return "NG"

    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))

    return "OK"
