import Constants from '../constants/Constants'

export default {
  shuffle (array) {
    for (var i = array.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1))
      var temp = array[i]
      array[i] = array[j]
      array[j] = temp
    }
    return array
  },
  userId () {
    return '_' + Math.random().toString(36).substr(2, 9)
  },
  setUser (user) {
    console.log('Setting user ', user)
    window.localStorage.setItem(`${Constants.APP_STORAGE_KEY}-user`, JSON.stringify(user))
  },
  getUser () {
    return JSON.parse(window.localStorage.getItem(`${Constants.APP_STORAGE_KEY}-user`))
  },
  setAdShown () {
    window.localStorage.setItem(`${Constants.APP_STORAGE_KEY}-adShown`, new Date().getTime())
  },
  canShowAd () {
    if (!window.localStorage.getItem(`${Constants.APP_STORAGE_KEY}-adShown`)) {
      return true
    }
    let time = window.localStorage.getItem(`${Constants.APP_STORAGE_KEY}-adShown`)
    console.log(new Date().getTime() - time)
    return (new Date().getTime() - time) > Constants.AD_INTERVAL
  }
}
