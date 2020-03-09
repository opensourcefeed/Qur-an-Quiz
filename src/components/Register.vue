<template>
  <!-- Loading animation container -->
  <div>
   <Spinner v-if="processing"/>
   <img id="title-logo" src="../../static/images/logo.jpg"/>
   <h1>Register</h1>
   <form autocomplete="off">
    <div class="error" v-if="error">{{error}}</div>
    <div>
      <label>
        <input type="text" v-model="user.name" placeholder="Name" tabindex="1" required />
        <span class="required">Name</span>
      </label>
    </div>
    <div>
      <label>
        <input type="email" v-model="user.email" placeholder="Email" tabindex="1" required />
        <span class="required">Email</span>
      </label>
    </div>
    <div>
      <label>
        <input type="phone" v-model="user.phone" placeholder="Phone" tabindex="1" required />
        <span class="required">Phone (With country code)</span>
      </label>
    </div>
    <div>
      <label>
        <input type="password" v-model="user.password" placeholder="Password" tabindex="2" required />
        <span class="required">Password</span>
      </label>
    </div>
    <div>
      <label>
        <input type="password" v-model="user.confirmPassword" placeholder="Confirm Password" tabindex="2" required />
        <span class="required">Confirm Password</span>
      </label>
    </div>
    <div class="btn" @click='register'>Register</div>
     Already have an account? Login <router-link :to="{name: 'Login'}">
      here
    </router-link>
  </form>

</div>
</template>

<script>
import Spinner from './Spinner'
import Constants from '../constants/Constants.js'
import CommonUtils from '../mixins/CommonUtils.js'

export default {
  name: 'Register',
  components: {
    Spinner
  },
  data: function () {
    return {
      user: {
        name: '',
        email: '',
        phone: '',
        password: '',
        confirmPassword: ''
      },
      error: '',
      processing: false
    }
  },
  methods: {
    validate: function () {
      if (this.user.name === '') {
        this.error = 'Name can\'t be empty'
      } else if (this.user.email === '') {
        this.error = 'Email can\'t be empty'
      } else if (this.user.phone === '') {
        this.error = 'Phone can\'t be empty'
      } else if (this.user.password === '') {
        this.error = 'Password can\'t be empty'
      } else if (this.user.password !== this.user.confirmPassword) {
        this.error = 'Password and confirm password does n\'t match'
      } else {
        this.error = ''
      }
    },
    register: function () {
      console.log(this.user)
      this.processing = true
      this.validate()
      if (this.error) {
        this.processing = false
        return
      }
      delete this.user.confirmPassword
      let _self = this

      fetch(`${Constants.REMOTE}register`, {
        body: JSON.stringify(this.user),
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
          // window.localStorage.setItem(`${Constants.APP_STORAGE_KEY}-id`, data.id)
          if (data.status === 'success') {
            CommonUtils.setUser(data.user)
            _self.$router.push('/')
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
