import requests
import re

USERNAME = "mario-alimenti"  # <-- Cambia con il tuo username Credly
README_PATH = "README.md"

# Recupera dati dei badge
url = f"https://www.credly.com/users/{USERNAME}/badges.json"
r = requests.get(url)
if r.status_code != 200:
    raise SystemExit(f"Errore nel recupero dei badge: {r.status_code}")

data = r.json().get("data", [])
badges = []

for b in data:
    name = b["badge_template"]["name"]
    img = b["badge_template"]["image"]["url"]
    badge_id = b["id"]
    link = f"https://www.credly.com/badges/{badge_id}"
    badges.append(f"[![{name}]({img})]({link})")

# Leggi il README e sostituisci la sezione
with open(README_PATH, "r") as f:
    content = f.read()

new_section = "\n".join(badges)
pattern = r"<!-- badges-start -->(.*?)<!-- badges-end -->"
replacement = f"<!-- badges-start -->\n{new_section}\n<!-- badges-end -->"
updated = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(README_PATH, "w") as f:
    f.write(updated)

print("✅ Sezione badge aggiornata!")
