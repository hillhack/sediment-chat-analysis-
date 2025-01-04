<template>
  <div class="text-analyzer">
    <textarea v-model="userInput" placeholder="Enter text here..." rows="10" cols="50"></textarea>
    <button @click="analyzeText">Analyze</button>
    
    <div v-if="results">
      <h2>Analysis Results</h2>
      <div class="results-container">
        <div class="word-count">
          <h3>Word Count</h3>
          <ul class="no-bullets">
            <li v-for="(count, word) in results.word_count" :key="word">
              {{ word }}: {{ count }}
            </li>
          </ul>
        </div>
        <div class="sentiment-score">
          <h3>Sentiment Score</h3>
          <div class="sentiment-meter">
            <SentimentMeter :sentimentScore="results.sentiment.toFixed(2)" />
            <p>{{ results.sentiment.toFixed(2) }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SentimentMeter from '@/components/SentimentMeter.vue';

export default {
  components: {
    SentimentMeter,
  },
  data() {
    return {
      userInput: '',
      results: null,
    };
  },
  methods: {
    async analyzeText() {
      try {
        const response = await fetch('http://localhost:5000/analyze', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ text: this.userInput }),
        });
        this.results = await response.json();
      } catch (error) {
        console.error('Error analyzing text:', error);
      }
    },
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Bangers&display=swap');

.text-analyzer {
  max-width: 600px;
  margin: auto;
  text-align: center;
}
textarea {
  width: 100%;
  height: 200px;
  font-size: 1.4em;
  text-align: center;
  margin: 1em 0;
  font-family: "Bangers", cursive;
  padding: 0.5em 0;
  margin-bottom: 10px;
}
button {
  font-size: 1.2em;
  padding: 0.5em 1em;
  margin-bottom: 1em;
  cursor: pointer;
  font-family: "Bangers", cursive;
  background: rgb(255, 240, 33);
  transition: linear 0.2s;
  border: 1.5px solid black;
  box-shadow: 2px 2px white;

  &:hover {
    transform: translate(-2px, -2px);
    box-shadow: 4px 4px black;
  }
}
.no-bullets {
  list-style-type: none;
  padding: 0;
}
.results-container {
  display: flex;
  justify-content: space-between;
}
.word-count, .sentiment-score {
  width: 48%;
}
</style>