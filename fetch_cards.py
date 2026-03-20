import requests
import pandas as pd
from datetime import date

BASE = "https://api.pokemontcg.io/v2"

def fetch_cards(set_id):
    cards = []
    page = 1
    while True:
        r = requests.get(f"{BASE}/cards", params={"q": f"set.id:{set_id}", "page": page, "pageSize": 250})
        data = r.json()
        cards += data["data"]
        if len(data["data"]) < 250:
            break
        page += 1
    return cards

rows = []
for set_id in ["sv1", "swsh4", "base1"]:
    print(f"Fetching {set_id}...")
    for c in fetch_cards(set_id):
        prices = c.get("tcgplayer", {}).get("prices", {})
        p = prices.get("holofoil") or prices.get("normal") or {}
        rows.append({
            "card_id":       c["id"],
            "name":          c["name"],
            "set_id":        c["set"]["id"],
            "set_name":      c["set"]["name"],
            "series":        c["set"]["series"],
            "rarity":        c.get("rarity", "Unknown"),
            "snapshot_date": str(date.today()),
            "price_low":     p.get("low"),
            "price_mid":     p.get("mid"),
            "price_market":  p.get("market"),
            "price_high":    p.get("high"),
        })

df = pd.DataFrame(rows)
df.to_csv("cards.csv", index=False)
print(f"Done — {len(df)} cards saved to cards.csv")