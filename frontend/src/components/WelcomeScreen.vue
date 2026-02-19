<template>
  <div class="welcome-screen">
    <div class="content">
      <!-- Hogwarts Logo/Crest -->
      <div class="hogwarts-crest">
        <div class="crest-circle">
          🧙‍♂️
        </div>
      </div>

      <!-- Title -->
      <h1 class="title text-shimmer">The Official Hogwarts</h1>
      <h2 class="subtitle-text">Sorting Ceremony</h2>
      
      <p class="description">
        ✨ Discover which house you truly belong to ✨
      </p>

      <!-- Start Button -->
      <button class="magical-button start-button" @click="startCeremony">
        <span class="button-icon">⚡</span>
        <span class="button-text">BEGIN YOUR JOURNEY</span>
        <span class="button-icon">⚡</span>
      </button>
      
      <p class="hint">
        🎭 Are you brave, loyal, wise, or ambitious?
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WelcomeScreen',
  emits: ['start'],
  setup(props, { emit }) {
    const startCeremony = () => {
      emit('start')
    }

    return {
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
  background-image: url('/assets/hogwarts_bg.jpg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

/* Dark overlay for better text readability */
.welcome-screen::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: -1;
}

.content {
  text-align: center;
  padding: 40px;
  max-width: 1000px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 30px;
  animation: fadeInUp 1s ease-out;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.hogwarts-crest {
  margin-bottom: 20px;
  animation: float 3s ease-in-out infinite;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-15px);
  }
}

.crest-circle {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(26, 26, 46, 0.95), rgba(15, 15, 30, 0.95));
  border: 4px solid #FFD700;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 5rem;
  box-shadow: 0 0 50px rgba(255, 215, 0, 0.8);
  animation: rotateBorder 4s linear infinite;
}

@keyframes rotateBorder {
  from {
    box-shadow: 0 0 50px rgba(255, 215, 0, 0.8), 0 0 80px rgba(255, 215, 0, 0.4);
  }
  50% {
    box-shadow: 0 0 80px rgba(255, 215, 0, 1), 0 0 120px rgba(255, 215, 0, 0.6);
  }
  to {
    box-shadow: 0 0 50px rgba(255, 215, 0, 0.8), 0 0 80px rgba(255, 215, 0, 0.4);
  }
}

.title {
  font-family: 'Cinzel', serif;
  font-size: 4.5rem;
  font-weight: 700;
  text-shadow: 4px 4px 8px rgba(0, 0, 0, 0.9), 0 0 40px rgba(255, 215, 0, 0.7);
  letter-spacing: 4px;
  color: #FFD700;
  margin: 0;
  line-height: 1.2;
}

.subtitle-text {
  font-family: 'Cinzel', serif;
  font-size: 3.5rem;
  font-weight: 600;
  color: #FFF;
  text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.9), 0 0 30px rgba(255, 215, 0, 0.5);
  letter-spacing: 3px;
  margin: 0;
}

.description {
  font-size: 1.5rem;
  color: #E8D7C3;
  font-style: italic;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
  margin: 10px 0 20px 0;
}

.start-button {
  font-size: 1.8rem;
  padding: 25px 60px;
  animation: glow-pulse 2s ease-in-out infinite;
  background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
  border: 4px solid #FFD700;
  border-radius: 15px;
  color: #1a0f08;
  font-weight: 900;
  cursor: pointer;
  transition: all 0.3s ease;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
  box-shadow: 0 0 40px rgba(255, 215, 0, 0.8), 0 10px 30px rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  gap: 15px;
  letter-spacing: 3px;
}

.button-icon {
  font-size: 2rem;
  animation: sparkle 1.5s ease-in-out infinite;
}

.button-text {
  font-family: 'Cinzel', serif;
}

@keyframes sparkle {
  0%, 100% {
    transform: scale(1) rotate(0deg);
    opacity: 1;
  }
  50% {
    transform: scale(1.3) rotate(180deg);
    opacity: 0.8;
  }
}

.start-button:hover {
  transform: scale(1.05) translateY(-5px);
  background: linear-gradient(135deg, #FFA500 0%, #FFD700 100%);
  box-shadow: 0 0 60px rgba(255, 215, 0, 1), 0 15px 40px rgba(0, 0, 0, 0.6);
}

.start-button:active {
  transform: scale(0.98) translateY(0);
}

@keyframes glow-pulse {
  0%, 100% {
    box-shadow: 0 0 40px rgba(255, 215, 0, 0.8), 0 10px 30px rgba(0, 0, 0, 0.5);
  }
  50% {
    box-shadow: 0 0 70px rgba(255, 215, 0, 1), 0 10px 30px rgba(0, 0, 0, 0.5);
  }
}

.hint {
  font-size: 1.2rem;
  color: rgba(255, 215, 0, 0.8);
  font-style: italic;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
  margin-top: 10px;
}

@media (max-width: 768px) {
  .title {
    font-size: 2.5rem;
  }
  
  .start-button {
    font-size: 1.5rem;
    padding: 20px 60px;
  }
}
</style>
