@echo off
color 0a
:loop
echo launching...
start "tgbot1exp" python "C:\Users\user\PycharmProjects\tgbot1exp\main.py"

echo waiting 600 sec...
timeout /t 600 >nul

echo enging...
taskkill /f /im python.exe >nul 2>&1

echo reloading...
goto loop