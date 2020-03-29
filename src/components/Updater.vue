<template>
  <div class="popup-overlay">
    <div class="popup">
      <p>A new update is available. <br/>Would you like to update?</p>
      <table>
        <tr>
          <td>Latest Version</td>
          <td>{{this.update.latestVersion}}</td>
        </tr>
        <tr>
          <td>Current Version</td>
          <td>{{this.update.version}}</td>
        </tr>
      </table>
      <div class="btn" @click="openPlayStore">Update</div>
      <div class="btn" @click="$emit('close')">Later</div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Updater',
  props: ['update'],
  mounted: function () {
    console.log(this.update)
    console.log(this.update.version)
  },
  methods: {
    openPlayStore: function () {
      try {
        window.cordova.plugins.market.open('com.filmbiopsy.mobileapp')
      } catch (e) {
        console.log('failed to open market')
      }
    }
  }
}

</script>

<style scoped>
.btn {
  padding: .5rem;
  border-radius: 0;
  text-transformation: uppercase
}
.popup-overlay {
  position: absolute;
  background: #00000099;
  top: 0;
  height: 100%;
  width: 100%;
}
.popup {
  border: 1px solid #ddd;
  margin-top: 50%;
  background: white;
  padding: 1rem;
}
.popup p {
  font-size: 1.2rem;
  color: #c32526
}
table {
  width: 100%;
  text-align: left;
  padding: 1rem;
}
td {
  border: 1px solid #eee;
  padding: 1rem;
}
</style>
