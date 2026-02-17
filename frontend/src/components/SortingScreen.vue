<template>
  <div class="sorting-screen">
    <div class="content">
      <!-- Thinking Animation -->
      <div class="hat-thinking">
        <div class="hat-large">
          <svg viewBox="0 0 200 200" class="hat-svg">
            <path d="M100,50 Q80,40 70,60 Q60,80 65,100 L75,140 Q80,160 100,160 Q120,160 125,140 L135,100 Q140,80 130,60 Q120,40 100,50 Z" 
                  fill="#3d2817" 
                  stroke="#2a1810" 
                  stroke-width="2"/>
            <ellipse cx="100" cy="160" rx="35" ry="8" fill="#2a1810"/>
            <path d="M85,80 Q90,70 100,65 Q110,70 115,80" 
                  fill="none" 
                  stroke="#1a0f08" 
                  stroke-width="2"/>
          </svg>
        </div>
      </div>

      <!-- Thinking Message -->
      <div class="message-container">
        <h2 class="thinking-text">🤔 Hmm...{{ studentName }}...</h2>
        <p class="analyzing-text">{{ thinkingMessage }}<span class="dots">{{ dots }}</span></p>
        <p class="subtext">✨ Analyzing your magical traits... ✨</p>
      </div>

      <!-- Magical Energy Rings -->
      <div class="energy-rings">
        <div class="ring ring-1"></div>
        <div class="ring ring-2"></div>
        <div class="ring ring-3"></div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'

export default {
  name: 'SortingScreen',
  props: {
    studentName: {
      type: String,
      required: true
    }
  },
  emits: ['sorted'],
  setup(props, { emit }) {
    const thinkingMessage = ref('Difficult. Very difficult')
    const dots = ref('.')

    onMounted(() => {
      // Animate dots
      let dotCount = 1
      const dotInterval = setInterval(() => {
        dotCount = (dotCount % 3) + 1
        dots.value = '.'.repeat(dotCount)
      }, 500)

      // Perform sorting after 3 seconds
      setTimeout(async () => {
        clearInterval(dotInterval)
        await performSorting()
      }, 3000)
    })

    const performSorting = async () => {
      try {
        const response = await axios.post('/api/sort', {
          name: props.studentName
        })
        
        if (response.data.success) {
          // Add slight delay for dramatic effect
          setTimeout(() => {
            emit('sorted', {
              house: response.data.house,
              houseInfo: response.data.houseInfo
            })
          }, 500)
        }
      } catch (error) {
        console.error('Sorting failed:', error)
        // Fallback to random sorting
        const houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
        const randomHouse = houses[Math.floor(Math.random() * houses.length)]
        emit('sorted', { house: randomHouse })
      }
    }

    return {
      thinkingMessage,
      dots
    }
  }
}
</script>

<style scoped>
.sorting-screen {
  position: relative;
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
}

.content {
  text-align: center;
  position: relative;
}

.hat-thinking {
  position: relative;
  margin-bottom: 50px;
}

.hat-large {
  width: 200px;
  height: 200px;
  margin: 0 auto;
  animation: hatThinking 2s ease-in-out infinite;
}

.hat-svg {
  width: 100%;
  height: 100%;
  filter: drop-shadow(0 0 30px rgba(255, 215, 0, 0.7));
}

@keyframes hatThinking {
  0%, 100% {
    transform: rotate(-10deg) scale(1);
  }
  50% {
    transform: rotate(10deg) scale(1.1);
  }
}

.message-container {
  background: linear-gradient(135deg, rgba(26, 26, 46, 0.95), rgba(15, 15, 30, 0.95));
  border: 3px solid #FFD700;
  border-radius: 20px;
  padding: 40px 60px;
  box-shadow: 0 0 40px rgba(255, 215, 0, 0.5);
  backdrop-filter: blur(10px);
  position: relative;
  z-index: 2;
}

.thinking-text {
  font-family: 'Cinzel', serif;
  font-size: 2.5rem;
  color: #FFD700;
  margin-bottom: 20px;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
}

.analyzing-text {
  font-size: 1.8rem;
  color: #FFD700;
  margin-bottom: 15px;
  font-style: italic;
}

.dots {
  display: inline-block;
  width: 30px;
  text-align: left;
}

.subtext {
  font-size: 1.3rem;
  color: #E8D7C3;
  margin-top: 20px;
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.6;
  }
}

.energy-rings {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 400px;
  height: 400px;
  pointer-events: none;
  z-index: 1;
}

.ring {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border: 2px solid rgba(255, 215, 0, 0.5);
  border-radius: 50%;
  animation: expandRing 3s ease-out infinite;
}

.ring-1 {
  width: 100px;
  height: 100px;
  animation-delay: 0s;
}

.ring-2 {
  width: 150px;
  height: 150px;
  animation-delay: 1s;
}

.ring-3 {
  width: 200px;
  height: 200px;
  animation-delay: 2s;
}

@keyframes expandRing {
  0% {
    width: 50px;
    height: 50px;
    opacity: 0;
  }
  50% {
    opacity: 0.8;
  }
  100% {
    width: 400px;
    height: 400px;
    opacity: 0;
  }
}

@media (max-width: 768px) {
  .hat-large {
    width: 150px;
    height: 150px;
  }
  
  .message-container {
    padding: 30px 40px;
  }
  
  .thinking-text {
    font-size: 1.8rem;
  }
  
  .analyzing-text {
    font-size: 1.3rem;
  }
}
</style>
