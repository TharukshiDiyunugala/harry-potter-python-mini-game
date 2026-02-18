<template>
  <div id="app">
    <!-- Animated Background -->
    <div class="background">
      <div class="stars-container">
        <div v-for="n in 100" :key="n" class="star" :style="getStarStyle(n)"></div>
      </div>
      
      <!-- Floating particles -->
      <div v-for="n in 30" :key="'particle-' + n" class="particle" :style="getParticleStyle(n)"></div>
    </div>

    <!-- Music Control -->
    <button class="music-toggle" @click="toggleMusic" :class="{ playing: musicPlaying }">
      {{ musicPlaying ? '🔊' : '🔇' }}
    </button>

    <!-- Main Content -->
    <transition name="fade" mode="out-in">
      <WelcomeScreen 
        v-if="currentScreen === 'welcome'" 
        @start="showNameEntry"
      />
      <NameEntry 
        v-else-if="currentScreen === 'nameEntry'" 
        @submit="startSorting"
      />
      <SortingScreen 
        v-else-if="currentScreen === 'sorting'" 
        :studentName="studentName"
        @sorted="showResult"
      />
      <ResultScreen 
        v-else-if="currentScreen === 'result'" 
        :studentName="studentName"
        :house="sortedHouse"
        :houseInfo="houseInfo"
        @restart="restart"
        @startMaze="startMaze"
      />
      <MazeGame 
        v-else-if="currentScreen === 'maze'" 
        @back="showResult"
      />
    </transition>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import WelcomeScreen from './components/WelcomeScreen.vue'
import NameEntry from './components/NameEntry.vue'
import SortingScreen from './components/SortingScreen.vue'
import ResultScreen from './components/ResultScreen.vue'
import MazeGame from './components/MazeGame.vue'

export default {
  name: 'App',
  components: {
    WelcomeScreen,
    NameEntry,
    SortingScreen,
    ResultScreen,
    MazeGame
  },
  setup() {
    const currentScreen = ref('welcome')
    const studentName = ref('')
    const sortedHouse = ref(null)
    const houseInfo = ref(null)
    const musicPlaying = ref(false)
    const audio = ref(null)

    onMounted(() => {
      // Initialize audio element
      audio.value = new Audio('/assets/theme.mp3')
      audio.value.loop = true
      audio.value.volume = 0.3 // 30% volume
      
      // Add event listeners for debugging
      audio.value.addEventListener('loadeddata', () => {
        console.log('Audio loaded successfully')
      })
      audio.value.addEventListener('error', (e) => {
        console.error('Audio loading error:', e)
      })
    })

    const showNameEntry = () => {
      currentScreen.value = 'nameEntry'
    }

    const startSorting = (name) => {
      studentName.value = name
      currentScreen.value = 'sorting'
    }

    const showResult = (data) => {
      if (data) {
        sortedHouse.value = data.house
        houseInfo.value = data.houseInfo
      }
      currentScreen.value = 'result'
    }

    const restart = () => {
      studentName.value = ''
      sortedHouse.value = null
      houseInfo.value = null
      currentScreen.value = 'welcome'
    }

    const startMaze = () => {
      currentScreen.value = 'maze'
    }

    const toggleMusic = () => {
      musicPlaying.value = !musicPlaying.value
      
      if (musicPlaying.value) {
        // Play music
        audio.value?.play().catch(error => {
          console.log('Audio playback failed:', error)
          musicPlaying.value = false
        })
      } else {
        // Pause music
        audio.value?.pause()
      }
    }

    const getStarStyle = (n) => {
      return {
        left: `${Math.random() * 100}%`,
        top: `${Math.random() * 100}%`,
        animationDelay: `${Math.random() * 2}s`,
        animationDuration: `${2 + Math.random() * 2}s`
      }
    }

    const getParticleStyle = (n) => {
      return {
        left: `${Math.random() * 100}%`,
        top: `${Math.random() * 100}%`,
        animationDelay: `${Math.random() * 4}s`,
        animationDuration: `${3 + Math.random() * 3}s`
      }
    }

    return {
      currentScreen,
      studentName,
      sortedHouse,
      houseInfo,
      musicPlaying,
      showNameEntry,
      startSorting,
      showResult,
      restart,
      startMaze,
      toggleMusic,
      getStarStyle,
      getParticleStyle
    }
  }
}
</script>

<style scoped>
#app {
  width: 100vw;
  height: 100vh;
  background-image: url('/assets/hogwarts_bg.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  z-index: 0;
}

.background::before {
  z-index: 2;
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, rgba(10, 10, 15, 0.7) 0%, rgba(26, 21, 32, 0.8) 50%, rgba(15, 10, 21, 0.7) 100%);
  z-index: 1hidden;
}

.background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, #0a0a0f 0%, #1a1520 50%, #0f0a15 100%);
  z-index: 0;
}

.stars-container {
  position: absolute;
  width: 100%;
  height: 100%;
}

.music-toggle {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 1000;
  font-size: 2rem;
  background: rgba(26, 26, 46, 0.8);
  border: 2px solid #FFD700;
  border-radius: 50%;
  width: 60px;
  height: 60px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.music-toggle:hover {
  background: rgba(26, 26, 46, 1);
  box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
  transform: scale(1.1);
}

.music-toggle.playing {
  box-shadow: 0 0 20px rgba(255, 215, 0, 0.7);
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}
</style>
