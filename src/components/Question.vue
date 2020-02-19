<template>
  <div>
    <div class="nav">
      <h2>
        <router-link id="back" :to="{name: 'Category'}"><img class="icon" src="../../assets/meta/back.svg"></router-link>{{topic}}
      </h2>
    </div>

    <div v-if="question && loaded" id="quiz" >
      <div class="info">
        <p class="progress">Question {{questionNum}} of {{questions.length}}</p>
        <p class="timer">Remaining time {{remainingTime}}</p>
      </div>
      <p class="question">{{question.question}}</p>
      <div class="option btn" :class="{correct: selectedAnswer === option && option == question.answer, incorrect: selectedAnswer === option && option !== question.answer}" @click="markAnswer(option)" v-bind:key="index" v-for="(option, index) of question.options">{{option}}</div>
      <div v-if="selected">
        <router-link class="option btn" v-if="questionNum < questions.length" :to="{name: 'Question', params: {category: topicId, number: Number(questionNum) + 1}}">
          CONTINUE
        </router-link>
        <router-link class="option btn" v-else :to="{name: 'Result'}">
          Finish
        </router-link>
      </div>

    </div>
    <div class="loading" v-else-if="error">
      <p>Could not load questions, please check your network.</p>
    </div>
    <Spinner v-else />

    <!-- <div class="video-responsive">
      <div v-if="error">
        {{error.message}}<br/><br/>
        technical : {{error.technical}}
      </div>
      <div id="video-frame"></div>
      <div v-if="!loaded" class="loader"></div>
    </div>
    <a class="external" @click="fullscreen" v-if="loaded"><img src="../assets/meta/fullscreen.svg">Play Fullscreen</a>
    <Viewers v-if="videoId && !isFullscreen" :videoId="videoId"></Viewers>
    <router-link class="link" :to="{name: 'Videos', params: {categoryId: categoryId, channelId: channelId, live: true}}">
      Latest videos from {{channel.name}}
    </router-link> -->

  </div>
</template>

<script>
import axios from 'axios'
import CommonUtils from '../mixins/CommonUtils.js'
import Constants from '../constants/Constants.js'
import Spinner from './Spinner'

export default {
  name: 'question',
  components: {
    Spinner
  },
  data: function () {
    return {
      selected: false,
      selectedAnswer: '',
      loaded: false,
      error: false,
      remainingTime: Constants.TIMEOUT
    }
  },
  methods: {
    markAnswer: function (answer) {
      console.log('asking to mark answer')
      console.log(this.selected)
      if (this.selected) return
      this.selected = true
      this.selectedAnswer = answer
      if (answer === this.question.answer) {
        this.$store.state.data.score += 1
      }
      console.log('score ' + this.$store.state.data.score)
    },
    updateTimer: function () {
      console.log(this)
      this.remainingTime -= 1
      if (this.remainingTime === 0) {
        if (this.questionNum < this.questions.length) {
          this.$router.push({name: 'Question', params: {category: this.topicId, number: Number(this.questionNum) + 1}})
        } else {
          this.$router.push({name: 'Result'})
        }
      }
      this.timer = setTimeout(this.updateTimer, 1000)
    },
    loadData: function () {
      let _self = this
      axios.get(`${Constants.REMOTE_DATA}${this.topicId}.json`)
        .then((data) => {
          data = data.data
          console.log(data)
          _self.$store.commit('setData', data)
          let questions = CommonUtils.shuffle(data.questions)
          for (let question of questions) {
            question.options = CommonUtils.shuffle(question.options)
          }
          let questionCount = questions.length > Constants.QUESTION_COUNT ? Constants.QUESTION_COUNT : questions.length
          data.questions = questions.splice(0, questionCount)
          data.score = 0
          _self.loaded = true
          _self.updateTimer()
        })
        .catch(function (e) {
          _self.error = true
        })
    }
  },
  computed: {
    topicId () {
      return this.$route.params.topic
    },
    topic () {
      return this.$store.state.data.title ? this.$store.state.data.title : ''
    },
    questionNum () {
      return this.$route.params.number ? this.$route.params.number : 1
    },
    questions () {
      return this.$store.state.data.questions ? this.$store.state.data.questions : []
    },
    question () {
      return this.$store.state.data.questions && this.questionNum <= this.$store.state.data.questions.length ? this.$store.state.data.questions[this.questionNum - 1] : {}
    }
  },
  mounted: function () {
    console.log('inside mounter...')
    // this.updateTimer()
    this.loadData()
  },
  beforeDestroy: function () {
    console.log('clearing timeout')
    clearTimeout(this.timer)
  },
  beforeRouteLeave: function (from, to, next) {
    console.log('leaving route', from, to)
    next()
  },
  watch: {
    'questionNum': function () {
      this.selected = false
      this.selectedAnswer = ''
      clearTimeout(this.timer)
      this.remainingTime = Constants.TIMEOUT
      this.updateTimer()
      console.log('questionNum changed')
      if (this.questionNum === 1 || !this.$store.state.data.questions) {
        this.loadData()
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h2 {
  margin-top: 0;
}
#quiz {
  background: white;
}
.info {
  display: flex;
  border-bottom: 1px solid #eee;
  padding-bottom: .5rem;
  margin-bottom: .5rem
}
.progress, .timer {
  margin-bottom: 0px;
  padding: 0 10px;
  flex: 50%;
}
.progress {
  text-align: left;
}
.timer {
  text-align: right;
}
.question {
  text-align: left;
  font-size: 1.4rem;
  margin-top: auto;
  font-size: 32px;
  padding: 0 10px;
}
.option {
  padding: 10px;
  margin: 20px 10px;
  border-radius: 10px;
  cursor: pointer;
  font-size: 1.1rem;
  color: black;
  border: 3px solid var(--primary-color)
}
.correct {
  border: 3px solid green;
}
.incorrect {
  border: 3px solid red
}
</style>
