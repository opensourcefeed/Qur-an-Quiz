<template>
  <div>
    <div class="nav">
      <h2>
        <router-link id="back" :to="{name: 'Menu'}"><img class="icon" src="../../assets/meta/back.svg"></router-link> FilmBiopsy
      </h2>
    </div>
    <Spinner v-if="!ready" />
    <div class="content">
     <h1>{{title}}</h1>
     <p>{{content}}</p>
    </div>
  </div>
</template>

<script>
import Constants from '../constants/Constants.js'
import Spinner from './Spinner'

export default {
  name: 'Page',
  components: {
    Spinner
  },
  computed: {
    key: function () {
      return this.$route.params.key
    }
  },
  data: function () {
    return {
      ready: false,
      title: '',
      content: 'Could not load content'
    }
  },
  mounted: function () {
    let _self = this
    fetch(`${Constants.REMOTE_DATA}pages/${_self.key}.json`)
      .then(response => {
        if (response.ok) {
          return response.json()
        } else {
          throw new Error('Something went wrong')
        }
      })
      .then((data) => {
        _self.title = data.title
        _self.content = data.content
        _self.ready = true
      })
      .catch(() => {
        _self.ready = true
      })
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.content {
  margin-top: 3vh
}
h1 {
  font-size: 2rem;
  border-bottom: 1px dashed #ccc
}
p {
  text-align: left;
  padding: 1rem;
  line-height: 1.5rem;
}
</style>
