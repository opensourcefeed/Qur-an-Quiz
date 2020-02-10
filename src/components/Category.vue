<template>
  <div>
    <div class="nav">
      <h2>
        <router-link id="back" :to="{name: 'Menu'}"><img class="icon" src="../../assets/meta/back.svg"></router-link>Quiz Category
      </h2>
    </div>
    <div class="categories">
      <router-link v-bind:key="index" class="btn" v-for="(topic, index) in topics" :to="{name: 'Question', params: {topic: topic.id}}">
        {{topic.title}}
      </router-link>
    </div>
  </div>
</template>

<script>

import topics from '../../static/data/topics.json'
import Constants from '../constants/Constants.js'

export default {
  name: 'Category',
  data: function () {
    return {
      topics: []
    }
  },
  mounted: function () {
    this.topics = topics
    let _self = this
    fetch(`${Constants.REMOTE_DATA}topics.json`)
      .then(data => data.json())
      .then((data) => {
        _self.topics = data
      })
  }
}
</script>
<style>
.categories {
  margin-top: 50%;
}
</style>
