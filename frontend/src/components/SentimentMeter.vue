<template>
    <div class="sentiment-meter">
      <div class="gauge">
        <svg viewBox="0 0 200 120" xmlns="http://www.w3.org/2000/svg">
          <!-- Semi-circular arc -->
          <path
            d="M 20,100 A 70,70 0 0,1 184,100"
            stroke="lightgray"
            stroke-width="35"
            fill="none"
          />
          <!-- Needle -->
          <line
            x1="100"
            y1="90"
            :x2="needleX"
            :y2="needleY"
            stroke="black"
            stroke-width="3"
          />
          <!-- Needle center -->
          <circle cx="100" cy="90" r="5" fill="black" />
          <!-- Labels -->
          <text
            v-for="(label, index) in labels"
            :key="index"
            :x="labelPositions[index].x"
            :y="labelPositions[index].y"
            :text-anchor="labelPositions[index].anchor"
            dominant-baseline="middle"
          >
            {{ label }}
          </text>
        </svg>
      </div>
    </div>
</template>
  
<script>
  export default {
    props: {
      sentimentScore: {
        type: Number,
        required: true,
        validator: (value) => value >= -1 && value <= 1,
      },
    },
    data() {
      return {
        labels: ["Happy", "Good", "Average", "Poor", "Bad"],  // Reversed label order
        needleLength: 50, // Adjust the length of the needle here
      };
    },
    computed: {
      // Calculate angle (90° to -90°) based on sentimentScore
      angle() {
        // Map sentiment score from [-1, 1] to [90, -90]
        return 90 - ((this.sentimentScore + 1) / 2) * 180;
      },
      // Needle position with adjusted needle length
      needleX() {
        const centerX = 100;
        return centerX + this.needleLength * Math.cos((this.angle * Math.PI) / 180);
      },
      needleY() {
        const centerY = 90;
        return centerY - this.needleLength * Math.sin((this.angle * Math.PI) / 180);
      },
      // Labels positions along the arc (Reversed order)
      labelPositions() {
        const radius = 66; // Radius for labels
        const centerX = 100;
        const centerY = 90;
        const angles = [0, 45, 90, 135, 180];  // Angles for label positions
        return angles.map((angle) => {
          const rad = (angle * Math.PI) / 180;
          return {
            x: centerX + radius * Math.cos(rad),
            y: centerY - radius * Math.sin(rad),
            anchor: angle === 0 ? "start" : angle === 180 ? "end" : "middle",
          };
        });
      },
    },
  };
</script>
  
<style scoped>
  .sentiment-meter {
    text-align: center;
    font-family: Arial, sans-serif;
  }
  
  .gauge {
    width: 200px;
    height: 120px;
  }
  
  path {
    fill: none;
  }
  
  text {
    font-size: 12px;
    fill: black;
  }

  circle {
    fill: red;
  }
  
  line {
    stroke: red;
    transform-origin: 100px 90px;
  }
</style>