"""
Einmaliger Bot-Durchlauf für geplante Ausführung (z.B. GitHub Actions).

Im Unterschied zu main.py läuft das NICHT in einer Endlosschleife - es
prüft einmal auf neue Angebote und beendet sich danach. Den Zeitplan
(z.B. alle 15 Minuten) übernimmt die GitHub-Actions-Workflow-Datei.
"""
from main import durchlauf

if __name__ == "__main__":
    durchlauf()
