<template>
  <div>
    <div class="nav">
      <h2>
        <router-link id="back" :to="{name: 'Menu'}"><img class="icon" src="../../assets/meta/back.svg"></router-link>Quiz Category
      </h2>
    </div>
    <div class="channels">
      <div v-bind:key="index" class="channel" v-for="(topic, index) in topics">
        <router-link :to="{name: 'Question', params: {topic: topic.id}}">
          <img src="../../assets/logo/placeholder.png">
          <br/>
          {{topic.title}}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>

import topics from '../../static/data/topics.json'

export default {
  name: 'Category',
  computed: {
    topics () {
      return topics
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.channels {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: .2em;
  margin-top: 2vh
}
.channel {
    background-color: white;
    padding: .5em;
    box-shadow: 1px 1px 1px #ddd;
    position: relative;
    height: 140px;
    word-break: break-all
}
.channel a {
  position: absolute;
  left: 0;
  right: 0;
  bottom: .5em;
}
.channel img {
  display: block;
  margin: auto;
  max-width: 80%;
  max-height: 84px
}
</style>
