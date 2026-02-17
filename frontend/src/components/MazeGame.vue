<template>
  <div class="maze-game">
    <div class="maze-container">
      <!-- Title -->
      <h1 class="maze-title text-shimmer">🌟 THE TRIWIZARD MAZE 🌟</h1>

      <!-- Game Status -->
      <div v-if="!gameWon" class="maze-instructions">
        <p>Use Arrow Keys ⬆️⬇️⬅️➡️ to navigate | Find the Triwizard Cup 🏆</p>
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
          
          <button class="magical-button" @click="backToResult">
            🔄 Return to Sorting Hat
          </button>
        </div>
      </div>

      <!-- Back Button -->
      <button v-if="!gameWon" class="back-button magical-button" @click="backToResult">
        ⬅️ Back to Sorting Hat
      </button>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue'
import axios from 'axios'

export default {
  name: 'MazeGame',
  emits: ['back'],
  setup(props, { emit }) {
    const maze = ref([])
    const playerPos = ref({ x: 1, y: 1 })
    const exitPos = ref({ x: 13, y: 13 })
    const gameWon = ref(false)
    const mazeGrid = ref(null)

    onMounted(async () => {
      await loadMaze()
      // Focus the maze grid for keyboard events
      setTimeout(() => {
        mazeGrid.value?.focus()
      }, 100)
    })

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

      const key = event.key
      let newX = playerPos.value.x
      let newY = playerPos.value.y

      switch (key) {
        case 'ArrowUp':
          newY -= 1
          break
        case 'ArrowDown':
          newY += 1
          break
        case 'ArrowLeft':
          newX -= 1
          break
        case 'ArrowRight':
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

        // Check if reached exit
        if (newX === exitPos.value.x && newY === exitPos.value.y) {
          gameWon.value = true
        }
      }
    }

    const backToResult = () => {
      emit('back')
    }

    return {
      maze,
      playerPos,
      exitPos,
      gameWon,
      mazeGrid,
      handleKeyPress,
      backToResult
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
}

.maze-container {
  text-align: center;
  padding: 20px;
}

.maze-title {
  font-family: 'Cinzel', serif;
  font-size: 2.5rem;
  margin-bottom: 20px;
  text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.8);
}

.maze-instructions {
  background: rgba(26, 26, 46, 0.9);
  border: 2px solid #FFD700;
  border-radius: 10px;
  padding: 15px 30px;
  margin-bottom: 25px;
  display: inline-block;
}

.maze-instructions p {
  color: #FFD700;
  font-size: 1.1rem;
  font-weight: 600;
  margin: 0;
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
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  animation: fadeIn 0.5s ease-out;
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
  background: linear-gradient(135deg, rgba(26, 26, 46, 0.95), rgba(15, 15, 30, 0.95));
  border: 4px solid #FFD700;
  border-radius: 20px;
  padding: 50px 70px;
  text-align: center;
  max-width: 600px;
  box-shadow: 0 0 60px rgba(255, 215, 0, 0.8);
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
  margin-bottom: 40px;
  font-style: italic;
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
