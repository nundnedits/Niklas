@echo off
cd /d %~dp0
pip install -r requirements.txt

:restart
python main.py
echo.
echo Bot wurde beendet oder ist abgestuerzt - Neustart in 10 Sekunden...
echo (Fenster schliessen, um den Bot wirklich zu stoppen)
timeout /t 10
goto restart
