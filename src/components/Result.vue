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
    <form>
      <p>We store your score & name to populate scoreboard</p>
      <label>Name:</label>
      <input type="text" id="name" v-model="name">
      <div class="btn" @click="saveScore">Submit</div>
    </form>
  </div>
</template>

<script>
import CommonUtils from '../mixins/CommonUtils.js'
import Constants from '../constants/Constants.js'

export default {
  name: 'Result',
  data: function () {
    return {
      name: ''
    }
  },
  methods: {
    populateName: function () {
      console.log('inside get name')
      let _self = this
      if (this.id) {
        console.log('inside if')
        fetch(`${Constants.REMOTE}scores/${this.id}`, {mode: 'cors'})
          .then(response => response.json())
          .then(function (data) {
            _self.name = data.name
          })
          .catch((error) => {
            window.alert(error)
          })
      } else {
        console.log('inside else')
        _self.name = CommonUtils.userId()
      }
    },
    saveScore () {
      let data = {}
      let _self = this
      data.name = this.name
      data.score = this.score ? this.score : 0
      if (this.id) {
        data.id = this.id
      }
      fetch(`${Constants.REMOTE}scores`, {
        body: JSON.stringify(data),
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        },
        mode: 'cors'
      })
        .then(response => response.json())
        .then(function (data) {
          console.log(data)
          window.localStorage.setItem(`${Constants.APP_STORAGE_KEY}-id`, data.id)
          _self.$router.push('/')
        })
        .catch((error) => {
          window.alert(error)
          _self.$router.push('/')
        })
    }
  },
  mounted: function () {
    this.populateName()
  },
  computed: {
    score: function () {
      return this.$store.state.data.score ? this.$store.state.data.score : ''
    },
    questionCount: function () {
      return this.$store.state.data.questions ? this.$store.state.data.questions.length : ''
    },
    id: function () {
      return window.localStorage.getItem(`${Constants.APP_STORAGE_KEY}-id`)
    }
  },
  watch: {
    'score': function () {
      this.name = this.populateName()
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
