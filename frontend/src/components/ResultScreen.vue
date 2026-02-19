<template>
  <div class="result-screen" :style="{ background: houseBg }">
    <!-- House-colored particles -->
    <div class="house-particles">
      <div v-for="n in 20" :key="'hp-' + n" class="house-particle" :style="getHouseParticleStyle(n)"></div>
    </div>

    <!-- Explosion Effect -->
    <div v-if="showExplosion" class="explosion">
      <div v-for="n in 50" :key="'exp-' + n" class="explosion-particle" :style="getExplosionStyle(n)"></div>
    </div>

    <div class="content">
      <!-- House Emblem -->
      <div class="house-emblem">
        <div class="emblem-circle" :style="{ borderColor: houseColor }">
          <div class="emoji-large">{{ houseInfo.emoji }}</div>
        </div>
      </div>

      <!-- Result Message -->
      <div class="result-card" :style="{ borderColor: houseColor, background: cardBg }">
        <h1 class="congratulations">🎉 CONGRATULATIONS! 🎉</h1>
        <h2 class="student-name">{{ studentName.toUpperCase() }}</h2>
        <p class="sorted-into">You have been sorted into</p>
        
        <div class="house-name-container">
          <h1 class="house-name text-shimmer" :style="{ color: houseColor }">
            {{ houseInfo.emoji }} {{ house.toUpperCase() }} {{ houseInfo.emoji }}
          </h1>
        </div>
        
        <p class="traits" :style="{ color: houseColor }">{{ houseInfo.traits }}</p>
        <p class="founder">Founded by: {{ houseInfo.founder }}</p>
        <p class="description">"{{ houseInfo.description }}"</p>
        <p class="quote-attribution">- The Sorting Hat</p>
      </div>

      <!-- Action Buttons -->
      <div class="action-buttons">
        <button class="magical-button maze-button" @click="startMaze">
          <span class="btn-icon">🌟</span>
          <span>ENTER THE TRIWIZARD MAZE</span>
          <span class="btn-icon">🌟</span>
        </button>
        <button class="magical-button restart-button" @click="restart">
          <span class="btn-icon">🔄</span>
          <span>Sort Another Student</span>
        </button>
        <button class="magical-button share-button" @click="shareResult">
          <span class="btn-icon">📢</span>
          <span>Share Your House</span>
        </button>
      </div>
      
      <!-- House Description -->
      <div class="house-details" :style="{ borderColor: houseColor }">
        <h3 class="details-title">About Your House</h3>
        <div class="house-qualities">
          <div class="quality-item" v-for="(quality, index) in houseQualities" :key="index">
            <span class="quality-icon">✨</span>
            <span class="quality-text">{{ quality }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'

export default {
  name: 'ResultScreen',
  props: {
    studentName: String,
    house: String,
    houseInfo: Object
  },
  emits: ['restart', 'startMaze'],
  setup(props, { emit }) {
    const showExplosion = ref(false)

    const houseColor = computed(() => props.houseInfo?.color || '#FFD700')
    const houseGlow = computed(() => props.houseInfo?.glowColor || '#FFD700')

    const houseQualities = computed(() => {
      const qualities = {
        'Gryffindor': ['Courage in the face of danger', 'Chivalry and honor', 'Determination and nerve'],
        'Hufflepuff': ['Hard work and dedication', 'Fair play and loyalty', 'Patience and kindness'],
        'Ravenclaw': ['Intelligence and wisdom', 'Creativity and wit', 'Love of learning'],
        'Slytherin': ['Ambition and cunning', 'Resourcefulness', 'Leadership and determination']
      }
      return qualities[props.house] || []
    })

    const houseBg = computed(() => {
      const colors = {
        'Gryffindor': 'linear-gradient(135deg, #1a0505 0%, #4a0808 100%)',
        'Hufflepuff': 'linear-gradient(135deg, #1a1508 0%, #4a3820 100%)',
        'Ravenclaw': 'linear-gradient(135deg, #050a1a 0%, #0f1f3a 100%)',
        'Slytherin': 'linear-gradient(135deg, #0a150f 0%, #1a3025 100%)'
      }
      return colors[props.house] || 'linear-gradient(135deg, #0a0a0f 0%, #1a1520 100%)'
    })

    const cardBg = computed(() => {
      return `linear-gradient(135deg, ${houseColor.value}22, ${houseColor.value}11)`
    })

    onMounted(() => {
      // Trigger explosion effect
      showExplosion.value = true
      setTimeout(() => {
        showExplosion.value = false
      }, 1000)
    })

    const restart = () => {
      emit('restart')
    }

    const startMaze = () => {
      emit('startMaze')
    }

    const shareResult = () => {
      const text = `🎭 I've been sorted into ${props.house}! 🎭\n${props.houseInfo?.traits}\n\n#HarryPotter #SortingHat`
      
      if (navigator.share) {
        navigator.share({
          title: 'Hogwarts Sorting',
          text: text
        }).catch(err => console.log('Share cancelled', err))
      } else {
        // Fallback: copy to clipboard
        navigator.clipboard.writeText(text)
          .then(() => alert('✅ Result copied to clipboard!'))
          .catch(() => alert('📎 Share: ' + text))
      }
    }

    const getHouseParticleStyle = (n) => {
      return {
        left: `${Math.random() * 100}%`,
        top: `${Math.random() * 100}%`,
        background: houseGlow.value,
        animationDelay: `${Math.random() * 3}s`,
        animationDuration: `${4 + Math.random() * 2}s`
      }
    }

    const getExplosionStyle = (n) => {
      const angle = (n / 50) * Math.PI * 2
      const distance = 100 + Math.random() * 200
      return {
        left: '50%',
        top: '50%',
        background: houseGlow.value,
        '--x': `${Math.cos(angle) * distance}px`,
        '--y': `${Math.sin(angle) * distance}px`
      }
    }

    return {
      showExplosion,
      houseColor,
      houseGlow,
      houseBg,
      cardBg,
      houseQualities,
      restart,
      startMaze,
      shareResult,
      getHouseParticleStyle,
      getExplosionStyle
    }
  }
}
</script>

<style scoped>
.result-screen {
  position: relative;
  width: 100%;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
  overflow: hidden;
}

.house-particles {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 1;
}

.house-particle {
  position: absolute;
  width: 6px;
  height: 6px;
  border-radius: 50%;
  opacity: 0.7;
  animation: floatHouse 5s ease-in-out infinite;
}

@keyframes floatHouse {
  0%, 100% {
    transform: translateY(0) translateX(0) scale(1);
    opacity: 0.7;
  }
  50% {
    transform: translateY(-100px) translateX(30px) scale(1.5);
    opacity: 0.3;
  }
}

.explosion {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 100;
}

.explosion-particle {
  position: absolute;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  animation: explode 1s ease-out forwards;
}

@keyframes explode {
  0% {
    transform: translate(0, 0) scale(1);
    opacity: 1;
  }
  100% {
    transform: translate(var(--x), var(--y)) scale(0);
    opacity: 0;
  }
}

.content {
  text-align: center;
  padding: 20px;
  max-width: 900px;
  z-index: 10;
  animation: slideUp 0.8s ease-out;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.house-emblem {
  margin-bottom: 30px;
}

.emblem-circle {
  width: 180px;
  height: 180px;
  margin: 0 auto;
  border: 4px solid;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.3);
  box-shadow: 0 0 40px currentColor;
  animation: rotateBorder 3s linear infinite, pulse 2s ease-in-out infinite;
}

@keyframes rotateBorder {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.emoji-large {
  font-size: 7rem;
  animation: bounce 1.5s ease-in-out infinite;
}

.result-card {
  border: 3px solid;
  border-radius: 20px;
  padding: 40px 50px;
  margin-bottom: 40px;
  backdrop-filter: blur(10px);
  box-shadow: 0 0 50px currentColor;
}

.congratulations {
  font-family: 'Cinzel', serif;
  font-size: 2.5rem;
  color: #FFD700;
  margin-bottom: 20px;
  animation: bounce 1s ease-in-out infinite;
}

.student-name {
  font-family: 'Cinzel', serif;
  font-size: 2.2rem;
  color: #FFFACD;
  margin-bottom: 20px;
  letter-spacing: 3px;
}

.sorted-into {
  font-size: 1.5rem;
  color: #E8D7C3;
  margin-bottom: 15px;
}

.house-name-container {
  margin: 20px 0;
  padding: 15px;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 10px;
}

.house-name {
  font-family: 'Cinzel', serif;
  font-size: 3.5rem;
  font-weight: 700;
  text-shadow: 0 0 20px currentColor;
  letter-spacing: 4px;
  margin: 0;
}

.traits {
  font-size: 1.5rem;
  font-weight: 600;
  margin: 25px 0;
  text-shadow: 0 0 10px currentColor;
}

.founder {
  font-size: 1.2rem;
  color: #FFD700;
  margin-bottom: 20px;
  font-style: italic;
}

.description {
  font-size: 1.1rem;
  color: #E8D7C3;
  font-style: italic;
  line-height: 1.6;
  margin-bottom: 10px;
}

.quote-attribution {
  font-size: 0.9rem;
  color: rgba(255, 215, 0, 0.7);
  text-align: right;
}

.action-buttons {
  display: flex;
  gap: 20px;
  justify-content: center;
  flex-wrap: wrap;
  margin-bottom: 30px;
}

.btn-icon {
  font-size: 1.3rem;
}

.maze-button {
  background: linear-gradient(135deg, rgba(14, 26, 64, 0.98), rgba(34, 47, 91, 0.98)) !important;
  border: 4px solid #5DADE2 !important;
  color: #5DADE2 !important;
  font-size: 1.3rem !important;
  padding: 20px 40px !important;
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 0 30px rgba(93, 173, 226, 0.6);
}

.maze-button:hover {
  box-shadow: 0 0 50px rgba(93, 173, 226, 0.9) !important;
  transform: translateY(-5px) !important;
}

.restart-button {
  background: linear-gradient(135deg, rgba(116, 0, 1, 0.98), rgba(174, 0, 1, 0.98)) !important;
  border: 4px solid #FFD700 !important;
  color: #FFD700 !important;
  font-size: 1.1rem !important;
  padding: 18px 35px !important;
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 0 30px rgba(255, 215, 0, 0.5);
}

.restart-button:hover {
  box-shadow: 0 0 50px rgba(255, 215, 0, 0.8) !important;
  transform: translateY(-5px) !important;
}

.share-button {
  background: linear-gradient(135deg, rgba(26, 71, 42, 0.98), rgba(42, 91, 62, 0.98)) !important;
  border: 4px solid #5DBE71 !important;
  color: #5DBE71 !important;
  font-size: 1.1rem !important;
  padding: 18px 35px !important;
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 0 30px rgba(93, 190, 113, 0.5);
}

.share-button:hover {
  box-shadow: 0 0 50px rgba(93, 190, 113, 0.8) !important;
  transform: translateY(-5px) !important;
}

.house-details {
  border: 3px solid;
  border-radius: 15px;
  padding: 30px;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(10px);
  margin-top: 10px;
}

.details-title {
  font-family: 'Cinzel', serif;
  font-size: 1.8rem;
  color: #FFD700;
  margin-bottom: 20px;
  text-shadow: 0 0 15px rgba(255, 215, 0, 0.7);
}

.house-qualities {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.quality-item {
  display: flex;
  align-items: center;
  gap: 15px;
  font-size: 1.2rem;
  color: #E8D7C3;
  padding: 12px 20px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
  transition: all 0.3s ease;
}

.quality-item:hover {
  background: rgba(255, 255, 255, 0.1);
  transform: translateX(10px);
}

.quality-icon {
  font-size: 1.5rem;
  color: #FFD700;
}

.quality-text {
  flex: 1;
  font-weight: 500;
}

@media (max-width: 768px) {
  .house-name {
    font-size: 2.5rem;
  }
  
  .result-card {
    padding: 30px 25px;
  }
  
  .action-buttons {
    flex-direction: column;
    width: 100%;
  }
  
  .magical-button {
    width: 100%;
  }
  
  .maze-button {
    font-size: 1.1rem !important;
    padding: 18px 30px !important;
  }
  
  .house-details {
    padding: 20px;
  }
  
  .quality-item {
    font-size: 1rem;
  }
}
</style>
