<template>
  <!-- Loading animation container -->
  <div>
   <Spinner v-if="processing"/>
   <img id="title-logo" src="../../static/images/logo.jpg"/>
   <h1>Login</h1>
   <form autocomplete="off">
    <div class="error" v-if="error">{{error}}</div>
    <div>
      <label class="label-email">
        <input type="text" v-model="loginVo.userId" placeholder="Email or Phone" tabindex="1" required />
        <span class="required">Email or Phone</span>
      </label>
    </div>
    <div>
      <label class="label-password">
        <input type="password" v-model="loginVo.password" placeholder="Password" tabindex="2" required />
        <span class="required">Password</span>
      </label>
    </div>
    <div class="btn" @click="login">Log In</div>
    Don't have an account? Register <router-link :to="{name: 'Register'}">
      here
    </router-link> for free
  </form>

</div>
</template>

<script>
import Spinner from './Spinner'
import Constants from '../constants/Constants.js'
import CommonUtils from '../mixins/CommonUtils.js'

export default {
  name: 'Login',
  components: {
    Spinner
  },
  data: function () {
    return {
      loginVo: {
        userId: '',
        password: ''
      },
      error: '',
      processing: true
    }
  },
  mounted: function () {
    this.processing = false
  },
  methods: {
    login: function () {
      let _self = this
      this.processing = true
      fetch(`${Constants.REMOTE}login`, {
        body: JSON.stringify(this.loginVo),
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        },
        mode: 'cors'
      })
        .then(response => response.json())
        .then(function (data) {
          console.log(data)
          if (data.status === 'success') {
            CommonUtils.setUser(data.user)
            _self.$router.push({name: 'Menu'})
          } else {
            _self.error = data.reason
            _self.processing = false
          }
        })
        .catch((error) => {
          _self.error = error
          _self.processing = false
        })
    }
  }
}
</script>
<style scoped>
#title-logo {
  border-radius: 100%;
}
form {
  text-align: left;
  margin: auto;
  padding: 1rem;
}
form > div {
  margin-top: 1rem;
}
label {
  display: flex;
  flex-direction: column;
  order: 2;
  outline: none
}
label > span {
  order: 1;
  font-size: .8rem;
}
input {
  order: 2;
}
.btn {
  margin: auto;
  text-align: center;
  border-radius: 0;
  padding: .1rem;
  width: 5rem;
  height: 2rem;
  line-height: 2rem;
  margin-top: 1rem;
  margin-bottom: 1rem;
}
</style>
