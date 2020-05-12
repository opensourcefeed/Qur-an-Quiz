<template>
  <div>
    <div class="nav">
      <h2><a><img class="icon" src="../../assets/meta/back-disabled.svg"></a>Menu</h2>
    </div>
    <div class="categories">
      <img id="title-logo" src="../../static/images/logo.png"/>
      <div class="group">
        <div class="item">
          <router-link :to="{name: 'Chapter'}">
            <img src="../../assets/meta/quiz.svg"><br/>
            Qur'an Quiz
          </router-link>
        </div>
       <!--  <div class="item">
          <router-link :to="{name: 'ScoreBoard'}">
            <img src="../../assets/meta/scoreboard.svg"><br/>
            ScoreBoard
          </router-link>
        </div>
        <div class="item">
          <a href="http://filmbiopsy.com">
            <img src="../../assets/meta/news.svg"><br/>
            Film News
          </a>
        </div> -->
      </div>
    </div>
<!--       <hr> -->
<!--       <div class="category">
        <a @click="openRateDialog"><img class="icon" src="../../assets/meta/star.svg">Rate Us</a>
      </div>
      <div class="category">
        <a @click="exitApp"><img class="icon" src="../../assets/meta/exit.svg">Exit</a>
      </div>
    </div>
    <hr>
    <router-link class="link" :to="{name: 'Page', params: {key: 'beta'}}">
      BETA RELEASE NOTES
    </router-link> -->
  </div>
</template>

<script>
import {openRateDialog} from '../mixins/rating.js'
export default {
  name: 'Menu',
  computed: {
    categories () {
      return this.$store.state.data.categories || []
    }
  },
  methods: {
    exitApp: function () {
      if (navigator.app) {
        navigator.app.exitApp()
      } else if (navigator.device) {
        navigator.device.exitApp()
      } else {
        window.close()
      }
    },
    openRateDialog: function () {
      openRateDialog()
    }
  },
  data () {
    return {
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.categories {
  margin-top: 5vh;
}
.category a{
  padding: 1em 1em;
  display: block;
  margin: .2em 1em;
  background: var(--primary-color);
  color: black;
  cursor: pointer;
  text-align: left;
  text-transform: uppercase;
  box-shadow: 1px 1px 1px 1px #eee;
}
hr {
  border: none;
  margin-bottom: 2em;
}
#title-logo {
  width: 128px;
  border-radius: 100%;
}
.group {
  display: grid;
  grid-template-columns: repeat(1, 1fr);
  grid-gap: .2em;
  margin-top: 2vh;
  margin: 16px;
}
.item {
    background-color: var(--primary-color);
    padding: .5em;
    box-shadow: 1px 1px 1px #ddd;
    position: relative;
    height: 80px;
    word-break: break-all;
    width: 30%;
    margin: auto;
}
.item a {
  position: absolute;
  left: 0;
  right: 0;
  bottom: .5em;
}
.item img {
  display: block;
  margin: auto;
  max-width: 80%;
  max-height: 84px;
  width: 40px;
}
p {
  border-top: 1px dashed #ddd;
  padding-top: 1rem;
}
</style>
