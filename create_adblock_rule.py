import requests
import json
import os

# APIの設定
ACCOUNT_ID = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
AUTH_EMAIL = os.environ.get("CLOUDFLARE_EMAIL")
AUTH_KEY = os.environ.get("CLOUDFLARE_API_KEY")
api_url = f"https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/gateway/rules/"

# ヘッダーの設定
headers = {
    "X-Auth-Email": AUTH_EMAIL,
    "X-Auth-Key": AUTH_KEY,
    "Content-Type": "application/json"
}

txt_file = "list_ids.txt"

with open(txt_file, 'r') as file:
    traffic_rule = ' or '.join(f"any(dns.domains[*] in ${line.strip()})" for line in file)

# リクエストボディの設定
payload = {
    "name": "AdBlock",
    "description": "Block DNS requests to known ad domains.",
    "precedence": 10000,
    "enabled": True,
    "action": "block",
    "filters": ["dns"],
    "traffic": traffic_rule,
    "rule_settings": {
        "block_page_enabled": False,
        "block_reason": "",
        "override_ips": None,
        "override_host": "",
        "l4override": None,
        "biso_admin_controls": None,
        "add_headers": None,
        "ip_categories": False,
        "ip_indicator_feeds": False,
        "check_session": None,
        "insecure_disable_dnssec_validation": False
    }
}

# PUTリクエストの送信
response = requests.post(api_url, headers=headers, data=json.dumps(payload))

# レスポンスの確認
if response.status_code == 200:
    print("Success:", response.json())
else:
    print("Error:", response.status_code)
    print(response.text)
