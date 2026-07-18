# Lego Deal-Bot

## Einrichtung

1. Python 3.10+ installieren, dann im Ordner:
   ```
   pip install -r requirements.txt
   ```

2. Discord-Webhook anlegen:
   Discord-Server -> Servereinstellungen -> Integrationen -> Webhooks -> Neuer Webhook -> URL kopieren.

3. In `config.py`:
   - `DISCORD_WEBHOOK_URL` eintragen (oder als Umgebungsvariable `DISCORD_WEBHOOK_URL` setzen)
   - `KLEINANZEIGEN_SUCHBEGRIFFE` / `EBAY_SUCHBEGRIFFE` / `NINTENDO_SUCHBEGRIFFE` anpassen
   - `PRICECHARTING_API_KEY` eintragen für die Nintendo-Nische (kostenlos hier registrieren:
     https://www.pricecharting.com/api-documentation)

4. **Wichtig - vor dem ersten Start prüfen/anpassen:**
   - `kleinanzeigen_scraper.py`: CSS-Selektoren gegen die aktuelle Seite prüfen
     (Kleinanzeigen ändert sein HTML gelegentlich)
   - `shop_scraper.py`: Selektoren an deine gewählte Shop-Seite anpassen
     (siehe Kommentare in der Datei)
   - `brickeconomy_client.py`: Selektor für den Wert-Preis ggf. anpassen

5. Starten:
   ```
   python main.py
   ```
   Der Bot läuft dauerhaft und prüft alle `CHECK_INTERVALL_SEKUNDEN`
   (Standard: 15 Minuten) neue Angebote.

## Automatisch laufen lassen mit GitHub Actions (kostenlos, kein eigener PC nötig)

1. Kostenloses Konto auf [github.com](https://github.com) erstellen (falls noch nicht vorhanden).
2. Neues Repository erstellen (Button "New" auf der GitHub-Startseite) - am besten **privat** stellen.
3. Alle Dateien aus diesem Ordner hochladen: im Repository auf "Add file" → "Upload files" → alle Dateien (inkl. dem versteckten `.github`-Ordner!) reinziehen → "Commit changes".
   - Falls der `.github`-Ordner beim Hochladen nicht mitkommt: Im Repository auf "Add file" → "Create new file" → als Dateiname `.github/workflows/deal-bot.yml` eintragen → Inhalt der Datei reinkopieren.
4. Secrets eintragen (das sind deine geheimen Zugangsdaten, die NICHT im Code stehen dürfen):
   Repository → "Settings" → "Secrets and variables" → "Actions" → "New repository secret":
   - Name: `DISCORD_WEBHOOK_URL`, Wert: deine Webhook-URL
   - Name: `PRICECHARTING_API_KEY`, Wert: dein PriceCharting-Key
5. Schreibrechte aktivieren, damit der Bot seine "gesehen"-Liste speichern darf:
   "Settings" → "Actions" → "General" → runter scrollen zu "Workflow permissions" →
   "Read and write permissions" auswählen → "Save".
6. Fertig - der Bot läuft jetzt automatisch alle 15 Minuten. Zum sofortigen Testen:
   Tab "Actions" → "Deal-Bot Check" → Button "Run workflow".

Ergebnis siehst du im "Actions"-Tab bei jedem Durchlauf (grüner Haken = lief durch,
rotes X = Fehler, dann auf den Durchlauf klicken für die Logs).

## Wichtige Einschränkungen

- Alle drei Datenquellen (Kleinanzeigen, BrickEconomy, Shop) werden per
  Scraping ausgelesen, nicht über offizielle APIs. Das heißt:
  - Es kann jederzeit brechen, wenn die Seiten ihr HTML ändern (Selektoren
    dann in der jeweiligen Datei anpassen).
  - Es kann gegen die Nutzungsbedingungen der jeweiligen Seite verstoßen,
    v.a. bei Kleinanzeigen. Nutze niedrige Frequenz (nicht unter dem
    Standardintervall) und nur für den persönlichen Gebrauch.
- Das Set-Nummer-Erkennungsmuster (Regex `\d{4,5}`) ist eine Heuristik -
  bei privaten Kleinanzeigen-Inseraten steht die Set-Nummer nicht immer
  im Titel, dann wird das Angebot übersprungen statt falsch bewertet.
- Verkauf ist in dieser Version NICHT automatisiert - der Bot meldet nur
  Deals in Discord, du kaufst/verkaufst weiterhin selbst.

## Nintendo-Nische: zusätzliche Einschränkungen

- Spiele haben (anders als Lego-Sets) keine eindeutige ID im Anzeigentitel.
  Die Zuordnung zum Marktwert läuft über Titel-Ähnlichkeitsabgleich gegen
  PriceCharting - das ist fehleranfälliger als die Lego-Set-Nummer-Logik.
  Prüf gemeldete Nintendo-Deals lieber nochmal manuell, bevor du kaufst.
- Der erkannte Zustand ("neu"/"cib"/"lose") basiert nur auf Schlagworten im
  Titel. Wenn nichts erkannt wird, rechnet der Bot konservativ mit dem
  niedrigeren "lose"-Preis.
- PriceCharting-Preise sind in US-Dollar und werden mit einem statischen,
  ungefähren Kurs (`USD_ZU_EUR_KURS` in config.py) umgerechnet - kein
  Live-Wechselkurs, gelegentlich manuell aktualisieren.
- Bei wertvollen alten Modulen (SNES, N64 etc.) gibt es ein reales
  Fälschungs-/Repro-Risiko, das der Bot nicht erkennen kann.
