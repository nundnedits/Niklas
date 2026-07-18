import os

# Discord Webhook-URL: Discord -> Servereinstellungen -> Integrationen -> Webhooks -> Neuer Webhook
# Am besten NICHT hart im Code speichern, sondern als Umgebungsvariable setzen.
DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL", "HIER_WEBHOOK_URL_EINTRAGEN")

# Mindestmarge, ab der ein Angebot gemeldet wird (3.0 = mind. dreifacher Nettoerlös)
MINDEST_MARGE = 3.0

# Geschätzte Verkaufsgebühren (z.B. eBay ~12%) und dein eigener Versand beim Weiterverkauf
VERKAUFSGEBUEHREN_PROZENT = 0.12
EIGENER_VERSAND = 4.99

# Suchbegriffe für Kleinanzeigen
KLEINANZEIGEN_SUCHBEGRIFFE = ["lego star wars"]

# Suchbegriffe für eBay.de (Sofort-Kaufen-Angebote)
EBAY_SUCHBEGRIFFE = ["lego star wars"]

# Kaufland.de Kategorie-/Suchseiten, die durchsucht werden sollen
KAUFLAND_URLS = [
    "https://www.kaufland.de/t/lego/lego-star-wars/~18761/",
]

# PriceCharting API-Key für Nintendo-Spielewerte (kostenlos registrieren:
# https://www.pricecharting.com/api-documentation)
PRICECHARTING_API_KEY = os.environ.get("PRICECHARTING_API_KEY", "HIER_API_KEY_EINTRAGEN")

# Grobe USD->EUR Näherung für PriceCharting-Preise (die sind in USD!).
# Kein Live-Kurs - gelegentlich manuell aktualisieren.
USD_ZU_EUR_KURS = 0.92

# Suchbegriffe für Nintendo-Spiele (eBay + Kleinanzeigen), alle Plattformen/Ären
NINTENDO_SUCHBEGRIFFE = ["nintendo spiel"]

# Wie oft der Bot neue Angebote sucht, in Sekunden (900 = alle 15 Minuten)
CHECK_INTERVALL_SEKUNDEN = 900

# Datei, in der bereits gemeldete Angebote gespeichert werden (gegen Doppel-Alerts)
SEEN_DATEI = "seen_angebote.json"
