<template>
  <div>
    <div class="nav">
      <h2>
        <router-link id="back" :to="{name: 'Menu'}"><img class="icon" src="../../assets/meta/back.svg"></router-link> {{page.title}}
      </h2>
    </div>
    <div class="content">
     <iframe :src="page.url" target="_top"/>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Page',
  computed: {
    page: function () {
      return {
        'title': 'FilmBiopsy',
        'url': 'https://www.filmbiopsy.com'
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.content {
  margin-top: 3vh
}
</style>
