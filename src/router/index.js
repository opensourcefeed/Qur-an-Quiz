import Vue from 'vue'
import Router from 'vue-router'
import Menu from '@/components/Menu'
import Category from '@/components/Category'
import Question from '@/components/Question'
import Result from '@/components/Result'
import Page from '@/components/Page'
import ScoreBoard from '@/components/ScoreBoard'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Welcome from '@/components/Welcome'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Welcome',
      component: Welcome
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/menu',
      name: 'Menu',
      component: Menu
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/quiz/category',
      name: 'Category',
      component: Category
    },
    {
      path: '/quiz/question/:topic/:number?',
      name: 'Question',
      component: Question
    },
    {
      path: '/quiz/result',
      name: 'Result',
      component: Result
    },
    {
      path: '/page',
      name: 'Page',
      component: Page
    },
    {
      path: '/scoreboard',
      name: 'ScoreBoard',
      component: ScoreBoard
    }
  ]
})
