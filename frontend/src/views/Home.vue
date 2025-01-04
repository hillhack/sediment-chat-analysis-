<template>
  <div class="home">
    <h1>Sediment Chat Analysis</h1>
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
.home {
  text-align: center;
  margin: 20px;
}
</style>