# cloudflare-adblock

## What is this

Cloudflare Zero TrustのGateway Firewall Policyの機能を使って、ポップアップ広告に使われるドメインリストに対するDNSクエリをブロックする。  
Cloudflare WARPなどのクライアントを使ってZero Trustを噛ませると、アドブロックとして機能する。

## How to use

```sh
# Setup

$ export CLOUDFLARE_ACCOUNT_ID=...
$ export CLOUDFLARE_EMAIL=...
$ export CLOUDFLARE_API_KEY=...

$ python3 -m venv .venv
$ . .venv/bin/activate
$ pip install -r requirements.txt

# Create domain lists

$ python3 create_domain_lists.py

# Get created domain list ids

$ . get_list_ids.sh

# Create rule

$ python3 create_adblock_rule.py
```
