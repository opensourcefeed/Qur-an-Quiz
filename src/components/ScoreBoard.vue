<template>
  <div>
    <div class="nav">
      <h2>
        <router-link id="back" :to="{name: 'Menu'}"><img class="icon" src="../../assets/meta/back.svg"></router-link>Score Board
      </h2>
    </div>
    <div class="content" v-if="loaded">
      <table>
        <thead>
          <td>Rank</td><td>Name</td><td>Best Score</td>
        </thead>
        <tbody>
          <tr v-bind:key="index" v-for="(record, index) in records">
            <td>{{index + 1}}</td>
            <td>{{record.name}}</td>
            <td>{{record.highest_score}}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <Spinner v-else />
    <div class="card" v-if="myRecord">
      <div class="name">{{myRecord.name}}</div>
      <table class="info">
        <tr>
          <td>Rank: {{myRecord.rank}}</td>
          <td>Best Score: {{myRecord.highest_score}}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import Constants from '../constants/Constants.js'
import Spinner from './Spinner'

export default {
  name: 'ScoreBoard',
  data: function () {
    return {
      records: [],
      myRecord: false,
      loaded: false
    }
  },
  components: {
    Spinner
  },
  methods: {
    fetchRecords: function () {
      let _self = this
      fetch(`${Constants.REMOTE}scores`, {mode: 'cors'})
        .then(response => response.json())
        .then(data => {
          _self.records = data
          _self.loaded = true
        })
        .catch((error) => {
          window.alert(error)
        })
    },
    fetchMyRecord: function () {
      let _self = this
      if (this.id) {
        fetch(`${Constants.REMOTE}scores/${this.id}`, {mode: 'cors'})
          .then(response => response.json())
          .then(function (data) {
            _self.myRecord = data
          })
          .catch((error) => {
            window.alert(error)
          })
      }
    }
  },
  mounted: function () {
    this.fetchMyRecord()
    this.fetchRecords()
  },
  computed: {
    id: function () {
      return window.localStorage.getItem(`${Constants.APP_STORAGE_KEY}-id`)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.content {
  margin-top: 3vh;
}
table {
  text-align: left;
  width: 100%;
}
td {
  background: white;
  padding: 1em;
  border: 1px solid #eee;
}
thead td {
  font-weight: bold
}
.card {
  background: var(--primary-color);
  padding-top: 1rem
}
.card td{
  background: none;
  border: 1px solid rgba(255, 255, 255, .2);
  width: 50%;
  font-size: 1rem;
}
.card td+td {
  text-align: left
}
.card .name {
  font-weight: bold;
  font-size: 24px;
  color: white;
}
</style>
