@echo off
echo ========================================
echo   Hogwarts Sorting Hat - Web App
echo   Starting Backend and Frontend...
echo ========================================
echo.

REM Check if required folders exist
if not exist "backend" (
    echo ERROR: backend folder not found!
    pause
    exit /b 1
)

if not exist "frontend" (
    echo ERROR: frontend folder not found!
    pause
    exit /b 1
)

echo Starting Flask Backend...
start "Flask Backend" cmd /k "cd backend && venv\Scripts\activate && python app.py"

echo Waiting 3 seconds for backend to start...
timeout /t 3 /nobreak >nul

echo Starting Vite Frontend...
start "Vite Frontend" cmd /k "cd frontend && npm run dev"

echo.
echo ========================================
echo   Both servers are starting!
echo.
echo   Backend:  http://localhost:5000
echo   Frontend: http://localhost:3000
echo.
echo   Open your browser to:
echo   http://localhost:3000
echo.
echo   Press any key to close this window
echo   (Servers will keep running)
echo ========================================
pause >nul
