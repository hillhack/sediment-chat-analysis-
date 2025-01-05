<template>
  <div class="home">
    <h1>Sentiment Chat Analysis</h1>
    <TextAnalyzer />
  </div>
</template>

<script>
import TextAnalyzer from '@/components/TextAnalyzer.vue';

export default {
  name: 'Home',
  components: {
    TextAnalyzer,
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Mystery+Quest&family=Noto+Sans+Warang+Citi&display=swap');

h1 {
  font-family: "Mystery Quest", serif;
  font-weight: 400;
  font-style: normal;
  font-size: 100px;
}
.home { 
  text-align: center;
  margin: 20px;
}

</style>
