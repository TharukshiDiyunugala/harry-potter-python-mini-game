<template>
  <div class="maze-game">
    <div class="maze-container">
      <!-- Title -->
      <h1 class="maze-title text-shimmer">🌟 THE TRIWIZARD MAZE 🌟</h1>

      <!-- Game Status and Controls -->
      <div v-if="!gameWon" class="game-header">
        <div class="maze-instructions">
          <p>🎮 Use <strong>Arrow Keys</strong> (⬆️⬇️⬅️➡️) or <strong>WASD</strong> to navigate</p>
          <p>🎯 Find the <strong>Triwizard Cup</strong> 🏆 to win!</p>
        </div>
        
        <div class="game-stats">
          <div class="stat">
            <span class="stat-label">👣 Moves:</span>
            <span class="stat-value">{{ moveCount }}</span>
          </div>
          <div class="stat">
            <span class="stat-label">⏱️ Time:</span>
            <span class="stat-value">{{ formattedTime }}</span>
          </div>
        </div>
      </div>

      <!-- Maze Grid -->
      <div class="maze-grid" ref="mazeGrid" tabindex="0" @keydown="handleKeyPress">
        <div class="maze-row" v-for="(row, y) in maze" :key="y">
          <div 
            v-for="(cell, x) in row" 
            :key="`${x}-${y}`"
            class="maze-cell"
            :class="{
              'wall': cell === 1,
              'path': cell === 0,
              'player': playerPos.x === x && playerPos.y === y,
              'exit': exitPos.x === x && exitPos.y === y
            }"
          >
            <span v-if="playerPos.x === x && playerPos.y === y" class="player-icon">🧙</span>
            <span v-else-if="exitPos.x === x && exitPos.y === y" class="exit-icon">🏆</span>
          </div>
        </div>
      </div>

      <!-- Win Modal -->
      <div v-if="gameWon" class="win-modal">
        <div class="win-content">
          <h2 class="win-title">🎉 CONGRATULATIONS! 🎉</h2>
          <p class="win-message">
            You've successfully navigated the Triwizard Maze!
          </p>
          <div class="trophy">🏆</div>
          <p class="win-subtitle">⭐ The Triwizard Cup is yours! ⭐</p>
          <p class="champion-text">Well Done, Champion Wizard!</p>
          
          <div class="win-stats">
            <div class="win-stat">
              <span>👣 Total Moves:</span>
              <strong>{{ moveCount }}</strong>
            </div>
            <div class="win-stat">
              <span>⏱️ Time Taken:</span>
              <strong>{{ formattedTime }}</strong>
            </div>
          </div>
          
          <div class="win-buttons">
            <button class="magical-button primary-btn" @click="backToResult">
              🎯 Return to Sorting Result
            </button>
            <button class="magical-button secondary-btn" @click="resetMaze">
              🔄 Play Again
            </button>
          </div>
        </div>
      </div>

      <!-- Control Buttons -->
      <div v-if="!gameWon" class="control-buttons">
        <button class="magical-button back-button" @click="backToResult">
          ⬅️ Back to Result
        </button>
        <button class="magical-button reset-button" @click="resetMaze">
          🔄 Reset Maze
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import axios from 'axios'

export default {
  name: 'MazeGame',
  emits: ['back', 'home'],
  setup(props, { emit }) {
    const maze = ref([])
    const playerPos = ref({ x: 1, y: 1 })
    const exitPos = ref({ x: 13, y: 13 })
    const gameWon = ref(false)
    const mazeGrid = ref(null)
    const moveCount = ref(0)
    const startTime = ref(null)
    const elapsedTime = ref(0)
    const timerInterval = ref(null)

    const formattedTime = computed(() => {
      const seconds = Math.floor(elapsedTime.value / 1000)
      const minutes = Math.floor(seconds / 60)
      const secs = seconds % 60
      return `${minutes}:${secs.toString().padStart(2, '0')}`
    })

    onMounted(async () => {
      await loadMaze()
      // Focus the maze grid for keyboard events
      setTimeout(() => {
        mazeGrid.value?.focus()
      }, 100)
      
      // Start timer
      startTimer()
    })

    onUnmounted(() => {
      stopTimer()
    })

    const startTimer = () => {
      startTime.value = Date.now()
      timerInterval.value = setInterval(() => {
        elapsedTime.value = Date.now() - startTime.value
      }, 100)
    }

    const stopTimer = () => {
      if (timerInterval.value) {
        clearInterval(timerInterval.value)
        timerInterval.value = null
      }
    }

    const loadMaze = async () => {
      try {
        const response = await axios.get('/api/maze/generate?size=15')
        if (response.data.success) {
          maze.value = response.data.maze
          playerPos.value = { x: response.data.start[0], y: response.data.start[1] }
          exitPos.value = { x: response.data.end[0], y: response.data.end[1] }
        }
      } catch (error) {
        console.error('Failed to load maze:', error)
        // Generate a simple fallback maze
        generateFallbackMaze()
      }
    }

    const generateFallbackMaze = () => {
      const size = 15
      const simpleMaze = Array(size).fill(null).map(() => Array(size).fill(1))
      
      // Create a simple path
      for (let i = 1; i < size - 1; i++) {
        for (let j = 1; j < size - 1; j++) {
          if (i % 2 === 1 && j % 2 === 1) {
            simpleMaze[i][j] = 0
          }
        }
      }
      
      // Create random passages
      for (let i = 1; i < size - 1; i += 2) {
        for (let j = 1; j < size - 1; j += 2) {
          const dir = Math.random() < 0.5 ? 'h' : 'v'
          if (dir === 'h' && j < size - 2) {
            simpleMaze[i][j + 1] = 0
          } else if (dir === 'v' && i < size - 2) {
            simpleMaze[i + 1][j] = 0
          }
        }
      }
      
      maze.value = simpleMaze
    }

    const handleKeyPress = (event) => {
      if (gameWon.value) return

      const key = event.key.toLowerCase()
      let newX = playerPos.value.x
      let newY = playerPos.value.y

      switch (key) {
        case 'arrowup':
        case 'w':
          newY -= 1
          break
        case 'arrowdown':
        case 's':
          newY += 1
          break
        case 'arrowleft':
        case 'a':
          newX -= 1
          break
        case 'arrowright':
        case 'd':
          newX += 1
          break
        default:
          return
      }

      event.preventDefault()

      // Check if move is valid
      if (
        newX >= 0 && 
        newX < maze.value[0].length && 
        newY >= 0 && 
        newY < maze.value.length && 
        maze.value[newY][newX] === 0
      ) {
        playerPos.value = { x: newX, y: newY }
        moveCount.value++

        // Check if reached exit
        if (newX === exitPos.value.x && newY === exitPos.value.y) {
          gameWon.value = true
          stopTimer()
        }
      }
    }

    const backToResult = () => {
      stopTimer()
      emit('back')
    }

    const resetMaze = async () => {
      gameWon.value = false
      moveCount.value = 0
      elapsedTime.value = 0
      stopTimer()
      await loadMaze()
      startTimer()
      setTimeout(() => {
        mazeGrid.value?.focus()
      }, 100)
    }

    return {
      maze,
      playerPos,
      exitPos,
      gameWon,
      mazeGrid,
      moveCount,
      formattedTime,
      handleKeyPress,
      backToResult,
      resetMaze
    }
  }
}
</script>

<style scoped>
.maze-game {
  position: relative;
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #15201a 0%, #1a3025 100%);
  z-index: 10;
  overflow-y: auto;
  padding: 20px;
}

.maze-container {
  text-align: center;
  padding: 20px;
  max-width: 100%;
}

.maze-title {
  font-family: 'Cinzel', serif;
  font-size: 2.5rem;
  margin-bottom: 25px;
  text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.8);
}

.game-header {
  display: flex;
  justify-content: center;
  gap: 30px;
  flex-wrap: wrap;
  margin-bottom: 25px;
}

.maze-instructions {
  background: rgba(26, 26, 46, 0.95);
  border: 3px solid #FFD700;
  border-radius: 15px;
  padding: 15px 30px;
  display: inline-block;
  box-shadow: 0 0 25px rgba(255, 215, 0, 0.4);
}

.maze-instructions p {
  color: #FFD700;
  font-size: 1.1rem;
  font-weight: 600;
  margin: 5px 0;
}

.maze-instructions strong {
  color: #FFF;
  text-shadow: 0 0 10px rgba(255, 215, 0, 0.8);
}

.game-stats {
  display: flex;
  gap: 20px;
  align-items: center;
}

.stat {
  background: rgba(26, 26, 46, 0.95);
  border: 3px solid #5DBE71;
  border-radius: 12px;
  padding: 12px 24px;
  display: flex;
  flex-direction: column;
  gap: 5px;
  box-shadow: 0 0 20px rgba(93, 190, 113, 0.3);
}

.stat-label {
  color: #5DBE71;
  font-size: 0.9rem;
  font-weight: 600;
}

.stat-value {
  color: #FFF;
  font-size: 1.5rem;
  font-weight: 700;
  text-shadow: 0 0 10px rgba(93, 190, 113, 0.5);
}

.maze-grid {
  display: inline-block;
  border: 4px solid #FFD700;
  border-radius: 10px;
  background: rgba(0, 0, 0, 0.5);
  padding: 10px;
  box-shadow: 0 0 40px rgba(255, 215, 0, 0.5);
  margin-bottom: 20px;
  outline: none;
}

.maze-row {
  display: flex;
  line-height: 0;
}

.maze-cell {
  width: 30px;
  height: 30px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  transition: all 0.3s ease;
}

.maze-cell.wall {
  background: #1a3025;
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
}

.maze-cell.path {
  background: #2a3a35;
}

.maze-cell.player {
  background: radial-gradient(circle, rgba(255, 215, 0, 0.3), transparent);
  animation: playerGlow 1s ease-in-out infinite;
}

.maze-cell.exit {
  background: radial-gradient(circle, rgba(93, 190, 113, 0.5), transparent);
  animation: exitGlow 2s ease-in-out infinite;
}

@keyframes playerGlow {
  0%, 100% {
    box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
  }
  50% {
    box-shadow: 0 0 20px rgba(255, 215, 0, 1);
  }
}

@keyframes exitGlow {
  0%, 100% {
    box-shadow: 0 0 15px rgba(93, 190, 113, 0.7);
  }
  50% {
    box-shadow: 0 0 30px rgba(93, 190, 113, 1);
  }
}

.player-icon {
  font-size: 26px;
  animation: bounce 0.5s ease-in-out infinite;
}

.exit-icon {
  font-size: 24px;
  animation: rotate 2s linear infinite;
}

@keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.win-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.95);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 0.5s ease-out;
  padding: 20px;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.win-content {
  background: linear-gradient(135deg, rgba(26, 26, 46, 0.98), rgba(15, 15, 30, 0.98));
  border: 4px solid #FFD700;
  border-radius: 25px;
  padding: 50px 70px;
  text-align: center;
  max-width: 650px;
  box-shadow: 0 0 80px rgba(255, 215, 0, 0.9);
  animation: slideIn 0.6s ease-out;
}

@keyframes slideIn {
  from {
    transform: scale(0.8) translateY(-50px);
    opacity: 0;
  }
  to {
    transform: scale(1) translateY(0);
    opacity: 1;
  }
}

.win-title {
  font-family: 'Cinzel', serif;
  font-size: 3rem;
  color: #FFD700;
  margin-bottom: 20px;
  animation: bounce 1s ease-in-out infinite;
}

.win-message {
  font-size: 1.4rem;
  color: #E8D7C3;
  margin-bottom: 30px;
  line-height: 1.6;
}

.trophy {
  font-size: 6rem;
  margin: 30px 0;
  animation: trophy-float 2s ease-in-out infinite;
}

@keyframes trophy-float {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-20px) rotate(10deg);
  }
}

.win-subtitle {
  font-size: 1.5rem;
  color: #FFD700;
  margin-bottom: 15px;
}

.champion-text {
  font-size: 1.3rem;
  color: #E8D7C3;
  margin-bottom: 30px;
  font-style: italic;
}

.win-stats {116, 0, 1, 0.95), rgba(174, 0, 1, 0.95));
  border: 3px solid #FFD700;
  font-size: 1.1rem;
  padding: 15px 35px;
}

.reset-button {
  background: linear-gradient(135deg, rgba(26, 71, 42, 0.95), rgba(42, 91, 62, 0.95));
  border: 3px solid #5DBE71;
  color: #5DBE71;
  font-size: 1.1rem;
  padding: 15px 35px;
}

.reset-button:hover {
  box-shadow: 0 0 30px rgba(93, 190, 113, 0.7);
}

@media (max-width: 768px) {
  .maze-title {
    font-size: 1.8rem;
  }
  
  .game-header {
    flex-direction: column;
    gap: 15px;
  }
  
  .game-stats {
    justify-content: center
.win-stat {
  background: rgba(93, 190, 113, 0.2);
  border: 2px solid #5DBE71;
  border-radius: 12px;
  padding: 15px 30px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.win-stat span {
  color: #5DBE71;
  font-size: 1rem;
}

.win-stat strong {
  color: #FFF;
  font-size: 1.8rem;
  text-shadow: 0 0 10px rgba(93, 190, 113, 0.7);
}

.win-buttons {
  display: flex;
  gap: 15px;
  justify-content: center;
  flex-wrap: wrap;
}

.primary-btn {
  background: linear-gradient(135deg, rgba(116, 0, 1, 0.95), rgba(174, 0, 1, 0.95)) !important;
  border: 3px solid #FFD700 !important;
  font-size: 1.1rem !important;
  padding: 18px 35px !important;
}

.secondary-btn {
  background: linear-gradient(135deg, rgba(26, 71, 42, 0.95), rgba(42, 91, 62, 0.95)) !important;
  border: 3px solid #5DBE71 !important;
  color: #5DBE71 !important;
  font-size: 1.1rem !important;
  padding: 18px 35px !important;
}

.control-buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
  margin-top: 25px;
  flex-wrap: wrap;
}

.back-button {
  background: linear-gradient(135deg, rgba(42, 58, 53, 0.9), rgba(58, 74, 69, 0.9));
  font-size: 1.1rem;
  padding: 15px 35px;
}

@media (max-width: 768px) {
  .maze-title {
    font-size: 1.8rem;
  }
  
  .maze-cell {
    width: 20px;
    height: 20px;
  }
  
  .player-icon,
  .exit-icon {
    font-size: 16px;
  }
  
  .win-content {
    padding: 30px 40px;
  }
  
  .win-title {
    font-size: 2rem;
  }
  
  .trophy {
    font-size: 4rem;
  }
}
</style>
