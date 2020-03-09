<template>
  <div>
    <Spinner />
  </div>
</template>

<script>
import Constants from '../constants/Constants.js'
import Spinner from './Spinner'

export default {
  name: 'Welcome',
  components: {
    Spinner
  },
  mounted: function () {
    let redirectTo = ''
    if (window.localStorage.getItem(`${Constants.APP_STORAGE_KEY}-user`)) {
      redirectTo = '/menu'
    } else {
      redirectTo = '/login'
    }
    this.$router.push(redirectTo)
  }
}

</script>
