<template>
  <div>
    <div class="nav">
      <h2>
        <a id="back-disabled" :to="{name: 'Category'}"><img class="icon" src="../../assets/meta/back-disabled.svg"></a>Result
      </h2>
    </div>
    <h3>Result</h3>
    You scored {{score * 100 / questionCount}}% by correctly answering {{score}} of total {{questionCount}} questions
    <hr>
      <router-link class="btn" :to="{name: 'Chapter'}">
        <img src="../../assets/meta/quiz.svg"><br/>
        Try Again
      </router-link>
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
  },
  computed: {
    score: function () {
      return this.$store.state.data.score ? this.$store.state.data.score : ''
    },
    levelId: function () {
      return this.$store.state.data.level ? this.$store.state.data.level : ''
    },
    categoryId: function () {
      return this.$store.state.data.category ? this.$store.state.data.category : ''
    },
    questionCount: function () {
      return this.$store.state.data.questions ? this.$store.state.data.questions.length : ''
    },
    id: function () {
      return CommonUtils.getUser().id
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h2 {
  margin-top: 0;
}
form {
  margin: 10px
}
form input {
  margin: 1rem;
  padding: 1rem;
  margin-top: 2rem;
  border: 1px solid #eee;
  font-size: 1rem;
  width: 60%;
}
hr {
  border-top: 1px solid #eee;
  margin-bottom: 2rem;
}
</style>
