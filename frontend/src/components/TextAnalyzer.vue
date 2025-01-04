<template>
  <div class="text-analyzer">
    <textarea v-model="userInput" placeholder="Enter text here..." rows="10" cols="50"></textarea>
    <button @click="analyzeText">Analyze</button>
    
    <div v-if="results">
      <h2>Analysis Results</h2>
      <h3>Word Count</h3>
      <ul>
        <li v-for="(count, word) in results.word_count" :key="word">
          {{ word }}: {{ count }}
        </li>
      </ul>
      <h3>Sentiment Score</h3>
      <div class="sentiment-meter">
        <svg viewBox="0 0 100 50">
          <path d="M10,40 Q50,10 90,40" stroke="black" fill="none"/>
          <line :x1="needleX1" :y1="needleY1" :x2="needleX2" :y2="needleY2" stroke="red" stroke-width="2"/>
        </svg>
        <p>{{ results.sentiment.toFixed(2) }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userInput: '',
      results: null,
    };
  },
  computed: {
    needleX1() {
      return 50;
    },
    needleY1() {
      return 40;
    },
    needleX2() {
      const sentiment = this.results ? this.results.sentiment : 0;
      return 50 + 40 * Math.cos((sentiment + 1) * Math.PI / 2);
    },
    needleY2() {
      const sentiment = this.results ? this.results.sentiment : 0;
      return 40 - 40 * Math.sin((sentiment + 1) * Math.PI / 2);
    },
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
@import url("https://fonts.googleapis.com/css2?family=Bangers&family=Lato&display=swap");

.text-analyzer {
  max-width: 600px;
  margin: auto;
  text-align: center;
}
ul{
  list-style-type: None;
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
.sentiment-meter {
  margin: 20px 0;
}
</style>