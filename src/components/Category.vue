<template>
  <div>
    <div class="nav">
      <h2>
        <router-link id="back" :to="{name: 'Menu'}"><img class="icon" src="../../assets/meta/back.svg"></router-link>Quiz Category
      </h2>
    </div>
    <div v-if="topics.length" class="categories">
      <router-link v-bind:key="index" class="btn" v-for="(topic, index) in topics" :to="{name: 'Question', params: {topic: topic.id}}">
        {{topic.title}}
      </router-link>
    </div>
    <div class="loading" v-else-if="error">
      <p>Could not load questions, please check your network.</p>
    </div>
    <Spinner v-else />
  </div>
</template>

<script>

import Constants from '../constants/Constants.js'
import Spinner from './Spinner'

export default {
  name: 'Category',
  components: {
    Spinner
  },
  data: function () {
    return {
      topics: [],
      error: false
    }
  },
  mounted: function () {
    let _self = this
    fetch(`${Constants.REMOTE_DATA}topics.json`)
      .then(response => {
        if (response.ok) {
          return response.json()
        } else {
          throw new Error('Something went wrong')
        }
      })
      .then((data) => {
        _self.topics = data
      })
      .catch(error => {
        window.alert(error)
        _self.error = true
      })
  }
}
</script>
<style>
.categories {
  margin-top: 50%;
}
</style>
