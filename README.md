# pokepulse_TCG
Pokemon TCG market price dashboard built with Python and Power BI

## What it does
- Pulls live card price data from the pokemontcg.io API
- Tracks 563+ cards across Base Set, Scarlet & Violet, and Sword & Shield
- Visualizes market prices, rarity breakdowns, and top valuable cards

## Tech stack
- **Python** — API data collection (requests, pandas)
- **Power BI** — Interactive dashboard with custom dark theme
- **Data source** — pokemontcg.io (TCGPlayer price data)

## Dashboard features
- KPI cards: avg price, total cards, max/min price
- Avg market price by rarity (bar chart)
- Top 10 most valuable cards (table)
- Price range scatter plot by rarity

## How to run
1. Install dependencies: `pip install requests pandas`
2. Run `python fetch_cards.py` to fetch latest prices
3. Open `PokePulse.pbix` in Power BI Desktop
4. Refresh data source to point to your local `cards.csv`
