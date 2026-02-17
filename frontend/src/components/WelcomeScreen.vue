<template>
  <div class="welcome-screen">
    <div class="content">
      <!-- Animated Sorting Hat -->
      <div class="hat-container">
        <div class="hat" :class="{ spinning: isSpinning }">
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

      <!-- Title -->
      <h1 class="title text-shimmer">The Official Sorting Ceremony</h1>
      <p class="subtitle">✨ The Magical Sorting Ceremony ✨</p>

      <!-- Welcome Message -->
      <div class="welcome-card">
        <h2>⚡ ENTER THE MAGICAL REALM OF HOGWARTS ⚡</h2>
        <p>
          Prepare to embark on an immersive journey through the ancient halls of wizardry.
          The legendary Sorting Hat, imbued with the wisdom of the Four Founders,
          will analyze your unique qualities and place you among your destined peers.
        </p>
        <p class="your-legacy">Your magical legacy awaits...</p>
        
        <div class="houses-preview">
          <span class="house-emoji gryffindor">🦁</span>
          <span class="house-emoji hufflepuff">🦡</span>
          <span class="house-emoji ravenclaw">🦅</span>
          <span class="house-emoji slytherin">🐍</span>
        </div>
      </div>

      <!-- Start Button -->
      <button class="magical-button start-button" @click="startCeremony">
        ⚡ BEGIN CEREMONY ⚡
      </button>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  name: 'WelcomeScreen',
  emits: ['start'],
  setup(props, { emit }) {
    const isSpinning = ref(false)

    onMounted(() => {
      // Start hat animation
      setTimeout(() => {
        isSpinning.value = true
      }, 500)
    })

    const startCeremony = () => {
      emit('start')
    }

    return {
      isSpinning,
      startCeremony
    }
  }
}
</script>

<style scoped>
.welcome-screen {
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
  padding: 20px;
  max-width: 900px;
}

.hat-container {
  margin-bottom: 30px;
  display: flex;
  justify-content: center;
}

.hat {
  width: 150px;
  height: 150px;
  animation: float 3s ease-in-out infinite;
}

.hat.spinning {
  animation: float 3s ease-in-out infinite, spin 4s linear infinite;
}

.hat-svg {
  width: 100%;
  height: 100%;
  filter: drop-shadow(0 0 20px rgba(255, 215, 0, 0.5));
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.title {
  font-family: 'Cinzel', serif;
  font-size: 3.5rem;
  font-weight: 700;
  margin-bottom: 15px;
  text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.8);
  letter-spacing: 3px;
}

.subtitle {
  font-size: 1.5rem;
  color: #E8D7C3;
  margin-bottom: 40px;
  font-style: italic;
}

.welcome-card {
  background: linear-gradient(135deg, rgba(26, 26, 46, 0.9), rgba(15, 15, 30, 0.9));
  border: 2px solid #FFD700;
  border-radius: 15px;
  padding: 40px;
  margin-bottom: 40px;
  box-shadow: 0 0 30px rgba(255, 215, 0, 0.3);
  backdrop-filter: blur(10px);
}

.welcome-card h2 {
  color: #FFD700;
  font-size: 1.8rem;
  margin-bottom: 25px;
  font-family: 'Cinzel', serif;
}

.welcome-card p {
  color: #E8D7C3;
  font-size: 1.1rem;
  line-height: 1.8;
  margin-bottom: 15px;
}

.your-legacy {
  font-style: italic;
  color: #FFD700 !important;
  margin-top: 20px;
  font-size: 1.2rem !important;
}

.houses-preview {
  display: flex;
  justify-content: center;
  gap: 30px;
  margin-top: 30px;
  font-size: 3rem;
}

.house-emoji {
  display: inline-block;
  animation: bounce 2s infinite;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.house-emoji:hover {
  transform: scale(1.3);
}

.house-emoji.gryffindor {
  animation-delay: 0s;
  filter: drop-shadow(0 0 10px #740001);
}

.house-emoji.hufflepuff {
  animation-delay: 0.2s;
  filter: drop-shadow(0 0 10px #FFDB00);
}

.house-emoji.ravenclaw {
  animation-delay: 0.4s;
  filter: drop-shadow(0 0 10px #0E1A40);
}

.house-emoji.slytherin {
  animation-delay: 0.6s;
  filter: drop-shadow(0 0 10px #1A472A);
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px);
  }
  60% {
    transform: translateY(-5px);
  }
}

.start-button {
  font-size: 1.5rem;
  padding: 22px 60px;
  animation: glow-pulse 2s ease-in-out infinite;
}

@keyframes glow-pulse {
  0%, 100% {
    box-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
  }
  50% {
    box-shadow: 0 0 40px rgba(255, 215, 0, 0.7);
  }
}

@media (max-width: 768px) {
  .title {
    font-size: 2.5rem;
  }
  
  .welcome-card {
    padding: 25px;
  }
  
  .welcome-card h2 {
    font-size: 1.4rem;
  }
  
  .houses-preview {
    font-size: 2rem;
    gap: 15px;
  }
}
</style>
