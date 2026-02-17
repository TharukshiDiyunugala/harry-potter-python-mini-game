# 🎩⚡ Hogwarts Sorting Hat Ceremony - Modern Web App

A beautiful, modern Harry Potter Sorting Hat game built with **Flask** backend and **Vue.js** frontend!

![Harry Potter](https://img.shields.io/badge/Harry%20Potter-Themed-gold)
![Flask](https://img.shields.io/badge/Backend-Flask-blue)
![Vue.js](https://img.shields.io/badge/Frontend-Vue.js-green)

## ✨ Features

### 🎨 Beautiful Modern UI
- **Responsive Design** - Works on desktop, tablet, and mobile
- **Smooth Animations** - GSAP-powered transitions and effects
- **Interactive Elements** - Magical particles, floating effects, glowing buttons
- **House-Themed Colors** - Custom styling for each Hogwarts house

### 🎮 Game Features
- **Welcome Screen** - Animated sorting hat with spinning effects
- **Name Entry** - Interactive input with magical sparkles and owl helper
- **Sorting Ceremony** - Dramatic sorting animation with thinking effects
- **House Results** - House-specific backgrounds, particles, and celebrations
- **Triwizard Maze** - Playable maze game with keyboard controls
- **Background Music** - Toggle-able music control

### 🏰 Four Hogwarts Houses
- 🦁 **Gryffindor** - Brave, daring, and chivalrous
- 🦡 **Hufflepuff** - Loyal, patient, and hardworking
- 🦅 **Ravenclaw** - Wise, witty, and clever
- 🐍 **Slytherin** - Ambitious, cunning, and resourceful

## 🚀 Quick Start

### Prerequisites
- **Python 3.8+** installed
- **Node.js 16+** installed
- **npm** or **yarn** package manager

### Installation

#### 1️⃣ Backend Setup (Flask)

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 2️⃣ Frontend Setup (Vue.js)

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

### Running the Application

You need to run **both backend and frontend** simultaneously:

#### Terminal 1 - Backend (Flask)
```bash
cd backend
python app.py
```
Backend will run on: **http://localhost:5000**

#### Terminal 2 - Frontend (Vue.js Development Server)
```bash
cd frontend
npm run dev
```
Frontend will run on: **http://localhost:3000**

**🌐 Open your browser and visit: http://localhost:3000**

## 📦 Production Build

### Build Frontend for Production
```bash
cd frontend
npm run build
```

This creates optimized files in `frontend/dist/` which Flask will serve automatically.

### Run Production Mode
```bash
cd backend
python app.py
```

Visit: **http://localhost:5000** (Flask serves the built Vue.js app)

## 🎯 Project Structure

```
HP Game/
├── backend/
│   ├── app.py                 # Flask server & API endpoints
│   └── requirements.txt       # Python dependencies
│
├── frontend/
│   ├── public/
│   │   └── index.html        # HTML template
│   ├── src/
│   │   ├── components/
│   │   │   ├── WelcomeScreen.vue    # Welcome/start screen
│   │   │   ├── NameEntry.vue        # Name input screen
│   │   │   ├── SortingScreen.vue    # Sorting animation
│   │   │   ├── ResultScreen.vue     # House result display
│   │   │   └── MazeGame.vue         # Triwizard maze game
│   │   ├── App.vue           # Main Vue app component
│   │   ├── main.js          # Vue app entry point
│   │   └── style.css        # Global styles
│   ├── package.json          # Node dependencies
│   └── vite.config.js       # Vite configuration
│
├── assets/                   # Game assets (images, sounds)
└── sorting_hat_backup.py     # Original Python/tkinter version
```

## 🛠️ Technology Stack

### Backend
- **Flask 3.0** - Lightweight Python web framework
- **Flask-CORS** - Cross-Origin Resource Sharing support
- **Python 3.8+** - Core backend logic

### Frontend
- **Vue.js 3** - Progressive JavaScript framework
- **Vite** - Next-generation frontend tooling
- **Axios** - HTTP client for API calls
- **GSAP** - Professional-grade animation library
- **Custom CSS** - Beautiful UI with animations

## 🎨 Features Breakdown

### 1. Welcome Screen
- Animated floating and spinning sorting hat
- House emoji previews with bounce animations
- Shimmer text effects
- Professional welcome card with gradient backgrounds

### 2. Name Entry
- Magical input field with sparkles
- Animated owl helper with speech bubble
- Real-time character animations
- Keyboard (Enter) and button submission

### 3. Sorting Screen
- Thinking hat animation (rotating and scaling)
- Dynamic message with animated dots
- Energy rings expanding effect
- 3-second dramatic sorting process

### 4. Result Screen
- House-specific gradient backgrounds
- Explosion effect on reveal
- Rotating house emblem
- House-colored floating particles
- Congratulations with all house information
- Action buttons for maze and restart

### 5. Maze Game
- Procedurally generated maze (15x15)
- Keyboard controls (Arrow keys)
- Player wizard icon (🧙)
- Glowing trophy exit (🏆)
- Win modal with celebrations
- Forbidden Forest themed styling

## 🔧 API Endpoints

### `GET /api/houses`
Get all house information
```json
{
  "success": true,
  "houses": {
    "Gryffindor": { ... },
    "Hufflepuff": { ... },
    "Ravenclaw": { ... },
    "Slytherin": { ... }
  }
}
```

### `POST /api/sort`
Sort a student into a house
```json
// Request
{
  "name": "Harry Potter"
}

// Response
{
  "success": true,
  "name": "Harry Potter",
  "house": "Gryffindor",
  "houseInfo": { ... }
}
```

### `GET /api/maze/generate?size=15`
Generate a random maze
```json
{
  "success": true,
  "maze": [[1,0,1,...], ...],
  "size": 15,
  "start": [1, 1],
  "end": [13, 13]
}
```

## 🎭 Customization

### Change House Colors
Edit colors in:
- `backend/app.py` - HOUSE_INFO dictionary
- `frontend/src/style.css` - CSS variables

### Modify Animations
- Component-specific animations: `frontend/src/components/*.vue`
- Global animations: `frontend/src/style.css`

### Add Sound Effects
Update the music toggle function in `App.vue`:
```javascript
const toggleMusic = () => {
  musicPlaying.value = !musicPlaying.value
  // Add your audio logic here
  const audio = new Audio('/assets/theme.mp3')
  if (musicPlaying.value) {
    audio.play()
  } else {
    audio.pause()
  }
}
```

## 🐛 Troubleshooting

### Backend not starting?
```bash
# Make sure virtual environment is activated
# Reinstall dependencies
pip install -r requirements.txt
```

### Frontend not loading?
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### CORS errors?
- Make sure backend is running on port 5000
- Check `vite.config.js` proxy settings
- Verify Flask-CORS is installed

### Maze not working?
- Click on the maze grid to focus it
- Ensure you're using arrow keys (not WASD)
- Check browser console for errors

## 📝 Development Tips

### Hot Reload
Both Flask (debug mode) and Vite support hot reload:
- Frontend changes update instantly
- Backend changes restart Flask automatically

### Browser DevTools
- Press F12 to open developer tools
- Check Console for errors
- Use Vue DevTools extension for component inspection

## 🎓 Learning Resources

### Flask
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

### Vue.js
- [Vue.js 3 Documentation](https://vuejs.org/)
- [Vue.js Tutorial](https://vuejs.org/tutorial/)

### Vite
- [Vite Documentation](https://vitejs.dev/)

## 🌟 Future Enhancements

Possible additions:
- [ ] User authentication and save sorting results
- [ ] Multiplayer maze racing
- [ ] House points system
- [ ] Spell casting mini-games
- [ ] Leaderboard for maze completion times
- [ ] More houses (Ilvermorny, etc.)
- [ ] Character customization
- [ ] Sound effects and background music
- [ ] Social sharing of results

## 📜 License

This is a fan-made educational project. Harry Potter is a trademark of Warner Bros.

## 🙏 Credits

- **J.K. Rowling** - Harry Potter universe
- **Warner Bros** - Harry Potter franchise
- **Original Game** - Your tkinter version
- **Modern Version** - Flask + Vue.js transformation

---

**May magic be with you always! ✨🎩⚡**

*Enjoy your magical sorting ceremony!*
