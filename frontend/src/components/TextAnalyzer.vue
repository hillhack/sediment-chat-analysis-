<template>
  <div class="text-analyzer">
    <textarea v-model="userInput" placeholder="Enter text here..." rows="10" cols="50"></textarea>
    <button @click="analyzeText">Analyze</button>
    
    <div v-if="results">
      <h2>Analysis Results</h2>
      <h3>Word Count</h3>
      <pre>{{ results.word_count }}</pre>
      <h3>Sentiment Score</h3>
      <p>{{ results.sentiment }}</p>
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
.text-analyzer {
  max-width: 600px;
  margin: auto;
  text-align: center;
}
textarea {
  width: 100%;
  margin-bottom: 10px;
}
button {
  padding: 10px 20px;
  font-size: 16px;
}
</style>