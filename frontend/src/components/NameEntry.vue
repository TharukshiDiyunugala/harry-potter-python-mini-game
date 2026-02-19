<template>
  <div class="name-entry-screen">
    <div class="content">
      <h1 class="title text-shimmer">Enter Your Name</h1>
      <p class="subtitle">Let the Sorting Hat know who you are...</p>

      <!-- Owl Character -->
      <div v-if="showOwl" class="owl-container">
        <div class="owl">🦉</div>
        <div class="speech-bubble">
          <p>{{ owlMessage }}</p>
        </div>
      </div>

      <!-- Name Input -->
      <div class="input-container">
        <input 
          v-model="studentName"
          ref="nameInput"
          type="text" 
          class="magical-input"
          placeholder="Enter your name..."
          @focus="handleFocus"
          @blur="handleBlur"
          @keyup.enter="submitName"
          maxlength="30"
        />
        <div class="sparkles">
          <span v-for="n in 8" :key="n" class="sparkle">✨</span>
        </div>
      </div>

      <!-- Submit Button -->
      <button 
        class="magical-button submit-button" 
        @click="submitName"
        :disabled="!studentName.trim()"
      >
        ✨ BEGIN SORTING ✨
      </button>

      <p class="hint">Press Enter or click the button to continue</p>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  name: 'NameEntry',
  emits: ['submit'],
  setup(props, { emit }) {
    const studentName = ref('')
    const showOwl = ref(false)
    const owlMessage = ref("A fine name! Let's sort you!")
    const nameInput = ref(null)

    onMounted(() => {
      // Focus input on mount
      setTimeout(() => {
        nameInput.value?.focus()
      }, 300)
    })

    const handleFocus = () => {
      showOwl.value = true
      owlMessage.value = "A fine name! Let's sort you!"
    }

    const handleBlur = () => {
      setTimeout(() => {
        showOwl.value = false
      }, 200)
    }

    const submitName = () => {
      const name = studentName.value.trim()
      if (name) {
        emit('submit', name)
      }
    }

    return {
      studentName,
      showOwl,
      owlMessage,
      nameInput,
      handleFocus,
      handleBlur,
      submitName
    }
  }
}
</script>

<style scoped>
.name-entry-screen {
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
}

.title {
  font-family: 'Cinzel', serif;
  font-size: 3rem;
  margin-bottom: 15px;
}

.subtitle {
  font-size: 1.3rem;
  color: #E8D7C3;
  margin-bottom: 50px;
  font-style: italic;
}

.owl-container {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 30px;
  animation: slideIn 0.5s ease-out;
}

.owl {
  font-size: 4rem;
  animation: owlBounce 1s ease-in-out infinite;
}

@keyframes owlBounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-15px);
  }
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateX(50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.speech-bubble {
  position: absolute;
  left: calc(50% + 80px);
  top: 50%;
  transform: translateY(-50%);
  background: rgba(26, 26, 46, 0.95);
  border: 2px solid #FFD700;
  border-radius: 15px;
  padding: 15px 25px;
  white-space: nowrap;
  box-shadow: 0 0 20px rgba(255, 215, 0, 0.4);
}

.speech-bubble::before {
  content: '';
  position: absolute;
  left: -10px;
  top: 50%;
  transform: translateY(-50%);
  width: 0;
  height: 0;
  border-top: 10px solid transparent;
  border-bottom: 10px solid transparent;
  border-right: 10px solid #FFD700;
}

.speech-bubble p {
  color: #FFD700;
  font-size: 1rem;
  font-weight: 600;
  margin: 0;
  font-style: italic;
}

.input-container {
  position: relative;
  margin-bottom: 40px;
  display: flex;
  justify-content: center;
}

.sparkles {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 500px;
  height: 100px;
  pointer-events: none;
}

.sparkle {
  position: absolute;
  font-size: 1.2rem;
  opacity: 0;
  animation: sparkleAnimation 2s infinite;
}

.sparkle:nth-child(1) { top: 0; left: 10%; animation-delay: 0s; }
.sparkle:nth-child(2) { top: 10%; right: 10%; animation-delay: 0.2s; }
.sparkle:nth-child(3) { bottom: 10%; left: 15%; animation-delay: 0.4s; }
.sparkle:nth-child(4) { bottom: 0; right: 15%; animation-delay: 0.6s; }
.sparkle:nth-child(5) { top: 30%; left: 5%; animation-delay: 0.8s; }
.sparkle:nth-child(6) { top: 30%; right: 5%; animation-delay: 1s; }
.sparkle:nth-child(7) { bottom: 30%; left: 8%; animation-delay: 1.2s; }
.sparkle:nth-child(8) { bottom: 30%; right: 8%; animation-delay: 1.4s; }

@keyframes sparkleAnimation {
  0%, 100% {
    opacity: 0;
    transform: scale(0) rotate(0deg);
  }
  50% {
    opacity: 1;
    transform: scale(1.2) rotate(180deg);
  }
}

.submit-button {
  margin-bottom: 20px;
  box-shadow: 0 0 40px rgba(255, 215, 0, 0.6), 0 8px 20px rgba(0, 0, 0, 0.4);
}

.submit-button:disabled {
  opacity: 0.4;
  cursor: not-allowed;
  box-shadow: none;
  transform: none;
}

.submit-button:disabled:hover {
  transform: none;
  box-shadow: none;
  background: linear-gradient(135deg, rgba(116, 0, 1, 0.95), rgba(174, 0, 1, 0.95));
}

.hint {
  color: rgba(255, 215, 0, 0.6);
  font-size: 0.9rem;
  font-style: italic;
}

@media (max-width: 768px) {
  .title {
    font-size: 2rem;
  }
  
  .owl {
    font-size: 3rem;
  }
  
  .speech-bubble {
    position: static;
    transform: none;
    margin-top: 20px;
    white-space: normal;
  }
  
  .speech-bubble::before {
    display: none;
  }
  
  .input-container .magical-input {
    width: 90%;
  }
}
</style>
