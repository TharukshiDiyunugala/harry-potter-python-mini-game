# 🎯 Quick Setup Guide

## For Beginners - Step-by-Step Instructions

### Step 1: Install Prerequisites

#### Install Python (if not already installed)
1. Visit https://www.python.org/downloads/
2. Download Python 3.8 or higher
3. During installation, **CHECK** "Add Python to PATH"
4. Verify installation:
   ```bash
   python --version
   ```

#### Install Node.js (if not already installed)
1. Visit https://nodejs.org/
2. Download the LTS (Long Term Support) version
3. Install with default settings
4. Verify installation:
   ```bash
   node --version
   npm --version
   ```

### Step 2: Setup Backend

Open Command Prompt or PowerShell and navigate to your project:

```bash
# Navigate to project folder
cd "E:\HP Game"

# Go to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# You should see (venv) before your prompt now

# Install Flask and dependencies
pip install -r requirements.txt
```

### Step 3: Setup Frontend

Open a **NEW** Command Prompt/PowerShell window:

```bash
# Navigate to project folder
cd "E:\HP Game"

# Go to frontend folder
cd frontend

# Install Node.js dependencies (this may take a few minutes)
npm install
```

### Step 4: Run the Application

You need **TWO terminal windows** open:

#### Terminal Window 1 - Backend
```bash
cd "E:\HP Game\backend"
venv\Scripts\activate    # Activate virtual environment
python app.py
```

You should see:
```
🎩 Starting Hogwarts Sorting Hat Backend...
🌐 Backend running at: http://localhost:5000
```

#### Terminal Window 2 - Frontend
```bash
cd "E:\HP Game\frontend"
npm run dev
```

You should see:
```
  VITE v5.x.x  ready in xxx ms

  ➜  Local:   http://localhost:3000/
```

### Step 5: Open in Browser

Open your web browser and visit:
```
http://localhost:3000
```

🎉 **You should now see the Hogwarts Sorting Hat game!**

---

## Common Issues & Solutions

### Issue: "python is not recognized"
**Solution:** Python not added to PATH. Reinstall Python and check "Add to PATH"

### Issue: "npm is not recognized"
**Solution:** Node.js not installed or not in PATH. Reinstall Node.js

### Issue: "Cannot activate venv"
**Solution (Windows):** Run PowerShell as Administrator and execute:
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: "Port 5000 already in use"
**Solution:** Another app is using port 5000. Either:
1. Stop that app, OR
2. Change port in `backend/app.py`:
   ```python
   app.run(debug=True, port=5001)  # Change to 5001
   ```

### Issue: Frontend shows blank page
**Solution:** 
1. Check browser console (F12) for errors
2. Verify backend is running (should see messages in terminal)
3. Try clearing browser cache
4. Restart both backend and frontend

### Issue: CORS errors in browser console
**Solution:** 
1. Make sure Flask backend is running on port 5000
2. Verify Flask-CORS is installed: `pip install flask-cors`

---

## Stopping the Application

### To stop the backend:
Press `Ctrl + C` in the backend terminal window

### To stop the frontend:
Press `Ctrl + C` in the frontend terminal window

---

## Running Again Later

### Quick Start (after initial setup)

**Terminal 1:**
```bash
cd "E:\HP Game\backend"
venv\Scripts\activate
python app.py
```

**Terminal 2:**
```bash
cd "E:\HP Game\frontend"
npm run dev
```

**Browser:**
Visit `http://localhost:3000`

---

## Production Build (Optional)

To create a production-ready version:

```bash
# Build frontend
cd frontend
npm run build

# This creates optimized files in frontend/dist/

# Now just run backend:
cd ../backend
venv\Scripts\activate
python app.py

# Visit http://localhost:5000
# Flask will serve the built Vue.js app
```

---

## Video Tutorial Format

If you want to create a video, here's the flow:

1. **Show prerequisites** (2 min)
   - Check if Python is installed
   - Check if Node.js is installed

2. **Backend setup** (3 min)
   - Create venv
   - Install dependencies
   - Show requirements.txt

3. **Frontend setup** (3 min)
   - Install npm packages
   - Show package.json structure

4. **Running the app** (2 min)
   - Start backend in terminal 1
   - Start frontend in terminal 2
   - Open browser

5. **Demo the game** (5 min)
   - Welcome screen
   - Enter name
   - Sorting ceremony
   - Result display
   - Try the maze

Total: ~15 minutes

---

## Need Help?

1. **Check console** - Look for error messages
2. **Google the error** - Most common issues have solutions online
3. **Check versions** - Ensure Python 3.8+ and Node 16+
4. **Restart** - Sometimes a fresh start helps!

---

**Happy Coding! 🎩✨**
