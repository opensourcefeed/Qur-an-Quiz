import Vue from 'vue'
import Router from 'vue-router'
import Menu from '@/components/Menu'
import Category from '@/components/Category'
import Question from '@/components/Question'
import Update from '@/components/Update'
import Result from '@/components/Result'
import Page from '@/components/Page'
import ScoreBoard from '@/components/ScoreBoard'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Menu',
      component: Menu
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
      path: '/update',
      name: 'Update',
      component: Update
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
