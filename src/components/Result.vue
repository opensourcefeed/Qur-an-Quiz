<template>
  <div>
    <div class="nav">
      <h2>
        <a id="back-disabled" :to="{name: 'Category'}"><img class="icon" src="../../assets/meta/back-disabled.svg"></a>Result
      </h2>
    </div>
    <h3>Result</h3>
    You scored {{score * 100 / questionCount}}% by correctly answering {{score}} of total {{questionCount}} questions
    <form>
      <label>Name:</label>
      <input type="text" v-model="name">
      <router-link class="btn" :to="{'name': 'Category'}">Play Again</router-link>
    </form>
  </div>
</template>

<script>
import CommonUtils from '../mixins/CommonUtils.js'

export default {
  name: 'Result',
  data: function () {
    return {
      name: ''
    }
  },
  mounted: function () {
    this.name = CommonUtils.userId()
  },
  computed: {
    score: function () {
      return this.$store.state.data.score ? this.$store.state.data.score : ''
    },
    questionCount: function () {
      return this.$store.state.data.questions ? this.$store.state.data.questions.length : ''
    }
  },
  watch: {
    'score': function () {
      this.name = CommonUtils.userId()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h2 {
  margin-top: 0;
}

.video-responsive{
  margin-top: 5vh;
  overflow:hidden;
  padding-bottom:56.25%;
  position:relative;
  height:0;
}
.video-responsive iframe{
  left:0;
  top:0;
  height:100%;
  width:100%;
  position:absolute;
}
form input {
  margin: 1rem;
  padding: 1rem;
  margin-top: 2rem;
}
</style>
