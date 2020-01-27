<template>
  <div>
    <div class="nav">
      <h2>
        <router-link id="back" :to="{name: 'Category'}"><img class="icon" src="../../assets/meta/back.svg"></router-link>{{topic}}
      </h2>
    </div>

    <div v-if="question" id="quiz" >
      <p class="progress">Question {{questionNum}} of {{questions.length}}</p>
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

export default {
  name: 'question',
  data: function () {
    return {
      selected: false,
      selectedAnswer: ''
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
    loadData: function () {
      let _self = this
      try {
        axios.get(`/static/data/${this.topicId}.json`)
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
            console.log('hi')
            data.score = 0
            console.log(data)
          })
      } catch (e) {
        console.log(e)
      }
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
    this.loadData()
  },
  watch: {
    'questionNum': function () {
      this.selected = false
      this.selectedAnswer = ''
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
.progress {
  text-align: left;
  margin-bottom: 0px;
  padding: 0 10px;
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
