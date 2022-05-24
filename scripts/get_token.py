from requests_oauthlib import OAuth1Session
import os

"""
## このスクリプトの用途
アカウントの認証情報を取得する。

## 方法
Developer Portal でアプリを取得しただけでは、特定のアカウントとして呟く権限がない。
特定のアカウントとして呟くために、そのアカウントがわから許可をしてもらい、その認証情報を取得する必要がある。
このスクリプトを実行するとurlがconsoleに出力される
urlをターゲットとしているアカウントでログインしているブラウザに入力、許可すると数字が出てくるのでコンソールに入力。
認証情報が手に入るのでそれを post_tweet.py に追加。
"""

consumer_key = "your app key"
consumer_secret = "your app secret"

# Get request token
request_token_url = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret)

try:
    fetch_response = oauth.fetch_request_token(request_token_url)
except ValueError:
    print(
        "There may have been an issue with the consumer_key or consumer_secret you entered."
    )

resource_owner_key = fetch_response.get("oauth_token")
resource_owner_secret = fetch_response.get("oauth_token_secret")
print("Got OAuth token: %s" % resource_owner_key)

# Get authorization
base_authorization_url = "https://api.twitter.com/oauth/authorize"
authorization_url = oauth.authorization_url(base_authorization_url)
print("Please go here and authorize: %s" % authorization_url)
verifier = input("Paste the PIN here: ")

# Get the access token
access_token_url = "https://api.twitter.com/oauth/access_token"
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    verifier=verifier,
)
oauth_tokens = oauth.fetch_access_token(access_token_url)

print(oauth_tokens)
