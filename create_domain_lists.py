import os
import requests
import json

# APIの設定
ACCOUNT_ID = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
AUTH_EMAIL = os.environ.get("CLOUDFLARE_EMAIL")
AUTH_KEY = os.environ.get("CLOUDFLARE_API_KEY")
api_url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/gateway/lists"

# ヘッダーの設定
headers = {
    "X-Auth-Email": AUTH_EMAIL,
    "X-Auth-Key": AUTH_KEY,
    "Content-Type": "application/json"
}

# 'popup_ads_list.txt' ファイルを読み込む
txt_file = 'popup_ads_list.txt'

if os.path.exists(txt_file):
    with open(txt_file, 'r') as file:
        lines = file.readlines()

    # 1000行ごとにリクエストを分割
    for i in range(0, len(lines), 1000):
        chunk = lines[i:i+1000]

        # リクエストボディの作成
        payload = {
            "description": "Pop-Up Ads Block list",
            "items": [{"value": line.strip()} for line in chunk],
            "name": f"Pop-Up Ads Block list {i//1000 + 1}",
            "type": "DOMAIN"
        }

        # APIリクエストの送信
        response = requests.post(
            api_url, headers=headers, data=json.dumps(payload))

        # レスポンスの確認
        if response.status_code == 200:
            print(f"Success: Chunk {i//1000 + 1}")
        else:
            print(f"Error: Chunk {i//1000 + 1}")
            print(response.text)
else:
    print("No .txt file found in the current directory.")
