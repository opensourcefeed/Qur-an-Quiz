<template>
  <div id="app">
    <router-view/>
    <Updater @close="updateAvailable = false" :update="update" v-if="updateAvailable"/>
  </div>
</template>

<script>
import Constants from './constants/Constants'

export default {
  name: 'App',
  data: function () {
    return {
      updateAvailable: false,
      update: {}
    }
  },
  methods: {
    onDeviceReady: function () {
      console.log('device ready')

      document.removeEventListener('deviceready', this.onDeviceReady)

      // define backbutton functionality
      document.addEventListener('backbutton', this.onBackKeyDown, false)
    },
    onBackKeyDown: function (e) {
      e.preventDefault()
      console.log('pressed backbutton')
      let back = document.getElementById('back')
      if (back && back.getAttribute('class') !== 'disabled') {
        back.click()
      } else {
        // Exit app
        if (navigator.app) {
          navigator.app.exitApp()
        } else if (navigator.device) {
          navigator.device.exitApp()
        } else {
          window.close()
        }
      }
    }
  },
  mounted () {
    // let localStorage = window.localStorage
    // let data = JSON.parse(localStorage.getItem(STORAGE_KEY)) || json
    let _self = this
    // this.$store.commit('setData', data)

    // Try to load meta data, save it on local
    fetch(`${Constants.REMOTE_DATA}meta.json`)
      .then(response => {
        if (response.ok) {
          return response.json()
        } else {
          throw new Error('Something went wrong')
        }
      })
      .then((data) => {
        // alert(`Latest Version: ${data.latestVersion}\
        //   Installed Version: ${this.buildInfo.version}
        //   Update Available: ${typeof this.buildInfo.version !== 'undefined' && data.latestVersion > this.buildInfo.version}`)
        if (typeof this.buildInfo.version !== 'undefined' && data.latestVersion > this.buildInfo.version) {
          _self.update.version = this.buildInfo.version
          _self.update.latestVersion = data.latestVersion
          _self.updateAvailable = true
        }
      })
      .catch(error => {
        window.alert(error)
      })

    // load scripts
    let script = document.createElement('script')
    script.setAttribute('src', 'cordova.js')
    document.head.appendChild(script)

    document.addEventListener('deviceready', this.onDeviceReady)
  },
  computed: {
    buildInfo: function () {
      return window.BuildInfo ? window.BuildInfo : {}
    }
  }
}

</script>

<style>
:root {
  --primary-color: #00407f;
}
#app {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  padding-top: 3.2rem;
}
h1, h2 {
  font-weight: normal;
  margin-bottom: 0;
}
h2 {
  margin-top: 0;
  font-size: 1.2rem;
  text-transform: uppercase;
}
a {
  color: white;
  text-decoration: none;
}
body {
  max-width: 720px;
  margin: auto;
}
.nav {
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  padding: 1em .5em;
  background: var(--primary-color);
  color: white;
  text-align: left;
  box-shadow: 1px 1px 1px rgba(0, 0, 0, .5);
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1
}
.icon {
  vertical-align: middle;
  margin-right: .5em;
  padding-right: .5em;
  border-right: 1px solid rgba(0, 0, 0, .2)
}
.nav a {
  color: white;
}
.external {
  background: var(--primary-color);
  padding: 1rem;
  color: white;
  display: block;
  margin-top: 5vh
}
.external img {
  vertical-align: middle;
}
.link {
  color: var(--primary-color);
  text-decoration: underline;
}
.btn {
  display: block;
  cursor: pointer;
  background: var(--primary-color);
  color: white;
  padding: 20px 10px;
  border-radius: 10px;
  margin: auto;
  margin: 10px;
}
.error {
  margin-top: 50vh;
  color: black;
}
</style>
